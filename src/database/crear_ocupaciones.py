from src import init_app
import datetime
from src.models.models import Ocupacion

def crear_ocupacion():
    app = init_app()
    with app.app_context:
        #test
        Ocupacion.crear(sala_id='1',
                        ocupacion_actual=30,
                        timestamp=datetime.datetime.utcnow())


# if __name__ == "__main__":
#     crear_ocupacion()