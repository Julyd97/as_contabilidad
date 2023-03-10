from dataclasses import field
from marshmallow import fields
from application import ma

class RegistroSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    id_documentocontable = fields.Integer()
    consecutivo = fields.Integer()
    fecha = fields.Date()
    id_proveedor = fields.Integer(required=True)
    observaciones = fields.String()

class AsientoSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    id_registro = fields.Integer()
    id_cuenta = fields.Integer()
    descripcion  = fields.String()
    id_proveedor = fields.Integer()
    debitocredito = fields.Boolean()
    valorbase = fields.Float()
    porcentaje = fields.Float()
    valortotal = fields.Float()
    id_formapago = fields.Integer(allow_none = True)
    id_centrocosto = fields.Integer(allow_none = True)

