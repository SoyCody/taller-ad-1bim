import json
import os
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Profesor, Carrera
Session =sessionmaker(bind=engine)
session =Session()
ruta = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'profesores.json')
with open(ruta, encoding='utf-8') as f:
    datos = json.load(f)

for item in datos:
    carrera = session.query(Carrera).filter(Carrera.nombre == item['carrera']).first()
    profesor = Profesor(
        id=item['id'],
        nombres=item['nombres'],
        apellidos=item['apellidos'],
        correo=item['correo'],
        especialidad=item['especialidad'],
        carrera_id=carrera.id
    )
    session.add(profesor)
session.commit()
session.close()
print("Profesores ingresados correctamente.")
