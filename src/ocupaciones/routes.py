from flask import Blueprint, jsonify, request
from flask import current_app as app
# from main import app
from src.models.models import Ocupacion

# bp = Blueprint('ocupaciones', __name__)

# Obtener info de ocupación actual de una sala específica
@app.route('/ocupacion_actual/<int:sala_id>', methods=['GET'])
def get_ocupaciones_by_sala_id(sala_id):
    return Ocupacion.get_ocupacion_by_sala_id(sala_id)

# Obtener info de ocupación actual de todas las salas
@app.route('/ocupacion_actual', methods=['GET'])
def get_all_ocupaciones_actuales():
    ocupaciones = Ocupacion.get_ocupaciones()
    return jsonify([{'id': ocupacion.id, 
                     'timestamp': ocupacion.timestamp, 
                     'sala_id': ocupacion.sala_id, 
                     'ocupacion_actual': ocupacion.ocupacion_actual} for ocupacion in ocupaciones])

# Agregar ocupación actual de una sala específica
@app.route('/ocupacion_actual', methods=['POST'])
def add_ocupacion_actual():

    sala_id = request.args.get('sala_id')
    timestamp = request.args.get('timestamp')
    ocupacion_actual = request.args.get('ocupacion_actual')

    # implementar try except
    ocupacion = Ocupacion.crear(sala_id, ocupacion_actual, timestamp)
    
    return jsonify({'id': ocupacion.id, 
                    'timestamp': ocupacion.timestamp, 
                    'sala_id': ocupacion.sala_id, 
                    'ocupacion_actual': ocupacion_actual})

@app.route('/ocupacion_actual', methods=['POST'])
def delete_ocupacion():
    # implementar mensajes
    return Ocupacion.eliminar_por_id(id)