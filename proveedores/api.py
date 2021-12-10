from flask import request, Blueprint
from flask_restful import Api, Resource

from proveedores.schemas import ProveedorSchema
from proveedores.models import Proveedor

proveedores_app = Blueprint('proveedores_app', __name__)
proveedor_schema = ProveedorSchema()

api = Api(proveedores_app)

class ProveedorListResource(Resource):
    def get(self, num_cedula=None):
        if num_cedula == None:
            proveedores = Proveedor.get_all()
            result = proveedor_schema.dump(proveedores, many=True)
        else:  
            proveedores = Proveedor.query.filter(Proveedor.numDocumento.like(str(num_cedula) + '%')).all()
            if proveedores == []:
                return  {'message': 'Ocurrio un error buscando con el numero dado'}, 404
            else:         
                result = proveedor_schema.dump(proveedores, many=True)
        print(proveedores)
        return result, 201
    def post(self):
        data = request.get_json()
        proveedor_dict = proveedor_schema.load(data)
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
        return resp, 201
    
    
        
class ProveedorResource(Resource):
    def get(self, proveedor_id):
        proveedor = Proveedor.get_by_id(proveedor_id)
        if proveedor is None:
            raise ('El proveedor no existe')
        resp = proveedor_schema.dump(proveedor)
        return resp
    def put(self, proveedor_id):
        proveedor = Proveedor.get_by_id(proveedor_id)
        if proveedor is None:
            raise ('El proveedor no existe')
        data = request.get_json()
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
            return resp, 201
        except:
            return {'message': 'Ocurrio un error modificando el proveedor'}, 400
    def  delete(self, proveedor_id):
        proveedor = Proveedor.get_by_id(proveedor_id)
        if proveedor is None:
            raise ('El proveedor no existe')
        try:
            proveedor.delete()
            return 201
        except:
            return {'message': 'Un error ocurrio un error eliminando el proveedor'}, 400

api.add_resource(ProveedorListResource, '/api/v1.0/proveedores/', '/api/v1.0/proveedores/<num_cedula>', endpoint='proveedores_list_resource')
api.add_resource(ProveedorResource, '/api/v1.0/proveedor/<int:proveedor_id>', endpoint='proveedor_resource')