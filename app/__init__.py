import os
from flask import Flask
from .database import db
from .routes import api as main_api
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    JWTManager(app)
    main_api.init_app(app)

    with app.app_context():
        db.create_all()

    return app
