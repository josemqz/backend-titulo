from flask import jsonify
from flask import current_app as app
from src.models.models import Sala


# obtener información de la sala, incluyendo id, nombre, ocupación máxima 
@app.route('/salas', methods=['GET'])
def get_salas():
    salas = Sala.get_salas()
    return jsonify([{'id': sala.id,
                     'svg_id': sala.svg_id,
                     'nombre': sala.nombre, 
                     'ocupacion_max': sala.ocupacion_max} for sala in salas])

@app.route('/sala/<int:id>', methods=['GET'])
def get_sala_by_id():
    salas = Sala.get_sala_by_id()
    return salas
    
