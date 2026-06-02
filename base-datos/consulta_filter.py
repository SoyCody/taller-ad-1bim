from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico
Session = sessionmaker(bind=engine)
session = Session()
# filter() - filtra registros según una condición
print("=== CARRERAS DE LA FACULTAD DE INGENIERÍA ===")
facultad = session.query(Facultad).filter(Facultad.nombre == 'Facultad de Ingeniería').first()
carreras = session.query(Carrera).filter(Carrera.facultad_id == facultad.id).all()
for c in carreras:
    print(f"  {c.nombre} | Código: {c.codigo}")
print("\n=== PROFESORES CON ESPECIALIDAD EN 'DATOS' ===")
profesores = session.query(Profesor).filter(Profesor.especialidad.like('%Datos%')).all()
for p in profesores:
    print(f"  {p.nombres} {p.apellidos} | Especialidad: {p.especialidad}")
print("\n=== RECURSOS DE TIPO 'Libro' ===")
libros = session.query(RecursoAcademico).filter(RecursoAcademico.tipo == 'Libro').all()
for r in libros:
    print(f"  {r.titulo} | URL: {r.url}")
session.close()