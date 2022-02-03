"""
Date:       2022-01-22
Author:     Félix Armenta Aguiñaga
File:       StudentIOv2.py
Brief:      This file includes the Estudiante class declared with private 
            attributes and the corresponding methods to update them.
Version:    0.0.1
"""


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
