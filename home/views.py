from pydoc import plain
from flask import Blueprint,session, render_template, send_from_directory
from werkzeug.utils import redirect
from cuentas.forms import ModificarForm
import os
import random

home_app = Blueprint('home_app', __name__)

@home_app.route('/')
def index():
    if session.get('full_name'):
        return redirect('/plan')
    return render_template('home/general.html', cache_id=random.randrange(10000))

@home_app.route('/images/<filename>')
def image(filename):
    return send_from_directory(os.getcwd() + "/images/", filename=filename, as_attachment=False)

# @home_app.route('/plan')
# def plan():
#     if session.get('full_name'):
#         return redirect('/plan')
#     return render_template('home/general.html', cache_id=random.randrange(10000))
    