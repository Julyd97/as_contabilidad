from marshmallow import fields
from application import ma

class DocumentosContablesSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    fecha = fields.Date()
    descripcion = fields.String()
    consecutivo = fields.Integer()
    prefijo = fields.String()
    tipodocumento = fields.String()
    plantilla = fields.String()