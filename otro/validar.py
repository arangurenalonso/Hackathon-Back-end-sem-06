import re
from models.alumno import ModelAlumno


class Validacion:
    def __init__(self):
        self.alumno=ModelAlumno()
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
    def validar_id_correcto(self,codigo_ingresado):
        alumnos=self.alumno.get_alumno_all('alumno_id')
        valor=False
        for alumno in alumnos:
            if(alumno[0]==codigo_ingresado):
                valor=True
        return valor

    def validar_nombre_correcto(self,nombre_ingresado):
        alumnos=self.alumno.get_alumno_all('alumno_id')
        valor=False
        for alumno in alumnos:
            if(nombre_ingresado in alumno[1]):
                valor=True
        return valor



            