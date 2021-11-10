from marshmallow import fields
from application import ma

class ProveedorSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    tipoDocumento = fields.String()
    numDocumento = fields.Integer()
    pais = fields.String()
    departamento = fields.String()
    municipio = fields.String()
    primerNombre = fields.String()
    segundoNombre = fields.String()
    primerApellido = fields.String()
    segundoApellido = fields.String()
    direccion = fields.String()
    telefono = fields.Integer()
    correo = fields.String()
    codigoPostal = fields.Integer()
