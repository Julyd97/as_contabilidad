from cgi import print_directory
from flask import request, Blueprint
from flask_restful import Api, Resource

from proveedores.schemas import ProveedorSchema
from proveedores.models import Proveedor

proveedores_app = Blueprint('proveedores_app', __name__)
proveedor_schema = ProveedorSchema()

api = Api(proveedores_app)

class ProveedorListResource(Resource):
    def get(self):
        num_cedula=request.args.get('numero')
        nom_proveedor = request.args.get('nombre')
        if num_cedula == None and nom_proveedor == None:
            proveedores = Proveedor.query.order_by(Proveedor.numDocumento)
            result = proveedor_schema.dump(proveedores, many=True)    
        elif num_cedula != None and nom_proveedor== None:
            proveedores = Proveedor.query.filter(Proveedor.numDocumento.like(str(num_cedula) + '%')).order_by(Proveedor.numDocumento).all()
            result = proveedor_schema.dump(proveedores, many=True)
            if proveedores == []:
                return  result, 404
        else:  
            proveedores = Proveedor.query.filter(Proveedor.primerNombre.like(str(nom_proveedor) + '%')).order_by(Proveedor.numDocumento).all()
            result = proveedor_schema.dump(proveedores, many=True)
            if proveedores == []:
                return  result, 404
        return result, 201
    def post(self):
        data = request.get_json()
        proveedor_dict = proveedor_schema.load(data)
        num_documento = proveedor_dict['numDocumento']
        proveedor_actual= Proveedor.query.filter_by(numDocumento = num_documento).first()
        if(proveedor_actual != None):
            return {'message': 'El proveedor que intenta crear ya esta creado.', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404
        else:
            proveedor = Proveedor(tipoDocumento = proveedor_dict['tipoDocumento'],
                                    numDocumento = proveedor_dict['numDocumento'],
                                    pais = proveedor_dict['pais'], departamento = proveedor_dict['departamento'],
                                    municipio = proveedor_dict['municipio'],
                                    primerNombre = proveedor_dict['primerNombre'],
                                    segundoNombre = proveedor_dict['segundoNombre'],
                                    primerApellido = proveedor_dict['primerApellido'],
                                    segundoApellido = proveedor_dict['segundoApellido'],
                                    direccion = proveedor_dict['direccion'],
                                    telefono = proveedor_dict['telefono'],
                                    correo = proveedor_dict['correo'],
                                    codigoPostal = proveedor_dict['codigoPostal']
            )  
            proveedor.save()
            resp = proveedor_schema.dump(proveedor)
            return {'message':'El proveedor se creo exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
    
    
        
class ProveedorResource(Resource):
    def get(self, proveedor_id):
        proveedor = Proveedor.get_by_id(proveedor_id)
        if proveedor is None:
            return {'message': 'El proveedor que esta buscando no existe', 'alerta':'alert-warning', 'icon':'#exclamation-triangle-fill'}, 404
        resp = proveedor_schema.dump(proveedor)
        return resp
    def put(self, proveedor_id):
        proveedor = Proveedor.get_by_id(proveedor_id)
        if proveedor is None:
            return {'message': 'El proveedor que esta modificando no existe', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404
        data = request.get_json()
        proveedor_dict = proveedor_schema.load(data)
        print(data)
        try:
            proveedor_dict = proveedor_schema.load(data)
            proveedor.tipoDocumento = proveedor_dict['tipoDocumento']
            proveedor.proveedornumDocumento = proveedor_dict['numDocumento']
            proveedor.pais = proveedor_dict['pais']
            proveedor.departamento = proveedor_dict['departamento']
            proveedor.municipio = proveedor_dict['municipio']
            proveedor.primerNombre = proveedor_dict['primerNombre']
            proveedor.segundoNombre = proveedor_dict['segundoNombre']
            proveedor.primerApellido = proveedor_dict['primerApellido']
            proveedor.segundoApellido = proveedor_dict['segundoApellido']
            proveedor.direccion = proveedor_dict['direccion']
            proveedor.telefono = proveedor_dict['telefono']
            proveedor.correo = proveedor_dict['correo']
            proveedor.codigoPostal = proveedor_dict['codigoPostal']
            
            proveedor.save()
            resp = proveedor_schema.dump(proveedor)
            return {'message':'El proveedor se modifico exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Ocurrio un error modificando el proveedor','alerta':'alert-warning', 'icon':'#exclamation-triangle-fill'}, 400
    def  delete(self, proveedor_id):
        proveedor = Proveedor.get_by_id(proveedor_id)
        if proveedor is None:
            return {'message': 'El proveedor que intenta eliminar no existe', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404
        try:
            proveedor.delete()
            return {'message': 'El proveedor se elimino exitosamente', 'alerta':'alert-success', 'icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Ocurrio un error eliminando el proveedor','alerta':'alert-warning', 'icon':'#exclamation-triangle-fill'}, 400

api.add_resource(ProveedorListResource, '/api/v1.0/proveedores/', endpoint='proveedores_list_resource')
api.add_resource(ProveedorResource, '/api/v1.0/proveedor/<int:proveedor_id>', endpoint='proveedor_resource')