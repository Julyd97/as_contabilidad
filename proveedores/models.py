from application import db, BaseModelMixin

class Proveedor(db.Model, BaseModelMixin):

    id = db.Column(db.Integer(), primary_key=True)
    tipoDocumento = db.Column(db.String(5))
    numDocumento = db.Column(db.BigInteger())
    pais = db.Column(db.String(40))
    departamento = db.Column(db.String(40))
    municipio = db.Column(db.String(40))
    primerNombre = db.Column(db.String(15))
    segundoNombre = db.Column(db.String(15))
    primerApellido = db.Column(db.String(15))
    segundoApellido = db.Column(db.String(15))
    direccion = db.Column(db.String(130))
    telefono = db.Column(db.BigInteger())
    correo = db.Column(db.String(120))
    codigoPostal = db.Column(db.Integer())  
    
    def __init__(self, tipoDocumento, numDocumento, pais, departamento, municipio, primerNombre, segundoNombre, primerApellido, segundoApellido, direccion, telefono, correo, codigoPostal):
        self.tipoDocumento = tipoDocumento
        self.numDocumento = numDocumento
        self.pais = pais
        self.departamento = departamento
        self.municipio = municipio
        self.primerNombre = primerNombre
        self.segundoNombre = segundoNombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.codigoPostal = codigoPostal

    def __repr__(self):
        return f'Proveedor({self.numDocumento})'
        