from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico

Session= sessionmaker(bind=engine)
session =Session()
# or_() - filtra registros que cumplan al menos una condición
print("=== RECURSOS DE TIPO 'Libro' O 'Video' ===")
recursos = session.query(RecursoAcademico).filter(
    or_(RecursoAcademico.tipo == 'Libro', RecursoAcademico.tipo == 'Video')
).all()
for r in recursos:
    print(f"  [{r.tipo}] {r.titulo}")

print("\n=== PROFESORES CON ESPECIALIDAD EN 'Inteligencia Artificial' O 'Bases de Datos' ===")
profesores = session.query(Profesor).filter(
    or_(
        Profesor.especialidad == 'Inteligencia Artificial',
        Profesor.especialidad == 'Bases de Datos'
    )
).all()
for p in profesores:
    print(f"  {p.nombres} {p.apellidos} | Especialidad: {p.especialidad}")

print("\n=== FACULTADES EN 'Edificio A' O 'Edificio C' ===")
facultades = session.query(Facultad).filter(
    or_(Facultad.ubicacion == 'Edificio A', Facultad.ubicacion == 'Edificio C')
).all()
for f in facultades:
    print(f"  {f.nombre} | Ubicación: {f.ubicacion}")

session.close()
