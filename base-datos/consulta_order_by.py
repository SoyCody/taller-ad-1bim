from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico

Session =sessionmaker(bind=engine)
session=Session()
# order_by() ordena los resultados por un campo
print("=== FACULTADES ORDENADAS POR NOMBRE (ASC) ===")
facultades = session.query(Facultad).order_by(Facultad.nombre).all()
for f in facultades:
    print(f"  {f.nombre} | Decano: {f.decano}")

print("\n=== PROFESORES ORDENADOS POR APELLIDO (ASC) ===")
profesores = session.query(Profesor).order_by(Profesor.apellidos).all()
for p in profesores:
    print(f"  {p.apellidos}, {p.nombres} | Especialidad: {p.especialidad}")
print("\n=== RECURSOS ORDENADOS POR FECHA DE PUBLICACIÓN (ASC) ===")
recursos = session.query(RecursoAcademico).order_by(RecursoAcademico.fecha_publicacion).all()
for r in recursos:
    print(f"  {r.fecha_publicacion} | {r.titulo} | Tipo: {r.tipo}")

print("\n=== CARRERAS ORDENADAS POR CÓDIGO (DESC) ===")
carreras = session.query(Carrera).order_by(Carrera.codigo.desc()).all()
for c in carreras:
    print(f"  {c.codigo} | {c.nombre}")

session.close()
