from marshmallow import fields
from application import ma

class CarteraSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    parent_id = fields.Integer(allow_none = True)
    nivel = fields.String()
    serial = fields.String()
    descripcion = fields.String()
    cartera = fields.Boolean()
    tercero = fields.Boolean()
    proveedor = fields.Boolean()
    centroCosto = fields.Boolean()