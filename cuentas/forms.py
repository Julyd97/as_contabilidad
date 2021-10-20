from flask_wtf import FlaskForm
from wtforms import BooleanField, validators,ValidationError, StringField, PasswordField, widgets, SelectMultipleField, IntegerField

from cuentas.models import Clase, Grupo, Cuenta, Subcuenta, Auxiliar


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

class CuentasForm(FlaskForm):
    
    serial=IntegerField('Codigo', [validators.InputRequired(), validators.NumberRange(min=1,max=9999999999, message="Las clases deben ser de 1-9")])
    descripcion = StringField('Descripción', [ validators.InputRequired(), validators.Length(max=150)])
    
    string_of_files = ['Cartera\r\nTercero\r\nProveedor\r\nCentroCosto']
    list_of_files = string_of_files[0].split()
    files  = [(x,x) for x in list_of_files]
    example  = MultiCheckboxField('Parametros', choices = files)
    
    def validate(self):
        rv=FlaskForm.validate(self)
        if not rv:
            return False
        serial = self.serial.data
        serial = list(map(int,str(serial)))
        serial_digits = [str(digit) for digit in serial]
        serial_clase  = int("".join(serial_digits[0]))
        clase = Clase.query.filter_by(serial=serial_clase).first()
        if clase is not None:
            if (len(serial) > len(str(serial_clase))):
                serial_grupo = int("".join(serial_digits[0:2]))
                grupo = Grupo.query.filter_by(serial=serial_grupo).first()
                if grupo is not None:
                    if (len(serial) > len(str(serial_grupo))):
                        if(len(serial[2:])%2 == 0):    
                            serial_cuenta = int("".join(serial_digits[0:4]))
                            cuenta = Cuenta.query.filter_by(serial=serial_cuenta).first()
                            if cuenta is not None:
                                if(len(serial) > len(str(serial_clase))):
                                    serial_subcuenta = int("".join(serial_digits[0:6]))
                                    subcuenta = Subcuenta.query.filter_by(serial=serial_subcuenta).first()
                                    if subcuenta is not None:
                                        if (len(serial) > len(str(serial_subcuenta))):
                                            serial_auxiliar = int("".join(serial_digits[0:8]))
                                            auxiliar = Auxiliar.query.filter_by(serial=serial_auxiliar).first()
                                            if auxiliar is not None:
                                                if (len(serial) > len(str(serial_auxiliar))):
                                                    serial_subauxiliar = int("".join(serial_digits))
                                                    subauxiliar = Subauxiliar.query.filter_by(serial = serial_subauxiliar).first()
                                                    if subauxiliar is not None:
                                                        self.serial.errors.append('La clase que intenta crear, ya se encuentra en uso')
                                                        return False
                                                    else:
                                                        return True
                                                else:
                                                    self.serial.errors.append('La clase que intenta crear, ya se encuentra en uso')
                                            elif (len(serial) > len(str(serial_auxiliar))):
                                                self.serial.errors.append( 'El objeto intenta crear, no tiene un auxiliar creado.')
                                                return False
                                            else:
                                                return True
                                        else:
                                            self.serial.errors.append('La clase que intenta crear, ya se encuentra en uso')
                                            return False
                                    elif(len(serial) > len(str(serial_subcuenta))):
                                        self.serial.errors.append( 'El objeto intenta crear, no tiene una subcuenta creada.')
                                        return False
                                    else:
                                        return True
                                else:
                                    self.serial.errors.append('La clase que intenta crear, ya se encuentra en uso')
                                    return False
                            elif(len(serial) > len(str(serial_cuenta))):
                                print(serial)
                                print(serial_cuenta)
                                self.serial.errors.append( 'El objeto intenta crear, no tiene una cuenta creada.')
                                return False
                            else:
                                return True
                        else:
                            self.serial.errors.append('La clase que intenta crear es invalida')
                            return False
                    else:
                        self.serial.errors.append('La clase que intenta crear, ya esta sen uso')
                        return False
                elif (len(serial) > len(str(serial_grupo))):                                
                    self.serial.errors.append('El objeto que intenta crear, no tiene un grupo creado.')
                    return False
                else:
                    return True
            else:
                self.serial.errors.append('La clase que intenta crear, ya se encuentra en uso')
                return False
        elif (len(serial) > len(str(serial_clase))):
            self.serial.errors.append('El objeto que intenta crear, no tiene una clase creada.')
            return False
        else:
            return True

class ModificarForm(FlaskForm):
    serial = IntegerField('Serial:')
    descripcion = StringField('Descripción')
    cartera  = BooleanField('Cartera')
    tercero = BooleanField('Tercero')
    proveedor = BooleanField('Proveedor')
    costo = BooleanField('C.Costo')