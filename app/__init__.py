from flask import Flask
from app.routes.home import home_bp
from app.routes.about import about_bp
from app.routes.contact import contact_bp
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)

    with app.app_context():
        db.create_all()
    return app