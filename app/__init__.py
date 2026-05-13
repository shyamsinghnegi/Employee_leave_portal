from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    from app import models
    from app.routes.auth import auth
    from app.routes.employee import employee
    from app.routes.manager import manager
    
    app.config.from_object(Config)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(auth)
    app.register_blueprint(employee)
    app.register_blueprint(manager)
    return app
    
    