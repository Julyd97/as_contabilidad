from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_marshmallow import Marshmallow

from proveedores.error_handling import ObjectNotFound, AppErrorBaseClass
# setup db
db = SQLAlchemy()
ma = Marshmallow()

#methods
class BaseModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()
def create_app(** config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # import blueprints
    
    from user.views import user_app
    from home.views import home_app
    from cuentas.views import cuenta_app
    from cartera.api import cartera_app
    from proveedores.api import proveedores_app
    from documentoscontables.api import documentoscontables_app
    from registro.api import registro_app
    # register blueprints
    
    app.register_blueprint(user_app)
    app.register_blueprint(home_app)
    app.register_blueprint(cuenta_app)
    app.register_blueprint(cartera_app)
    app.register_blueprint(proveedores_app)
    app.register_blueprint(documentoscontables_app)
    app.register_blueprint(registro_app)
    return app
