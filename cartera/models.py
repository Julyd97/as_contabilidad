from application import db, BaseModelMixin

class Cartera(db.Model, BaseModelMixin):

    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer(), nullable = True)
    nivel = db.Column(db.String(2))
    serial = db.Column(db.String(20))
    descripcion = db.Column(db.String(150))
    cartera = db.Column(db.Boolean())
    tercero = db.Column(db.Boolean())
    proveedor = db.Column(db.Boolean())
    centroCosto = db.Column(db.Boolean())
    naturaleza = db.Column(db.Boolean())
    tipo = db.Column(db.String(5))

    def __init__(self, parent_id, nivel, serial, descripcion, cartera, tercero, proveedor, centroCosto, naturaleza, tipo):
        self.parent_id = parent_id
        self.nivel = nivel
        self.serial = serial
        self.descripcion = descripcion
        self.cartera = cartera
        self.tercero = tercero
        self.proveedor = proveedor
        self.centroCosto = centroCosto
        self.naturaleza = naturaleza
        self.tipo = tipo
    
    def __repr__(self):
        return self.serial