from application import db, BaseModelMixin

class DocumentosContables(db.Model, BaseModelMixin):

    id = db.Column(db.Integer(), primary_key=True)
    fecha = db.Column(db.Date())
    descripcion = db.Column(db.String(150))
    consecutivo= db.Column(db.Integer())
    prefijo = db.Column(db.String(5))
    
    def __init__(self, fecha, descripcion, consecutivo, prefijo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.consecutivo = consecutivo
        self.prefijo = prefijo

    def __repr__(self):
        return f'Documento({self.descripcion})'
        