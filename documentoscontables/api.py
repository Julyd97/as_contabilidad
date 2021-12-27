from flask import request, Blueprint
from flask_restful import Api, Resource

from documentoscontables.schemas import DocumentosContablesSchema
from documentoscontables.models import DocumentosContables

documentoscontables_app = Blueprint('documentoscontables_app', __name__)
documentoscontables_schema = DocumentosContablesSchema()

api = Api(documentoscontables_app)

class DocumentosContablesListResource(Resource):
    def get(self, num_cedula=None):
        if num_cedula == None:
            documentos = DocumentosContables.get_all()
            result = documentoscontables_schema.dump(documentos, many=True)
        else:  
            proveedores = DocumentosContables.query.filter(DocumentosContables.numDocumento.like(str(num_cedula) + '%')).all()
            if proveedores == []:
                return  {'message': 'Ocurrio un error buscando con el numero dado'}, 404
            else:         
                result = documentoscontables_schema.dump(proveedores, many=True)
        return result, 201
    def post(self):
        data = request.get_json()
        documentoscontables_dict = documentoscontables_schema.load(data)
        documentos = DocumentosContables(fecha = documentoscontables_dict['fecha'],
                                        descripcion = documentoscontables_dict['descripcion'],
                                        consecutivo = documentoscontables_dict['consecutivo'],
                                        prefijo = documentoscontables_dict['prefijo']
        )  
        documentos.save()
        resp = documentoscontables_schema.dump(documentos)
        return resp, 201
    
    
        
class DocumentosContablesResource(Resource):
    def get(self, documento_id):
        proveedor = DocumentosContables.get_by_id(documento_id)
        if proveedor is None:
            raise ('El proveedor no existe')
        resp = documentoscontables_schema.dump(proveedor)
        return resp
    def put(self, proveedor_id):
        documento = DocumentosContables.get_by_id(proveedor_id)
        if documento is None:
            raise ('El proveedor no existe')
        data = request.get_json()
        try:
            documento_dict = documentoscontables_schema.load(data)
            documento.fecha = documento_dict['fecha']
            documento.descripcion = documento_dict['descripcion']
            documento.consecutivo = documento_dict['consecutivo']
            documento.prefijo = documento_dict['prefijo']
            
            
            documento.save()
            resp = documentoscontables_schema.dump(documento)
            return resp, 201
        except:
            return {'message': 'Ocurrio un error modificando el proveedor'}, 400
    def  delete(self, documento_id):
        documento = DocumentosContables.get_by_id(documento_id)
        if documento is None:
            raise ('El proveedor no existe')
        try:
            documento.delete()
            return 201
        except:
            return {'message': 'Un error ocurrio un error eliminando el proveedor'}, 400

api.add_resource(DocumentosContablesListResource, '/api/v1.0/documentoscontables/', endpoint='documentoscontables_list_resource')
api.add_resource(DocumentosContablesResource, '/api/v1.0/documentoscontables/<int:documento_id>', endpoint='documentoscontables_resource')