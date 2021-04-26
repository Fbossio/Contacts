from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
form flask import Flask


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(_name__, instance_relative_config=False)
    app.config.from_object(config[config_name])

    from .models import User, Contact

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app
