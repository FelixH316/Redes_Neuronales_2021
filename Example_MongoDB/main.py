"""
Date:       2022-01-22
Author:     Félix Armenta Aguiñaga
File:       main.py
Brief:      Example using MongoDB on Python with mongoengine package
Version:    0.0.1
"""

from mongoengine import *
from datetime import *
from paqueteT4.StudentIOv2 import Estudiante


class estudiantes(Document):
    nombre = StringField(required=True, max_length=70)
    correo = StringField(required=True, max_length=70)
    contrasena = StringField(required=True, max_length=50)
    materias = ListField(required=True)
    noControl = IntField(required=True, min_value=10240000, max_value=20249999)
    fecha = DateTimeField(default=datetime.now())


class studentMongoManager:
    def __init__(self):
        connect("IECA", host="localhost", port=27017)
        self.conteo = len(estudiantes.objects())

    def generarNoControl(self):
        nc = self.conteo
        nc += 20240000
        while self.validarNoCotrol(nc):
            nc += 1
            self.conteo += 1
        return nc

    def validarNoCotrol(self, newNoControl, oldNoControl=None):
        if (newNoControl < 10240000) or (newNoControl > 20249999):
            print("\tNo de control no valido, rango de 10240000 a 20249999")
            return True
        lista = estudiantes.objects()
        if lista:
            if newNoControl == oldNoControl:
                return False
            for i in range(len(lista)):
                if newNoControl == lista[i].noControl:
                    return True
            return False
        else:
            return False

    def guardarEstudiante(self, student):
        post = estudiantes(
            nombre=student.getNombre(),
            correo=student.getCorreo(),
            contrasena=student.getContra(),
            materias=student.getMaterias(),
            noControl=student.getNoControl(),
            fecha=datetime.now()
        )
        post.save()
        print(f"\tEstudiante {student.getNoControl()} guardado")

    def mostrarEstudiantes(self):
        # print("\n\tNo. CONTROL\tNOMBRE\tCORREO\t\t\t\t\t\tPASSWORD")
        listaDB = estudiantes.objects()
        if listaDB:
            j = 0
            while (j < len(listaDB)):
                subjects = listaDB[j].materias
                print(f"\tNumero de Control: {listaDB[j].noControl} ______________________________________________")
                print(f"\tNombre: {listaDB[j].nombre} - Correo: {listaDB[j].correo} - Contrasena: {listaDB[j].contrasena}")
                # print(f"\tMateria 1: {subjects[0]} - Materia 2: {subjects[1]} - Materia 3: {subjects[2]}")
                # [PV] Sugerencia para mostrar de 0 a 3 materias, para usar de 0 a N usar un loop
                if len(subjects) > 0:
                    print(f"\tMateria 1: {subjects[0]}")
                if len(subjects) > 1:
                    print(f"\tMateria 2: {subjects[1]}")
                if len(subjects) > 2:
                    print(f"\tMateria 3: {subjects[2]}")
                print(" ")
                j+=1
        else:
            print("\t No hay estudiantes en la base de datos")

    def agregarEstudiante(self):
        name = input("\tIngresa nombre: ")
        mail = input("\tIngresa correo: ")
        password = input("\tIngresa contrasena: ")
        sub1 = input("\tIngresa materia 1: ")
        sub2 = input("\tIngresa materia 2: ")
        sub3 = input("\tIngresa materia 3: ")
        subLista = [sub1, sub2, sub3]
        alumno = Estudiante(name, mail, password, subLista)
        alumno.updateNoControl(self.generarNoControl())
        self.guardarEstudiante(alumno)

    def editarEstudiante(self):
        self.mostrarEstudiantes()
        seleccion = input("\tIngresa el No. de Control del estudiante a modificar: ")
        modificado = estudiantes.objects(noControl=int(seleccion))
        # print(type(modificado)) # Modificado trae una lista de objetos
        name = input("\tIngresa nombre: ")
        mail = input("\tIngresa correo: ")
        password = input("\tIngresa contrasena: ")
        sub1 = input("\tIngresa materia 1: ")
        sub2 = input("\tIngresa materia 2: ")
        sub3 = input("\tIngresa materia 3: ")
        subLista = [sub1, sub2, sub3]
        nc = input("\tIngresa numero de control: ")
        while self.validarNoCotrol(int(nc), int(seleccion)):
            nc = input("\tWARNING repetido, ingresa numero de control: ")
        modificado[0].update(nombre=name, correo=mail, contrasena=password,
                             materias=subLista, noControl=int(nc), fecha=datetime.now())
        print(f"\tEstudiante {modificado[0].noControl} editado")


    def eliminarEstudiante(self):
        self.mostrarEstudiantes()
        seleccion = input("\tIngresa el No. de Control del estudiante a eliminar: ")
        eliminado = estudiantes.objects(noControl=int(seleccion))
        if eliminado:
            print(f"\tEstudiante {eliminado[0].noControl} eliminado")
            eliminado[0].delete()
        else:
            print(f"\tWARNING: No se encontro estudiante {int(seleccion)}")


if __name__ == '__main__':
    correr = True
    admi = studentMongoManager()
    studentData = [
        ["John Locke", "farmentaa.pci@ieca.mx", "Hatch4", ["Historia", "Matematicas", "Geografia"]],
        ["Jack Shepard", "3armenta@gmail.com", "Oceanic815", ["Electronica", "Calculo", "Termodinamica"]],
        ["Sayid Jarra", "15240784@leon.tecnm.mx", "Aye16", ["English", "Metodos Numericos", "Alebra Lineal"]],
        ["Kate Austen", "IECA.Tres@cinvestav.mx", "Austen23", ["Protocolos", "Dinamica", "Calculo Vectorial"]],
        ["James Ford", "ve14893@innovaccion.mx", "Ford42", ["Control", "Robotica", "Ecuaciones Diferenciales"]],
    ]

    while correr:
        print("\n\tREGISTRO DE ESTUDIANTES")
        print("\t1. Publicar registro inicial")
        print("\t2. Mostrar estudiantes")
        print("\t3. Editar estudiante")
        print("\t4. Agregar estudiante")
        print("\t5. Eliminar estudiante")
        print("\t6. Salir del programa")
        ans = input("\tIngresa el numero de tu seleccion: ")

        if ans == '1':
            print("\n\tSUBIENDO A BASE DE DATOS...")
            if estudiantes.objects():
                print("\tWARNING: la base de datos ya tiene objetos")

            else:
                studentList = []
                for i in range(5):
                    objeto = Estudiante(*studentData[i])
                    objeto.updateNoControl(admi.generarNoControl())
                    studentList.append(objeto)
                    admi.guardarEstudiante(studentList[i])
        elif ans == '2':
            print("\n\tMOSTRANDO ESTUDIANTES...")
            admi.mostrarEstudiantes()
        elif ans == '3':
            print("\n\tEDITANDO ESTUDIANTE...")
            admi.editarEstudiante()
        elif ans == '4':
            print("\n\tAGREGANDO ESTUDIANTE...")
            admi.agregarEstudiante()
        elif ans == '5':
            print("\n\tELIMINANDO ESTUDIANTE...")
            admi.eliminarEstudiante()
        elif ans == '6':
            correr = False
        else:
            print("\tOpcion no valida")
