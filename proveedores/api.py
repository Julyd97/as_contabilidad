from flask import request, Blueprint
from flask_restful import Api, Resource

from proveedores.schemas import ProveedorSchema
from proveedores.models import Proveedor

proveedores_app = Blueprint('proveedores_app', __name__)
proveedor_schema = ProveedorSchema()

api = Api(proveedores_app)

class ProveedorListResource(Resource):
    def get(self):
        proveedores = Proveedor.get_all()
        result = proveedor_schema.dump(proveedores, many=True)
        return result
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
            raise ObjectNotFound('El proveedor no existe')
        resp = proveedor_schema.dump(proveedor)
        return resp

api.add_resource(ProveedorListResource, '/api/v1.0/proveedores/', endpoint='proveedores_list_resource')
api.add_resource(ProveedorResource, '/api/v1.0/proveedor/<int:proveedor_id>', endpoint='proveedor_resource')