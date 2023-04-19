from src import init_app
from src.models.models import Sala

def crear_salas():
    app = init_app()
    with app.app_context:
        #test
        Sala.crear(svg_id="rect954", nombre="A-001", ocupacion_max = 50)

if __name__ == "__main__":
    crear_salas()