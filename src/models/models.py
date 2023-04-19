from sqlalchemy.sql import func
from src import db # importa db de __init__

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    svg_id = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    ocupacion_max = db.Column(db.Integer, nullable=False)
    ocupaciones = db.relationship('Ocupacion', backref='ocupacion', lazy='dynamic')
    # lazy=dinamic: retorna un objeto al que se puede aplicar distintos filtros, como all() y filter_by()
    
    def __init__(self, svg_id: int, nombre: str, ocupacion_max: int):
        self.svg_id = svg_id
        self.nombre = nombre
        self.ocupacion_max = ocupacion_max
    
    def __repr__(self):
        return '<Sala %r>' % self.nombre
    
    @staticmethod
    def crear(svg_id, nombre, ocupacion_max):
        nueva_sala = Sala(svg_id, nombre, ocupacion_max)
        db.session.add(nueva_sala)
        db.session.commit()

    @staticmethod
    def get_salas():
        return [{'id': i.id, 'svg_id': i.svg_id, 'nombre': i.nombre, 'ocupacion_max': i.ocupacion_max}
                for i in Sala.query.order_by('id').all()]
    
    @staticmethod
    def get_sala_by_id(id):
        return Sala.query.filter_by(id=id)


class Ocupacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sala_id = db.Column(db.Integer, db.ForeignKey(Sala.id))
    ocupacion_actual = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), 
                           nullable=False)

    def __repr__(self):
        return '<Ocupacion actual: %r [Sala %r]>' % (self.ocupacion_actual, self.sala_id)

    @staticmethod
    def crear(sala_id, ocupacion_actual, timestamp):
        nueva_ocupacion = Ocupacion(sala_id, ocupacion_actual, timestamp)
        db.session.add(nueva_ocupacion)
        db.session.commit()

    @staticmethod
    def get_ocupaciones():
        return [{'id': i.id, 'svg_id': i.svg_id, 'nombre': i.nombre, 'ocupacion_max': i.ocupacion_max,}
                for i in Ocupacion.query.order_by('id').all()]
    
        # return Ocupacion.query.order_by('id').all()

    @staticmethod
    def get_ocupaciones_by_sala_id(sala_id):
        # se supone que debería buscar en salas y de esa sala sacar la ocupacion
        return Sala.ocupacion.filter_by(sala_id=sala_id)
        # session.query(Sala).first().ocupaciones.all()

    def delete_ocupaciones_by_id(id):
        return Ocupacion.query.filter(Ocupacion.id == id).delete()