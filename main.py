from flask import Flask
from flask_env import MetaFlaskEnv
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from flask_cors import CORS
from dbmodel import Sala, Ocupacion

class Configuration(metaclass=MetaFlaskEnv):
    DB_ROOT_PASSWORD="123"
    DB_NAME=""
    DB_USER=""
    DB_PASSWORD="123"
    DB_HOST="localhost"
    DB_PORT=3306

"""
# Export environment variable for shell session
export DEBUG=true

# Set explicitly for a specific command execution
PORT=8000 python app.py
"""

app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
cors = CORS(app)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"

# obtener información de la sala, incluyendo id, nombre, ocupación máxima 
@app.route('/info_sala', methods=['GET'])
def get_info_sala():
    salas = Sala.query.all()
    return jsonify([{'id': sala.id, 
                     'nombre': sala.nombre, 
                     'ocupacion_max': sala.ocupacion_max} for sala in salas])

# Obtener info de ocupación actual de una sala específica
@app.route('/ocupacion_actual/<int:sala_id>', methods=['GET'])
def get_ocupacion_actual(sala_id):
    ocupacion = Ocupacion.query.get(sala_id)
    if not ocupacion:
        return jsonify({'error': 'Sala no encontrada'}), 404
    return jsonify({'sala': sala_id, 
                     'timestamp': ocupacion.timestamp, 
                     'ocupacion_actual': ocupacion.ocupacion_actual})

# Obtener info de ocupación actual de todas las salas
@app.route('/ocupacion_actual', methods=['GET'])
def get_all_ocupaciones_actuales():
    ocupaciones = Ocupacion.query.all()
    return jsonify([{'id': ocupacion.id, 
                     'timestamp': ocupacion.timestamp, 
                     'sala': ocupacion.sala_id, 
                     'ocupacion_actual': ocupacion.ocupacion_actual} for ocupacion in ocupaciones])

# Agregar ocupación actual de una sala específica
@app.route('/ocupacion_actual', methods=['POST'])
def add_ocupacion_actual():

    sala_id = request.args.get('sala_id')
    timestamp = request.args.get('timestamp')
    ocupacion_actual = request.args.get('ocupacion_actual')
    ocupacion = Ocupacion(timestamp=timestamp, sala=sala_id, ocupacion_actual=ocupacion_actual)

    db.session.add(ocupacion)
    db.session.commit()
    return jsonify({'id': ocupacion.id, 
                    'timestamp': ocupacion.timestamp, 
                    'sala': ocupacion.sala_id, 
                    'ocupacion_actual': ocupacion_actual})


if __name__ == "__main__":
    app.run()