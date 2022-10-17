from contextlib import nullcontext
from email.policy import default
from operator import truediv
from application import db, BaseModelMixin
from cartera.models import Cartera
from cuentas.models import Cuenta
from documentoscontables.models import DocumentosContables

class Registro(db.Model, BaseModelMixin):

    id = db.Column(db.Integer(), primary_key=True)
    id_documentocontable = db.Column(db.Integer, db.ForeignKey('documentos_contables.id'))
    consecutivo = db.Column(db.Integer())
    fecha = db.Column(db.Date())
    id_proveedor = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))
    observaciones = db.Column(db.String(150))  
    
    documentocontable = db.relationship('DocumentosContables',
        backref=db.backref('registros'))

    proveedor = db.relationship('Proveedor',
        backref=db.backref('registros'))
    
    def __init__(self, documentocontable, consecutivo, fecha, proveedor, observaciones):
        self.id_documentocontable = documentocontable['id']
        self.consecutivo = consecutivo
        self.fecha = fecha
        self.id_proveedor = proveedor['id']
        self.observaciones = observaciones

    def __repr__(self):
        return '<Registro' % self.id

class Asiento(db.Model, BaseModelMixin):

    id = db.Column(db.Integer(), primary_key=True)
    id_registro = db.Column(db.Integer, db.ForeignKey('registro.id'))
    id_cuenta = db.Column(db.Integer(), db.ForeignKey('cartera.id'))
    descripcion = db.Column(db.String(150))
    id_proveedor = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))
    debitocredito = db.Column(db.Boolean())
    valorbase = db.Column(db.Float())
    porcentaje = db.Column(db.Float())
    valortotal = db.Column(db.Float())
    id_formapago = db.Column(db.Integer(), nullable = True)
    id_centrocosto = db.Column(db.Integer(), nullable = True)

    registro = db.relationship('Registro',
        backref=db.backref('asientos'))

    Cartera = db.relationship('Cartera',
        backref=db.backref('asientos'))
    
    proveedor = db.relationship('Proveedor',
        backref=db.backref('asientos'))
        

    def __init__(self, registro, cuenta, descripcion, proveedor, debitocredito, valorbase, porcentaje, valortotal, id_formapago, id_centrocosto):
        self.id_registro = registro['id']
        self.id_cuenta = cuenta['id']
        self.descripcion = descripcion
        self.id_proveedor = proveedor['id']
        self.debitocredito =  debitocredito
        self.valorbase = valorbase
        self.porcentaje = porcentaje
        self.valortotal = valortotal
        self.id_formapago = id_formapago
        self.id_centrocosto = id_centrocosto

    def __repr__(self):
        return self.id
    