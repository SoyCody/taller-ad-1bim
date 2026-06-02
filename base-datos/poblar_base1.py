import json
import os
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad
Session=sessionmaker(bind=engine)
session = Session()
ruta=os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'facultades.json')
with open(ruta, encoding='utf-8') as f:
    datos = json.load(f)
for item in datos:
    facultad = Facultad(
        id=item['id'],
        nombre=item['nombre'],
        ubicacion=item['ubicacion'],
        decano=item['decano']
    )
    session.add(facultad)
session.commit()
session.close()
print("Facultades ingresadas correctamente.")
