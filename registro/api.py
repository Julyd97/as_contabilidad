import imp
from flask import request, Blueprint
from flask_restful import Api, Resource
from sqlalchemy import update

from registro.schemas import RegistroSchema
from registro.models import Registro
from cartera.models import Cartera
from cartera.schemas import CarteraSchema
from proveedores.models import Proveedor
from proveedores.schemas import ProveedorSchema
from documentoscontables.models import DocumentosContables
from documentoscontables.schemas import DocumentosContablesSchema

registro_app = Blueprint('registro_app', __name__)
registro_schema = RegistroSchema()
proveedor_schema = ProveedorSchema()
cartera_schema = CarteraSchema()
documentoscontables_schema = DocumentosContablesSchema()

api = Api(registro_app)

class RegistroListResource(Resource):
    def get(self):
        consecutivo = request.args.get('consecutivo')
        registros = Registro.query.order_by(Registro.consecutivo)
        if consecutivo !=None :
            registros = Registro.query.filter(Registro.consecutivo.like(str(consecutivo)+ '%')).order_by(Registro.consecutivo).all()
            if registros == []:
                result = registro_schema.dump(registros, many=True)
                return  result, 404 
        result = registro_schema.dump(registros, many=True)        
        return result, 201
    def post(self):
        data = request.get_json()
        registro_dict = registro_schema.load(data)
        consecutivo_registro = registro_dict['consecutivo']
        id_documentocontable = registro_dict['id_documentocontable']
        id_proveedor = registro_dict['id_proveedor']
        documentoscontables = documentoscontables_schema.dump(DocumentosContables.get_by_id(id_documentocontable))
        
        proveedores = proveedor_schema.dump(Proveedor.get_by_id(id_proveedor))
        print(data)
        registro_actual = Registro.query.filter_by(consecutivo = consecutivo_registro).first()
        if(registro_actual != None):
            return {'message':'La cuenta que intenta crear ya esta creada.','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        else:
            registro = Registro(
                                documentocontable = documentoscontables,
                                consecutivo = registro_dict['consecutivo'],
                                fecha = registro_dict['fecha'],
                                proveedor = proveedores,
                                observaciones = registro_dict['observaciones'],
                        )  
            registro.save()
            stmt=(update(DocumentosContables).where(DocumentosContables.id == id_documentocontable).values(consecutivo = consecutivo_registro))
            print(registro.id)
            print(stmt)
            print(id_documentocontable)
            print(consecutivo_registro  )
            resp = registro_schema.dump(registro)
            return {'message':'El registro se creo exitosamente','alerta':'alert-success','icon':'#check-circle-fill', 'id': registro.id}, 201
    
    
        
class RegistroResource(Resource):
    def get(self, registro_id):
        registro = Registro.get_by_id(registro_id)
        if registro is None:
            return {'message':'El registro no existe.','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}
        resp = registro_schema.dump(registro)
        return resp
    def put(self, registro_id):
        registro = Registro.get_by_id(registro_id)
        if registro is None:
            return{'message':'El registro no existe', 'alerta':'alert-danger','icon':'#exclamation-triangle-fill'}
        data = request.get_json()
        try:
            registro_dict = registro_schema.load(data)
            
            registro.consecutivo = registro_dict['consecutivo']
            registro.fecha = registro_dict['fecha']
            registro.id_proveedor = registro_dict['id_proveedor']
            registro.observaciones = registro_dict['observaciones']
            
            registro.save()
            resp = registro_schema.dump(registro)
            return {'message': 'El registro se ha modificado con exito', 'alerta':'alert-success','icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Ocurrio un error modificando el registro', 'alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 400
    def  delete(self, registro_id):
        registro = Registro.get_by_id(registro_id)
        if registro is None:
            return {'message': 'La cuenta que intenta eliminar no existe', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404
        try:
            registro.delete()
            return {'message': 'La cuenta se elimino con exito', 'alerta':'alert-success', 'icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Un error ocurrio un error eliminando la cuenta seleccionada', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404

api.add_resource(RegistroListResource, '/api/v1.0/registros/', endpoint='registro_list_resource')
api.add_resource(RegistroResource, '/api/v1.0/registro/<int:registro_id>', endpoint='registro_resource')

from registro.schemas import AsientoSchema
from registro.models import Asiento

asiento_schema = AsientoSchema()

class AsientoListResource(Resource):
    def get(self):
        id_registro = request.args.get('id_registro')
        asientos = Asiento.query.order_by(Asiento.id_registro)
        if id_registro !=None :
            asientos = Asiento.query.filter(Asiento.id_registro.like(str(id_registro))).order_by(Asiento.id_registro).all()
            if asientos == []:
                result = asiento_schema.dump(asientos, many=True)
                return  result, 404 
        result = asiento_schema.dump(asientos, many=True)        
        return result, 201
    def post(self):
        data = request.get_json()
        
        for asientodata in data:
            asiento_dict = asiento_schema.load(asientodata)
            id_registro = asiento_dict['id_registro']
            id_cuenta = asiento_dict['id_cuenta']
            id_proveedor = asiento_dict['id_proveedor']
            registros = registro_schema.dump(Registro.get_by_id(id_registro))
            cuentas = cartera_schema.dump(Cartera.get_by_id(id_cuenta))
            proveedores = proveedor_schema.dump(Proveedor.get_by_id(id_proveedor))

            asiento = Asiento(
                                registro = registros,
                                cuenta = cuentas,
                                descripcion = asiento_dict['descripcion'],
                                proveedor = proveedores,
                                debitocredito = asiento_dict['debitocredito'],
                                valorbase = asiento_dict['valorbase'],
                                porcentaje = asiento_dict['porcentaje'],
                                valortotal = asiento_dict['valortotal'],
                                id_formapago = asiento_dict['id_formapago'],
                                id_centrocosto = asiento_dict['id_centrocosto']
                        )  
            asiento.save()
            return {'message':'El asiento se creo exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
    
    
        
class AsientoResource(Resource):
    def get(self, asiento_id):
        asiento = Asiento.get_by_id(asiento_id)
        if asiento is None:
            return {'message':'El asiento no existe.','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}
        resp = asiento_schema.dump(asiento)
        return resp
    def put(self, asiento_id):
        asiento = Asiento.get_by_id(asiento_id)
        if asiento is None:
            return{'message':'El asiento no existe', 'alerta':'alert-danger','icon':'#exclamation-triangle-fill'}
        data = request.get_json()
        try:
            asiento_dict = asiento_schema.load(data)
            
            asiento.id_registro = asiento_dict['id_registro']
            asiento.id_cuenta = asiento_dict['id_cuenta']
            asiento.descripcion = asiento_dict['descripcion']
            asiento.id_proveedor = asiento_dict['id_proveedor']
            asiento.debitocredito = asiento_dict['debitocredito']
            asiento.valorbase = asiento_dict['valorbase']
            asiento.porcentaje = asiento_dict['porcentaje']
            asiento.valortotal = asiento_dict['valortotal']
            asiento.id_formapago = asiento_dict['id_formapago']
            asiento.id_centrocosto = asiento_dict['id_centrocosto']
            
            asiento.save()
            resp = asiento_schema.dump(asiento)
            return {'message': 'El asiento se ha modificado con exito', 'alerta':'alert-success','icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Ocurrio un error modificando el asiento', 'alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 400
    def  delete(self, asiento_id):
        asiento = Asiento.get_by_id(asiento_id)
        if asiento is None:
            return {'message': 'El asiento que intenta eliminar no existe', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404
        try:
            asiento.delete()
            return {'message': 'El asiento se elimino con exito', 'alerta':'alert-success', 'icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Un error ocurrio un error eliminando el asiento seleccionada', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404

api.add_resource(AsientoListResource, '/api/v1.0/asientos/', endpoint='asiento_list_resource')
api.add_resource(AsientoResource, '/api/v1.0/asiento/<int:asiento_id>', endpoint='asiento_resource')