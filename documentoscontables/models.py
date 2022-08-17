from application import db, BaseModelMixin

class DocumentosContables(db.Model, BaseModelMixin):

    id = db.Column(db.Integer(), primary_key=True)
    fecha = db.Column(db.Date(),default=0)
    descripcion = db.Column(db.String(150))
    consecutivo= db.Column(db.Integer())
    prefijo = db.Column(db.String(5))
    tipodocumento = db.Column(db.String(15))
    plantilla = db.Column(db.String(15))
    
    def __init__(self, fecha, descripcion, consecutivo, prefijo, tipodocumento, plantilla):
        self.fecha = fecha
        self.descripcion = descripcion
        self.consecutivo = consecutivo
        self.prefijo = prefijo
        self.tipodocumento = tipodocumento
        self.plantilla = plantilla

    def __repr__(self):
        return f'Documento({self.descripcion})'

class RegistroDocumentosContables(db.Model, BaseModelMixin):
    id=db.Column(db.Integer(), primary_key=True)
    tipodocumento = db.Column(db.String(15))
    consecutivo = db.Column(db.Integer())
    fecha = db.Column(db.Date())
    proveedor_id = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))
    
    
        