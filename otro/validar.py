import re
from b_Models.alumno import ModelAlumno
from b_Models.periodo import ModelPeriodo
from b_Models.profesor import ModelProfesor
from b_Models.curso import ModelCurso
from b_Models.profesor_curso import Model_Profesor_Curso
from b_Models.salones import Salones
from b_Models.malla_curricular import Model_Malla_Curricular
from b_Models.notas import Notas
from datetime import datetime


class Validacion:
    def __init__(self):
        self.alumno=ModelAlumno()
        self.periodo=ModelPeriodo()
        self.profesor=ModelProfesor()
        self.cursos=ModelCurso()
        self.profesor_cursos=Model_Profesor_Curso()
        self.salones=Salones()
        self.malla_curricular=Model_Malla_Curricular()
        self.notas=Notas()

    def validar_nota(self):
        while True:
            try:
                while True:
                    nota=float(input(f"Ingrese la nota:\n"))
                    if nota>=0 and nota<=20:
                        break
                    else:
                        print("Ingrese una nota entre 0 a 20")
                break
            except ValueError:
                print(f'Ingrese un numero valido')
        return nota
    @classmethod
    def validar_texto(cls,Comentario):
        texto=""
        while True:
            texto=input(f"{Comentario}:\n")
            if cls.validar_palabra_alfabetico(texto):
                return texto
                  
            else:
                print("Error-El texto ingresado contiene caracteres numericos")

    @staticmethod
    def validar_palabra_alfabetico(texto):
        valor_de_verdad=True
        lista_texto=texto.split(" ")
        for palabra in lista_texto:
            if palabra.isalpha():
                valor_de_verdad=True  
            else:
                valor_de_verdad=True
        return valor_de_verdad
    @staticmethod
    def validar_edad(Comentario):
        edad=''
        while True:
            try:
                while True:
                    edad=int(input(f"{Comentario}:\n"))
                    if edad>=0 and edad<=100:
                        return edad
                    else:
                        print("Error-Ingrese una edad entre 0 a 100")
                break
            
            except ValueError:
                print(f'Error-Ingrese un numero valido')
    @staticmethod
    def validar_correo(Comentario):
        correo=''
        while True:
            correo=input(f"{Comentario}:\n")
            expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    
            if re.match(expresion_regular,correo.lower()):
                return correo
            else:
                print("Error-Correo ingresado no válido")

    def validar_id_correcto_alumno(self,codigo_ingresado):
        alumnos=self.alumno.get_alumno_all('alumno_id')
        valor=False
        for alumno in alumnos:
            if(alumno[0]==codigo_ingresado):
                valor=True
        return valor

    def validar_id_correcto_curso(self,codigo_ingresado):
        lista_curso=self.cursos.get_cursos_all('curso_id')
        valor=False
        for curso in lista_curso:
            if(curso[0]==codigo_ingresado):
                valor=True
        return valor

    def validar_id_correcto_malla_curricular(self,codigo_ingresado):
        lista_mallas_curriculares=self.malla_curricular.get_malla_curricular_all('id_malla')
        valor=False
        for malla in lista_mallas_curriculares:
            if(malla[0]==codigo_ingresado):
                valor=True
        return valor
    def validar_id_correcto_notas(self,codigo_ingresado):
        lista_notas=self.notas.get_nota_all('id_nota')
        valor=False
        for nota in lista_notas:
            if(nota[0]==codigo_ingresado):
                valor=True
        return valor

    def validar_id_correcto_periodo(self,codigo_ingresado):
        periodos=self.periodo.get_periodo_all('id_periodo')
        valor=False
        for periodo in periodos:
            if(periodo[0]==codigo_ingresado):
                valor=True
        return valor

    def validar_id_correcto_profesor_curso(self,codigo_ingresado):
        lista_profesor_curso=self.profesor_cursos.get_profesor_curso_all('id_profesor_curso')
        valor=False
        for prof_cur in lista_profesor_curso:
            if(prof_cur[0]==codigo_ingresado):
                valor=True
        return valor

    def validar_id_correcto_profesor(self,codigo_ingresado):
        periodos=self.profesor.get_profesor_all('profesor_id')
        valor=False
        for periodo in periodos:
            if(periodo[0]==codigo_ingresado):
                valor=True
        return valor


    def validar_id_correcto_salon(self,codigo_ingresado):
        lista_salones=self.salones.get_salones_all('id_salon')
        valor=False
        for salon in lista_salones:
            if(salon[0]==codigo_ingresado):
                valor=True
        return valor



    def validar_periodo_correcto(self,periodo_ingresado):
        periodos=self.periodo.get_periodo_all('id_periodo')
        valor=False
        for periodo in periodos:
            if(periodo_ingresado in periodo[1]):
                valor=True
        return valor

    def validar_nombre_correcto(self,nombre_ingresado):
        alumnos=self.alumno.get_alumno_all('alumno_id')
        valor=False
        for alumno in alumnos:
            if(nombre_ingresado in alumno[1]):
                valor=True
        return valor
    def validar_nombreCurso_correcto(self,nombre_ingresado):
        lista_curso=self.cursos.get_cursos_all('curso_id')
        valor=False
        for curso in lista_curso:
            if(nombre_ingresado in curso[1]):
                valor=True
        return valor
    def validar_nombresalon_correcto(self,nombre_ingresado):
        lista_salones=self.cursos.get_cursos_all('id_salon')
        valor=False
        for salon in lista_salones:
            if(nombre_ingresado in salon[1]):
                valor=True
        return valor
    @staticmethod
    def validar_fecha_inicio( fecha_desde):
        while True:
            try:
                fecha_desde = input("Ingresa la fecha de Inicio de Periodo en el formato YYYY-MM-DD: ")
                datetime.strptime(fecha_desde, '%Y-%m-%d')
                return fecha_desde
            except ValueError:
                print("Fecha inválida")
        
    @staticmethod
    def validar_fecha_fin( fecha_hasta):
        while True:
            try:
                fecha_hasta = input("Ingresa la fecha de Fin de Periodo en el formato YYYY-MM-DD: ")
                datetime.strptime(fecha_hasta, '%Y-%m-%d')
                return fecha_hasta
            except ValueError:
                print("Fecha inválida")
        



    