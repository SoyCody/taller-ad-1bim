import json
import os
from datetime import date
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, RecursoAcademico, Profesor
Session =sessionmaker(bind=engine)
session =Session()

ruta = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'recursos_academicos.json')
with open(ruta, encoding='utf-8') as f:
    datos = json.load(f)

for item in datos:
    nombre_completo = item['profesor'].split(' ')
    nombres = nombre_completo[0]
    apellidos = ' '.join(nombre_completo[1:])
    profesor = session.query(Profesor).filter(
        Profesor.nombres == nombres,
        Profesor.apellidos == apellidos
    ).first()
    recurso = RecursoAcademico(
        id=item['id'],
        titulo=item['titulo'],
        fecha_publicacion=date.fromisoformat(item['fecha_publicacion']),
        tipo=item['tipo'],
        url=item['url'],
        profesor_id=profesor.id
    )
    session.add(recurso)
session.commit()
session.close()
print("Recursos académicos ingresados correctamente.")
