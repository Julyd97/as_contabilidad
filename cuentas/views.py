from flask import Blueprint, session, render_template, request,flash, redirect,url_for

from application import db
from cuentas.models import Clase, Grupo
from cuentas.forms import ClaseForm, GrupoForm
from user.models import User

cuenta_app = Blueprint('cuenta_app', __name__)

@cuenta_app.route('/')
def index():
    return render_template('cuentas/index.html')

@cuenta_app.route('/clase', methods=['GET', 'POST'])
def clase():
    form = ClaseForm()

    if form.validate_on_submit():
        serial = form.serial.data
        descripcion = form.descripcion.data.strip()
        if 'Cartera' in form.example.data:
                cartera=True
        else:
                cartera=False
        if 'Tercero' in form.example.data:
                tercero=True
        else:
                tercero=False
        if 'Proveedor' in form.example.data:
                proveedor=True
        else:
                proveedor=False
        if 'CentroCosto' in form.example.data:
                centroCosto=True
        else:
                centroCosto=False
        
        clase = Clase(
            serial=serial,
            descripcion = descripcion,
            cartera=cartera,
            tercero=tercero,
            proveedor=proveedor,
            centroCosto=centroCosto
        )
        db.session.add(clase)
        db.session.commit()
    return render_template('cuentas/clase.html', form=form)

@cuenta_app.route('/grupo', methods=['GET', 'POST'])
def grupo():
    form = GrupoForm()

    if form.validate_on_submit():
        serial_cuenta=form.serial_cuenta.data
        clase = Clase.query.filter_by(serial=serial_cuenta).first()
        if clase is not None:
            serial = form.serial.data
            descripcion = form.descripcion.data.strip()
            if 'Cartera' in form.example.data:
                    cartera=True
            else:
                    cartera=False
            if 'Tercero' in form.example.data:
                    tercero=True
            else:
                    tercero=False
            if 'Proveedor' in form.example.data:
                    proveedor=True
            else:
                    proveedor=False
            if 'CentroCosto' in form.example.data:
                    centroCosto=True
            else:
                    centroCosto=False
            
            grupo = Grupo(
                clase = clase,
                serial=serial,
                descripcion = descripcion,
                cartera=cartera,
                tercero=tercero,
                proveedor=proveedor,
                centroCosto=centroCosto
            )
            db.session.add(grupo)
            db.session.commit()
        else:
            flash('La clase a la que intenta agregar no se encuentra creada.')
    return render_template('cuentas/grupo.html', form=form)
