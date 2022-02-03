# DESCRIPTION:  Modulo con la clase Estudiante
#               Incluye metodos para obtener los atributos privados y también para actualizarlos
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3


class Estudiante:
    def __init__(self, nombre="_", correo="_", contra="_", materias="_", noControl=None):
        self.__nombre = nombre
        self.__correo = correo
        self.__contra = contra
        self.__materias = materias
        self.__noControl = noControl

    def getNoControl(self):
        return self.__noControl

    def getNombre(self):
        return self.__nombre

    def getCorreo(self):
        return self.__correo

    def getContra(self):
        return self.__contra

    def getMaterias(self):
        return self.__materias

    def updateNombre(self, nombre=None):
        if nombre:
            self.__nombre = nombre
            return True
        else:
            return False

    def updateCorreo(self, correo=None):
        if correo:
            self.__correo = correo
            return True
        else:
            return False

    def updateContra(self, contra=None):
        if contra:
            self.__contra = contra
            return True
        else:
            return False

    def updateMaterias(self, materias=None):
        if materias:
            self.__materias = materias
            return True
        else:
            return False

    def updateNoControl(self, noControl=None):
        if noControl is not None:
            self.__noControl = noControl
            return True
        else:
            return False
