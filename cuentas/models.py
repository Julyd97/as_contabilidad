from application import db

class Clase(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    serial = db.Column(db.Integer())
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())    
    
    def __init__(self, serial, descripcion, cartera, tercero, proveedor, centroCosto):
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto

    def __repr__(self):
        return '<Post %r>' % self.serial

class Grupo(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    clase_id = db.Column(db.Integer, db.ForeignKey('clase.id'))
    serial = db.Column(db.Integer())
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())

    clase = db.relationship('Clase',
        backref=db.backref('grupos'))
        

    def __init__(self, clase, serial, descripcion, cartera, tercero, proveedor, centroCosto):
        self.clase_id = clase.id
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto

    def __repr__(self):
        return self.serial
    

class Cuenta(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    serial = db.Column(db.Integer())
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())

    grupo = db.relationship('Grupo',
        backref=db.backref('cuentas'))
        

    def __init__(self, grupo, serial, descripcion, cartera, tercero, proveedor, centroCosto):
        self.grupo_id = grupo.id
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto

    def __repr__(self):
        return self.serial


class Subcuenta(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.id'))
    serial = db.Column(db.Integer())
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())

    cuenta = db.relationship('Cuenta',
        backref=db.backref('subcuentas'))
        

    def __init__(self, cuenta, serial, descripcion, cartera, tercero, proveedor, centroCosto):
        self.cuenta_id = cuenta.id
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto

    def __repr__(self):
        return self.serial

class Auxiliar(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    subcuenta_id = db.Column(db.Integer, db.ForeignKey('subcuenta.id'))
    serial = db.Column(db.Integer())
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())

    subcuenta = db.relationship('Subcuenta',
        backref=db.backref('auxiliares'))
        

    def __init__(self, subcuenta, serial, descripcion, cartera, tercero, proveedor, centroCosto):
        self.subcuenta_id = subcuenta.id
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto

    def __repr__(self):
        return self.serial

class Subauxiliar(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    auxiliar_id = db.Column(db.Integer, db.ForeignKey('auxiliar.id'))
    serial = db.Column(db.Integer())
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())

    auxiliar = db.relationship('Auxiliar',
        backref=db.backref('subauxiliares'))
        

    def __init__(self, auxiliar, serial, descripcion, cartera, tercero, proveedor, centroCosto):
        self.auxiliar_id = auxiliar.id
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto

    def __repr__(self):
        return self.serial

