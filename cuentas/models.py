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