from flask import Blueprint, session, render_template, request,flash, redirect,url_for
from flask.helpers import get_flashed_messages

from application import db
from cuentas.models import Clase, Grupo, Cuenta, Subcuenta, Auxiliar, Subauxiliar
from cuentas.forms import ClaseForm, GrupoForm,CuentasForm, ModificarForm
from user.models import User
from user.views import login_required
import random

cuenta_app = Blueprint('cuenta_app', __name__)

@cuenta_app.route('/plan', methods=['GET','POST','DELETE'])
@login_required
def index():
        # Cargar los datos en tabla de Cartera
    get_flashed_messages()
    clases = Clase.query.with_entities(Clase.serial, Clase.descripcion, Clase.cartera, Clase.tercero, Clase.proveedor, Clase.centroCosto)
    grupo = Grupo.query.with_entities(Grupo.serial, Grupo.descripcion, Grupo.cartera, Grupo.tercero, Grupo.proveedor, Grupo.centroCosto)
    cuenta = Cuenta.query.with_entities(Cuenta.serial, Cuenta.descripcion, Cuenta.cartera, Cuenta.tercero, Cuenta.proveedor, Cuenta.centroCosto)
    subcuenta = Subcuenta.query.with_entities(Subcuenta.serial, Subcuenta.descripcion, Subcuenta.cartera, Subcuenta.tercero, Subcuenta.proveedor, Subcuenta.centroCosto)
    auxiliar = Auxiliar.query.with_entities(Auxiliar.serial, Auxiliar.descripcion, Auxiliar.cartera, Auxiliar.tercero, Auxiliar.proveedor,Auxiliar.centroCosto)
    subauxiliar = Subauxiliar.query.with_entities(Subauxiliar.serial, Subauxiliar.descripcion, Subauxiliar.cartera, Subauxiliar.tercero, Subauxiliar.proveedor, Subauxiliar.centroCosto)
    x = clases.union(grupo, cuenta, subcuenta, auxiliar, subauxiliar).order_by(Clase.descripcion)
    clase = list(x)
    clase1=[]
    for i in clase:
            clase1.append([str(i[0]), i[1], i[2], i[3],i[4], i[5]])
    clase1 = sorted(clase1, key=lambda clase : clase[0]) 
    modificar_form = ModificarForm()
    form=CuentasForm()

    print("retornando template")
    return render_template('home/index.html', clase=clase1,  cache_id=random.randrange(10000), modificar_form = modificar_form, form=form )

@cuenta_app.route('/crearcuenta', methods=['GET','POST','DELETE'])
def crearCuenta():
        # Crear nuevas cuentas en cartera
    form=CuentasForm()
    if form.submitCrear.data:
        print(form.submitCrear.data)
        serial = form.serial.data
        descripcion = form.descripcion.data
        example = form.example.data    
        if form.validate():
                objeto = adiciondeobjetos(serial, descripcion, example)
                db.session.add(objeto)
                db.session.commit()
                flash('El objeto se agrego con exito a la base de datos')
    return redirect('/plan')

@cuenta_app.route('/modificaryeliminarCuenta', methods=['GET', 'POST', 'DELETE'])
def modificaryeliminarCuenta():
        # Eliminar o modificar cuentas en cartera
    modificar_form = ModificarForm()
    if modificar_form.validate():
        serial = modificar_form.serial.data
        print(serial)
        descripcion = modificar_form.descripcion.data
        cartera = modificar_form.cartera.data
        tercero = modificar_form.tercero.data
        proveedor = modificar_form.proveedor.data
        costo = modificar_form.costo.data
        print(descripcion)
        if modificar_form.submitGuardar.data:
                objeto = modificarobjeto(serial)
                objeto.descripcion = descripcion
                objeto.cartera = cartera
                objeto.tercero = tercero
                objeto.proveedor = proveedor
                objeto.centroCosto = costo
                db.session.commit()
                flash('Se modifico correctamente.')
        elif modificar_form.submitBorrar.data:
                serial = modificar_form.serial.data
                objeto = modificarobjeto(serial)
                try:
                        db.session.delete(objeto)
                        db.session.commit()
                        flash('Se elimino correctamente.')
                except:
                        pass
                        flash('El objeto no se pudo eliminar de forma correcta.')
          
        return redirect('/plan')

