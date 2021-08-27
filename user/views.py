from flask import Blueprint,render_template, redirect, session, url_for, flash, Flask,abort
from flask_mail import Mail,Message
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
import random
import os


from user.models import User
from user.forms  import RegisterForm, LoginForm, RecoveryForm, PasswordForm
from application import db
from settings import mail_settings, MAIL_USERNAME,SECRET_KEY

#Create blueprint
user_app = Blueprint('user_app', __name__)
# Mail settings
app = Flask(__name__)
app.config.update(mail_settings)
mail = Mail(app)

ts = URLSafeTimedSerializer(secret_key=SECRET_KEY, salt = 'recover-key')

@user_app.route('/send_email')
def send_email(subject,recipients,body):
     with app.app_context():
            msg = Message(subject=subject,
                    sender=MAIL_USERNAME,
                    recipients=recipients, 
                    body=body)
            mail.send(msg)

@user_app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            form.full_name.data,
            form.telephone.data,
            form.email.data,
            hashed_password,
            form.college_name.data,
            form.college_direction.data,
            form.college_nit.data
        )
        db.session.add(user)
        db.session.commit()
        send_email(subject="Registro exitoso As Contable!!",
                    recipients=[form.email.data], 
                    body="Bienvenido a As contable, su aliado en contabilidades de entidades")
        flash('Usted ya se encuentra registrado, porfavor inicie sesión')

        return redirect(url_for('.login'))
    return render_template('user/register.html', form=form, cache_id=random.randrange(10000))

@user_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, college_nit = form.college_nit.data).first()
        session['id'] = user.id
        print(session['id'])
        session['full_name'] = user.full_name

        return redirect(url_for('home_app.index'))
    
    return render_template('user/login.html', form=form, error=error, cache_id=random.randrange(10000))

@user_app.route('/logout')
def logout():
    session.pop('id')
    session.pop('full_name')
    flash('User logged out')
    return redirect(url_for('home_app.index'))

@user_app.route('/recovery', methods = ['GET', 'POST'])
def recovery():
    form = RecoveryForm()
    
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data, college_nit=form.college_nit.data).first()

        token = ts.dumps([form.email.data, form.college_nit.data], salt ='recover-key')
        recovery_url = url_for('.recover',token=token,_external=True)
        send_email(subject = "Password reset requested", recipients=[form.email.data], body=recovery_url)
        flash('Se envio un link a su correo, porfavor revise')
    
    return render_template('user/recovery.html', form=form)

@user_app.route('/recover/<token>', methods=[ 'GET', 'POST'])
def recover(token):
    try:
        [email,college_nit] = ts.loads(token, salt = 'recover-key', max_age=86400)
        print(email)
        print(college_nit)
    except:
        abort(404)
    
    form = PasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email, college_nit=college_nit).first()
        hashed_password = generate_password_hash(form.password.data)
        user.password = hashed_password

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
    return render_template('user/recover.html', form=form, token=token)    
