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
                return  {'message': 'El documento buscado no existe','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 404
            else:         
                result = documentoscontables_schema.dump(proveedores, many=True)
        return result, 201
    def post(self):
        data = request.get_json()
        documentoscontables_dict = documentoscontables_schema.load(data)
        documentos = DocumentosContables(fecha = documentoscontables_dict['fecha'],
                                        descripcion = documentoscontables_dict['descripcion'],
                                        consecutivo = documentoscontables_dict['consecutivo'],
                                        prefijo = documentoscontables_dict['prefijo'],
                                        tipodocumento = documentoscontables_dict['tipodocumento'],
                                        plantilla = documentoscontables_dict['plantilla']
        )  
        documentos.save()
        resp = documentoscontables_schema.dump(documentos)
        return {'message':'El documento se creo exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
    
    
        
class DocumentosContablesResource(Resource):
    def get(self, documento_id):
        documento = DocumentosContables.get_by_id(documento_id)
        if documento is None:
            return  {'message': 'El documento buscado no existe','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        resp = documentoscontables_schema.dump(documento)
        return resp
    def put(self, documento_id):
        documento = DocumentosContables.get_by_id(documento_id)
        data = request.get_json()
        if documento is None:
            return  {'message': 'El documento buscado no existe','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        try:
            documento_dict = documentoscontables_schema.load(data)
            print(documento_dict)
            documento.fecha = documento_dict['fecha']
            documento.descripcion = documento_dict['descripcion']
            documento.consecutivo = documento_dict['consecutivo']
            documento.prefijo = documento_dict['prefijo']
            documento.tipodocumento = documento_dict['tipodocumento']
            
            
            documento.save()
            resp = documentoscontables_schema.dump(documento)
            return {'message':'El documento se modifico exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Ocurrio un error modificando el proveedor','alerta':'alert-warning','icon':'#exclamation-triangle-fill'}, 400
    def  delete(self, documento_id):
        documento = DocumentosContables.get_by_id(documento_id)
        if documento is None:
            return  {'message': 'El documento buscado no existe','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        try:
            documento.delete()
            return {'message':'El documento se elimino exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Un error ocurrio un error eliminando el proveedor','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 400

api.add_resource(DocumentosContablesListResource, '/api/v1.0/documentoscontables/', endpoint='documentoscontables_list_resource')
api.add_resource(DocumentosContablesResource, '/api/v1.0/documentocontable/<int:documento_id>', endpoint='documentoscontables_resource')