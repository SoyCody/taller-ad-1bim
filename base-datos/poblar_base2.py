import json
import os
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Carrera, Facultad
Session =sessionmaker(bind=engine)
session = Session()

ruta = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'carreras.json')

with open(ruta, encoding='utf-8') as f:
    datos = json.load(f)
for item in datos:
    facultad = session.query(Facultad).filter(Facultad.nombre == item['facultad']).first()
    carrera = Carrera(
        id=item['id'],
        nombre=item['nombre'],
        codigo=item['codigo'],
        facultad_id=facultad.id
    )
    session.add(carrera)
session.commit()
session.close()
print("Carreras ingresadas correctamente.")
