from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

# setup db
db = SQLAlchemy()

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
    # register blueprints
    
    app.register_blueprint(user_app)
    app.register_blueprint(home_app)
    app.register_blueprint(cuenta_app)
    return app
