from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, ValidationError, IntegerField
from wtforms.fields.html5 import EmailField
from werkzeug.security import check_password_hash

from user.models import User


class LoginForm(FlaskForm):

    college_nit = IntegerField('Nit del Colegio', [validators.InputRequired()])
    email = EmailField('Correo Electronico', [validators.InputRequired(), validators.Email()])
    password =PasswordField('Contraseña', [
        validators.Required(),
        validators.Length(min=4, max=80)
    ])

    def validate(self):
        rv=FlaskForm.validate(self)
        if not rv:
            return False
        
        user = User.query.filter_by(
            email = self.email.data, college_nit = self.college_nit.data
        ).first()

        if user:
            if not check_password_hash(user.password, self.password.data):
                self.password.errors.append('Incorrect email or password')
                return False
            return True
        else:
            self.password.errors.append('Incorrect email or password')
            return False

class RegisterForm(FlaskForm):

    full_name = StringField('Nombre Completo', [validators.InputRequired()], render_kw={"placeholder": "Alberto tovar"})
    telephone = IntegerField('Telefono', [validators.InputRequired(), validators.NumberRange(min=3000000000)],  render_kw={"placeholder": "365478"})
    email = EmailField('Correo Electronico', [validators.InputRequired(), validators.Email()],  render_kw={"placeholder": "myemail@example.com"})
    password = PasswordField('Nueva contraseña',[validators.InputRequired(),validators.Length(min=4, max=80)],  render_kw={"placeholder": "Contraseña"})
    confirm = PasswordField('Repetir contraseña', [validators.EqualTo('password', message='Passwords must match'),],  render_kw={"placeholder": "Repita contraseña"})
    college_name = StringField('Nombre del Colegio', [validators.InputRequired()],  render_kw={"placeholder": "Colegio alberto"})
    college_direction = StringField('Dirección del Colegio', [validators.InputRequired()],  render_kw={"placeholder": "Cra 1122 # 15-65"})
    college_nit = IntegerField('Nit', [validators.InputRequired()], render_kw={"placeholder": "123456789"})

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data, college_nit=self.college_nit.data).first()
        if user is not None:
            raise ValidationError('El email y el nit ya esta en uso, porfavor utilice otro.')

class RecoveryForm(FlaskForm):

    college_nit = IntegerField('Nit', [validators.InputRequired()])
    email = EmailField('Correo Electronico', [validators.InputRequired(), validators.Email()])

class PasswordForm(FlaskForm):

    password = PasswordField('Nueva contraseña', [validators.InputRequired(), validators.Length(min=4, max=80)], render_kw={"placeholder": "Nueva contraseña"})
    confirm = PasswordField('Repetir contraseña', [validators.EqualTo('password', message='Passwords must match'),], render_kw={"placeholder": "Repita la contraseña"})