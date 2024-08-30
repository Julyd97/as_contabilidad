from marshmallow import fields
from application import ma
from proveedores.models import Proveedor
from marshmallow_sqlalchemy import field_for, auto_field
from marshmallow_sqlalchemy.fields import Nested

# class ProveedorSchema(ma.Schema):
#     id = fields.Integer(dump_only = True)
#     tipoDocumento = fields.String()
#     numDocumento = fields.Integer()
#     pais = fields.String()
#     departamento = fields.String()
#     municipio = fields.String()
#     primerNombre = fields.String()
#     segundoNombre = fields.String()
#     primerApellido = fields.String()
#     segundoApellido = fields.String()
#     direccion = fields.String()
#     telefono = fields.Integer(allow_none = True)
#     correo = fields.String()
#     codigoPostal = fields.Integer(allow_none = True)

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
    id = field_for( Proveedor, 'id', dump_only=True)

    class Meta:
        model = Proveedor
        load_instance = True