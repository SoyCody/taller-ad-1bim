from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico
Session = sessionmaker(bind=engine)
session = Session()
# Facultad → Carrera → Profesor → RecursoAcademico
facultades = session.query(Facultad).order_by(Facultad.nombre).all()
for facultad in facultades:
    print(f"\n{'='*60}")
    print(f"FACULTAD: {facultad.nombre}")
    print(f"Decano: {facultad.decano}")
    print(f"Ubicación: {facultad.ubicacion}")
    print(f"{'='*60}")
    recursos = (
        session.query(RecursoAcademico)
        .join(Profesor, RecursoAcademico.profesor_id == Profesor.id)
        .join(Carrera, Profesor.carrera_id == Carrera.id)
        .join(Facultad, Carrera.facultad_id == Facultad.id)
        .filter(Facultad.id == facultad.id)
        .order_by(RecursoAcademico.fecha_publicacion)
        .all()
    )
    if recursos:
        for r in recursos:
            print(f"Tipo de recurso: {r.tipo}")
            print(f"Titulo {r.titulo}")
            print(f"Fecha: {r.fecha_publicacion}")
            print(f"URL: {r.url}")
    else:
        print("error")
session.close()
