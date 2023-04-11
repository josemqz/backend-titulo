from flask_sqlalchemy import SQLAlchemy
# importar db?
from main import db

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    ocupacion_max = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Sala %r>' % self.name

class Ocupacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sala_id = db.Column(db.Integer, foreign_key=True)
    ocupacion_actual = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False) # cambiar por tiempo