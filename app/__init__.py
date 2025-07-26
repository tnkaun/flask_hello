from flask import Flask
from app.routes.home import home_bp
from app.routes.about import about_bp
from app.routes.contact import contact_bp
from app.routes.board import board_bp
from app.routes.auth import auth_bp
from config import Config
from app.extensions import db


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        #db.drop_all()
        db.create_all()
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(board_bp)
    app.register_blueprint(auth_bp)
    
    return app