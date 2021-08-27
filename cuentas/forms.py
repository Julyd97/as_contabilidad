from flask_wtf import FlaskForm
from wtforms import validators,ValidationError, StringField, PasswordField, widgets, SelectMultipleField, IntegerField

from cuentas.models import Clase

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label = False)
    option_widget = widgets.CheckboxInput()

class ClaseForm(FlaskForm):
    serial = IntegerField('Codigo', [validators.InputRequired(), validators.NumberRange(min=1,max=9, message="Las clases deben ser de 1-9")])
    descripcion = StringField('Descripción', [ validators.InputRequired(), validators.Length(max=150)])
    
    string_of_files = ['Cartera\r\nTercero\r\nProveedor\r\nCentroCosto']
    list_of_files = string_of_files[0].split()
    files  = [(x,x) for x in list_of_files]
    example  = MultiCheckboxField('Parametros', choices = files)

    def validate(self):
        rv=FlaskForm.validate(self)
        if not rv:
            return False
        clase = Clase.query.filter_by(serial=self.serial.data).first()
        if clase is not None:
            self.serial.errors.append('La clase que intenta crear, ya se encuentra en uso')
            return False
        else:
            return True

        
class GrupoForm(FlaskForm):
    
    serial_cuenta = IntegerField('Codigo cuenta', [validators.InputRequired(), validators.NumberRange(min=1,max=9, message="Las clases deben ser de 1-9")])
    serial = IntegerField('Codigo', [validators.InputRequired(), validators.NumberRange(min=1,max=9, message="Las clases deben ser de 1-9")])
    descripcion = StringField('Descripción', [ validators.InputRequired(), validators.Length(max=150)])
    
    string_of_files = ['Cartera\r\nTercero\r\nProveedor\r\nCentroCosto']
    list_of_files = string_of_files[0].split()
    files  = [(x,x) for x in list_of_files]
    example  = MultiCheckboxField('Parametros', choices = files)
    