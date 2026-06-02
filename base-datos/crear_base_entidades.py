from configuracion import cadena_base_datos
from sqlalchemy import Column, ForeignKey, Integer, String, Date, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine=create_engine(cadena_base_datos)
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Facultad(Base):
    __tablename__ = 'facultad'
    id = Column(Integer, primary_key=True)
    nombre =Column(String(150), nullable=False)
    ubicacion =Column(String(100))
    decano= Column(String(100))
    def __str__(self):
        return f"Facultad(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}', decano='{self.decano}')"
class Carrera(Base):
    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    codigo = Column(String(20), nullable=False)
    facultad_id = Column(Integer, ForeignKey('facultad.id'))
    def __str__(self):
        return f"Carrera(id={self.id}, nombre='{self.nombre}', codigo='{self.codigo}', facultad_id={self.facultad_id})"

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150))
    especialidad = Column(String(100))
    carrera_id = Column(Integer, ForeignKey('carrera.id'))
    def __str__(self):
        return f"Profesor(id={self.id}, nombres='{self.nombres}', apellidos='{self.apellidos}', correo='{self.correo}', especialidad='{self.especialidad}', carrera_id={self.carrera_id})"

class RecursoAcademico(Base):
    __tablename__ = 'recurso_academico'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(Date)
    tipo = Column(String(50))
    url = Column(String(500))
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    def __str__(self):
        return f"RecursoAcademico(id={self.id}, titulo='{self.titulo}', fecha_publicacion={self.fecha_publicacion}, tipo='{self.tipo}', url='{self.url}', profesor_id={self.profesor_id})"
Facultad.carreras =relationship('Carrera', back_populates='facultad')
Carrera.facultad =relationship('Facultad', back_populates='carreras')
Carrera.profesores=relationship('Profesor', back_populates='carrera')
Profesor.carrera= relationship('Carrera', back_populates='profesores')
Profesor.recursos =relationship('RecursoAcademico', back_populates='profesor')
RecursoAcademico.profesor = relationship('Profesor', back_populates='recursos')

Base.metadata.create_all(engine)
