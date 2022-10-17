import imp
from flask import request, Blueprint
from flask_restful import Api, Resource
from sqlalchemy import update
from application import db
from user.views import login_required
from registro.schemas import RegistroSchema
from registro.models import Registro
from registro.schemas import AsientoSchema
from registro.models import Asiento
from cartera.models import Cartera
from cartera.schemas import CarteraSchema
from proveedores.models import Proveedor
from proveedores.schemas import ProveedorSchema
from documentoscontables.models import DocumentosContables
from documentoscontables.schemas import DocumentosContablesSchema

registro_app = Blueprint('registro_app', __name__)
registro_schema = RegistroSchema()
asiento_schema = AsientoSchema()
proveedor_schema = ProveedorSchema()
cartera_schema = CarteraSchema()
documentoscontables_schema = DocumentosContablesSchema()

api = Api(registro_app)

class RegistroListResource(Resource):
    @login_required
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
        data_asientos = data['asiento']
        data.pop('asiento')
        data_registro = data
        try:
            registro_dict = registro_schema.load(data_registro)
        except:
            return {'message':'La creacion del registro no fue satisfactoria.','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        consecutivo_registro = registro_dict['consecutivo']
        fecha_registro = registro_dict['fecha']
        id_documentocontable = registro_dict['id_documentocontable']
        id_proveedor = registro_dict['id_proveedor']
        documentoscontables = documentoscontables_schema.dump(DocumentosContables.get_by_id(id_documentocontable))
        
        proveedores = proveedor_schema.dump(Proveedor.get_by_id(id_proveedor))
        
        registro_actual = Registro.query.filter_by(id_documentocontable = id_documentocontable, consecutivo = consecutivo_registro).first()
        if(registro_actual != None):
            return {'message':'La cuenta que intenta crear ya esta creada.','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        else:
            try:   
                registro = Registro(
                                    documentocontable = documentoscontables,
                                    consecutivo = registro_dict['consecutivo'],
                                    fecha = registro_dict['fecha'],
                                    proveedor = proveedores,
                                    observaciones = registro_dict['observaciones'],
                            )  
                doc=DocumentosContables.get_by_id(id_documentocontable)
                doc.consecutivo = consecutivo_registro
                doc.fecha = fecha_registro
                
                
                db.session.add(registro)
                db.session.add(doc)
                db.session.flush()
                valordebito = 0
                valorcredito = 0
                for asientodata in data_asientos:
                    try:
                        asiento_dict = asiento_schema.load(asientodata)
                    except:
                        {'message':'Fallo la creación de los asientos.','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
                    
                    id_registro = registro.id
                    id_cuenta = asiento_dict['id_cuenta']
                    id_proveedor = asiento_dict['id_proveedor']
                    debitoycredito = asiento_dict['debitocredito']
                    valortotal = asiento_dict['valortotal']
                    registros = registro_schema.dump(Registro.get_by_id(id_registro))
                    cuentas = cartera_schema.dump(Cartera.get_by_id(id_cuenta))
                    proveedores = proveedor_schema.dump(Proveedor.get_by_id(id_proveedor))

                    if debitoycredito == True:
                        valordebito += valortotal
                    elif debitoycredito == False:
                        valorcredito += valortotal


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
                    db.session.add(asiento)
                    db.session.flush()

                if valorcredito != valordebito:
                    db.session.rollback()
                    return {'message':'Los valores debitos y creditos no concuerdan','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
                
                resp = registro_schema.dump(registro)
                db.session.commit()
                
                return {'message':'El registro se creo exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
            except:
                # stmt=(update(DocumentosContables).where(DocumentosContables.id == id_documentocontable).values(consecutivo = consecutivo_registro))
                # print(registro.id)
                # print(stmt)
                print('ha fallado')
                db.session.rollback()
                return {'message':'Fallo la creacion del registro','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
    
    
        
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