from email import message
from flask import request, Blueprint
from flask_restful import Api, Resource
from sqlalchemy.orm import aliased

from cartera.schemas import CarteraSchema
from cartera.models import Cartera
from resources.errors import errors

cartera_app = Blueprint('cartera_app', __name__)
cartera_schema = CarteraSchema()

api = Api(cartera_app, errors=errors)

class CarteraListResource(Resource):
    def get(self):
        num_serial = request.args.get('codigo')
        txt_descripcion = request.args.get('descripcion')
        filter_childs = request.args.get('childs')
        cuentas = Cartera.query.order_by(Cartera.serial)
        print(filter_childs)
        if filter_childs !=None :
            cuentas1 = Cartera.query.with_entities(Cartera.parent_id).filter(Cartera.parent_id.is_not(None))
            cuentas =  Cartera.query.filter(Cartera.id.not_in(cuentas1)).order_by(Cartera.serial)
            print(cuentas)
        if num_serial == None and txt_descripcion == None and filter_childs == None:
            cuentas = Cartera.query.order_by(Cartera.serial)
        elif num_serial != None and txt_descripcion == None:
            cuentas = cuentas.filter(Cartera.serial.like(str(num_serial) + '%')).order_by(Cartera.serial).all()
        elif num_serial == None and txt_descripcion != None: 
            cuentas = cuentas.filter(Cartera.descripcion.like(str(txt_descripcion) + '%')).order_by(Cartera.descripcion).all()
            if cuentas == []:
                result = cartera_schema.dump(cuentas, many=True)
                return  result, 404 
        result = cartera_schema.dump(cuentas, many=True)        
        return result, 201
    def post(self):
        data = request.get_json()
        cuenta_dict = cartera_schema.load(data)
        serial_cuenta = cuenta_dict['serial']
        cuenta_actual = Cartera.query.filter_by(serial=serial_cuenta).first()
        if(cuenta_actual != None):
            return {'message':'La cuenta que intenta crear ya esta creada.','alerta': 'alert-danger','icon':'#exclamation-triangle-fill'}, 404
        else:
            if(len(serial_cuenta) > 1):
                a = verificar_parent(serial_cuenta)
                if(a[0] == True):
                    parent_id1 = a[1]
                    nivel1 = a[2]
                else:
                    return {'message':'La cuenta que intenta crear no tiene una cuenta superior','alerta':'alert-danger','icon':'#exclamation-triangle-fill'},404
            else:
                parent_id1 = None
                nivel1 = '0'
            cuenta = Cartera(parent_id = parent_id1,
                                nivel = nivel1,
                                serial = cuenta_dict['serial'],
                                descripcion = cuenta_dict['descripcion'],
                                cartera = cuenta_dict['cartera'],
                                tercero = cuenta_dict['tercero'],
                                proveedor = cuenta_dict['proveedor'],
                                centroCosto = cuenta_dict['centroCosto']
                        )  
            cuenta.save()
            resp = cartera_schema.dump(cuenta)
            return {'message':'La cuenta se creo exitosamente','alerta':'alert-success','icon':'#check-circle-fill'}, 201
    
    
        
class CarteraResource(Resource):
    def get(self, cuenta_id):
        cuenta = Cartera.get_by_id(cuenta_id)
        if cuenta is None:
            return {'message':'El proveedor no existe.','alerta':'alert-danger','icon':'#exclamation-triangle-fill'}
        resp = cartera_schema.dump(cuenta)
        return resp
    def put(self, cuenta_id):
        cuenta = Cartera.get_by_id(cuenta_id)
        if cuenta is None:
            return{'message':'La cuenta no existe', 'alerta':'alert-danger','icon':'#exclamation-triangle-fill'}
        data = request.get_json()
        try:
            cuenta_dict = cartera_schema.load(data)
            
            cuenta.descripcion = cuenta_dict['descripcion']
            cuenta.cartera = cuenta_dict['cartera']
            cuenta.tercero = cuenta_dict['tercero']
            cuenta.proveedor = cuenta_dict['proveedor']
            cuenta.centroCosto = cuenta_dict['centroCosto']
            
            cuenta.save()
            resp = cartera_schema.dump(cuenta)
            return {'message': 'La cuenta se ha modificado con exito', 'alerta':'alert-success','icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Ocurrio un error modificando la cuenta', 'alerta':'alert-danger','icon':'#exclamation-triangle-fill'}, 400
    def  delete(self, cuenta_id):
        cuenta = Cartera.get_by_id(cuenta_id)
        cuenta_child = Cartera.query.filter(Cartera.parent_id.like(cuenta_id)).all()
        if cuenta is None:
            return {'message': 'La cuenta que intenta eliminar no existe', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404
        elif(cuenta_child != []):
            return {'message': 'La cuenta que intenta posee cuentas inferiores y no puede ser eliminada', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 400
        try:
            cuenta.delete()
            return {'message': 'La cuenta se elimino con exito', 'alerta':'alert-success', 'icon':'#check-circle-fill'}, 201
        except:
            return {'message': 'Un error ocurrio un error eliminando la cuenta seleccionada', 'alerta':'alert-danger', 'icon':'#exclamation-triangle-fill'}, 404

api.add_resource(CarteraListResource, '/api/v1.0/carteras/', endpoint='cartera_list_resource')
api.add_resource(CarteraResource, '/api/v1.0/cartera/<int:cuenta_id>', endpoint='cartera_resource')

def verificar_parent(serial_hijo):
    longitud_serial_hijo = len(serial_hijo)
    if(longitud_serial_hijo > 2 and longitud_serial_hijo % 2 ==0):
        serial_parent = serial_hijo[0:(longitud_serial_hijo-2)]
    elif(longitud_serial_hijo == 2):
        serial_parent = serial_hijo[0:1]
    else:
        return [False]
    cuenta_parent = Cartera.query.filter_by(serial=serial_parent).first()
    if cuenta_parent ==None:
        return [False]
    else:
        nivel_cuenta = str(int(cuenta_parent.nivel)+1)
        parent_id = str(cuenta_parent.id)

        return [True, parent_id, nivel_cuenta]