from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None, grado="Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []
        self.grado = grado

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    #@ classmethod
    #def asignarNombre(cls, nombre=None):
        #if nombre is not None:
            #cls.grado = nombre
        #else:
            #cls.grado = "Grado 12" if cls.grado is None else cls.grado
        #return cls.grado

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"):
        #cls.grado = nombre
