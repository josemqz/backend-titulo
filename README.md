# backend-titulo
Backend de sitio web diseñado para visualizar los resultados de Crowd Counting en el campus San Joaquín de la Universidad Técnica Federico Santa María

## Instrucciones

### Ingresar a entorno virtual

Instalar módulo de entornos virtuales  
```
sudo apt update  
sudo apt install python3-venv
```  
  
Activar entorno  
```
source ./backend_env/bin/activate
```  
  
Desactivar entorno  
```
deactivate
```  

### Crear Base de Datos

Abrir entorno de Flask  
```
export FLASK_APP=main  
flask shell
```

Crear base de datos y tablas definidas en `main.py`  
```
from main import db, Sala, Ocupacion  
db.create_all()
```

Eliminar tablas (útil en caso de actualizar columnas)  
```
from main import db  
db.drop_all()
```

### Poblar Base de Datos

Crear instancias de datos  
```
flask shell  
  
from main import db, Sala, Ocupacion  
  
sala_a000 = Sala(nombre: 'A-000', ocupacion_max: 100)  
  
ocupacion_00_a000 = Ocupacion(sala_id='A-000'  
                            ocupacion_actual=0  
                            timestamp='00:00:00')  
```  

Añadir datos creados  
```
db.session.add(sala_a000)  
db.session.add(ocupacion_00_a000)  
```  

Aplicar los cambios  
```
db.session.commit()
```  

Mostrar los datos de tabla Sala  
```
Sala.query.all()
```  
  
_Referencia: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application_