def adiciondeobjetos(serial, descripcion, example):
        # Adición de objetos en Cartera
        serial = list(map(int,str(serial)))
        serial_digits = [str(digit) for digit in serial]
        serial_clase  = int("".join(serial_digits[0]))
        serial_grupo = int("".join(serial_digits[0:2]))
        serial_cuenta = int("".join(serial_digits[0:4]))
        serial_subcuenta = int("".join(serial_digits[0:6]))
        serial_auxiliar = int("".join(serial_digits[0:8]))
        serial_subauxiliar = int("".join(serial_digits))
        if 'Cartera' in example:
                cartera=True
        else:
                cartera=False
        if 'Tercero' in example:
                tercero=True
        else:
                tercero=False
        if 'Proveedor' in example:
                proveedor=True
        else:
                proveedor=False
        if 'CentroCosto' in example:
                centroCosto=True
        else:
                centroCosto=False
        
        if len(serial) == 1:
                
                objeto = Clase(
                        serial = serial_clase,
                        descripcion = descripcion,
                        cartera=cartera,
                        tercero=tercero,
                        proveedor=proveedor,
                        centroCosto=centroCosto
                )
        elif len(serial) == 2:
                clase = Clase.query.filter_by(serial = serial_clase).first()
                objeto = Grupo(
                        clase = clase,
                        serial = serial_grupo,
                        descripcion = descripcion,
                        cartera=cartera,
                        tercero=tercero,
                        proveedor=proveedor,
                        centroCosto=centroCosto
                )
        elif len(serial) == 4:
                grupo = Grupo.query.filter_by(serial = serial_grupo).first()
                objeto = Cuenta(
                        grupo = grupo,
                        serial = serial_cuenta,
                        descripcion = descripcion,
                        cartera=cartera,
                        tercero=tercero,
                        proveedor=proveedor,
                        centroCosto=centroCosto
                )
        elif len(serial) == 6:
                cuenta = Cuenta.query.filter_by(serial = serial_cuenta).first()
                objeto = Subcuenta(
                        cuenta = cuenta,
                        serial = serial_subcuenta,
                        descripcion = descripcion,
                        cartera=cartera,
                        tercero=tercero,
                        proveedor=proveedor,
                        centroCosto=centroCosto
                )
        elif len(serial) == 8:
                subcuenta = Subcuenta.query.filter_by(serial = serial_subcuenta).first()
                objeto = Auxiliar(
                        subcuenta = subcuenta,
                        serial = serial_auxiliar,
                        descripcion = descripcion,
                        cartera=cartera,
                        tercero=tercero,
                        proveedor=proveedor,
                        centroCosto=centroCosto
                )
        elif len(serial) == 10:
                auxiliar = Auxiliar.query.filter_by(serial = serial_auxiliar).first()
                objeto = Subauxiliar(
                        auxiliar = auxiliar,
                        serial = serial_subauxiliar,
                        descripcion = descripcion,
                        cartera=cartera,
                        tercero=tercero,
                        proveedor=proveedor,
                        centroCosto=centroCosto
                )
        
        return objeto

def modificarobjeto(serial):
        # BUscar el objeto con el serial para modificar o eliminarlo
        if len(str(serial)) == 1:
                objeto = Clase.query.filter_by(serial = serial).first()
        elif len(str(serial)) == 2:
                objeto = Grupo.query.filter_by(serial = serial).first()
        elif len(str(serial)) == 4:
                objeto = Cuenta.query.filter_by(serial = serial).first()
        elif len(str(serial)) == 6:
                objeto = Subcuenta.query.filter_by(serial = serial).first()
        elif len(str(serial)) == 8:
                objeto = Auxiliar.query.filter_by(serial = serial).first()
        elif len(str(serial)) == 10:
                objeto = Subauxiliar.query.filter_by(serial = serial).first()

        return objeto
        
        