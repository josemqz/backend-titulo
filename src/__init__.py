from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

"""
# Export environment variable for shell session
export DEBUG=true

# Set explicitly for a specific command execution
PORT=8000 python app.py
"""

db = SQLAlchemy()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('src.config.Configuration')
    
    cors = CORS(app)
    
    db.init_app(app)

    with app.app_context():

        from src.models.models import Sala, Ocupacion
        
        db.create_all()

        # if ENV.first:
        # from src.database.poblar_db import poblar
        # poblar()

        return app
