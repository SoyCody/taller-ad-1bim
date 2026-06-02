from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico
Session=sessionmaker(bind=engine)
session = Session()
# and_() - filtra registros que cumplan todas las condiciones simultáneamente
print("=== PROFESORES DE INGENIERÍA EN SOFTWARE CON CORREO INSTITUCIONAL ===")
carrera_isw = session.query(Carrera).filter(Carrera.codigo == 'ISW001').first()
profesores = session.query(Profesor).filter(
    and_(
        Profesor.carrera_id == carrera_isw.id,
        Profesor.correo.like('%@universidad.edu')
    )
).all()
for p in profesores:
    print(f"  {p.nombres} {p.apellidos} | Correo: {p.correo} | Especialidad: {p.especialidad}")
print("\n=== RECURSOS TIPO 'Guia' PUBLICADOS EN 2024 ===")
from datetime import date
recursos = session.query(RecursoAcademico).filter(
    and_(
        RecursoAcademico.tipo == 'Guia',
        RecursoAcademico.fecha_publicacion >= date(2024, 1, 1),
        RecursoAcademico.fecha_publicacion <= date(2024, 12, 31)
    )
).all()
for r in recursos:
    print(f"  {r.titulo} | Fecha: {r.fecha_publicacion} | URL: {r.url}")

print("\n=== CARRERAS CON CÓDIGO QUE EMPIEZA POR 'I' Y PERTENECEN A FACULTAD ID 1 ===")
carreras = session.query(Carrera).filter(
    and_(
        Carrera.codigo.like('I%'),
        Carrera.facultad_id == 1
    )
).all()
for c in carreras:
    print(f"  {c.codigo} | {c.nombre}")

session.close()
