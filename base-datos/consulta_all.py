from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico
Session =sessionmaker(bind=engine)
session =Session()

# all() - retorna todos los registros de la tabla
print("=== FACULTADES ===")
facultades=session.query(Facultad).all()
for f in facultades:
    print(f"  [{f.id}] {f.nombre} | Decano: {f.decano} | Ubicación: {f.ubicacion}")

print("\n=== CARRERAS ===")
carreras = session.query(Carrera).all()
for c in carreras:
    print(f"  [{c.id}] {c.nombre} | Código: {c.codigo} | Facultad ID: {c.facultad_id}")

print("\n=== PROFESORES ===")
profesores = session.query(Profesor).all()
for p in profesores:
    print(f"  [{p.id}] {p.nombres} {p.apellidos} | Especialidad: {p.especialidad} | Correo: {p.correo}")

print("\n=== RECURSOS ACADÉMICOS ===")
recursos = session.query(RecursoAcademico).all()
for r in recursos:
    print(f"  [{r.id}] {r.titulo} | Tipo: {r.tipo} | Fecha: {r.fecha_publicacion}")

session.close()
