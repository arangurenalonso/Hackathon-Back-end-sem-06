from Models.alumno import ModelAlumno
from otro.validar import Validacion

class AlumnoController:
    def __init__(self):
        self.alumno=ModelAlumno()
        self.validacion_class=Validacion()

    def list_alumnos(self):
        alumnos=self.alumno.get_alumno_all('nombres')
        texto=''
        for alumno in alumnos:
            texto+=f'''{alumno[0]}  - {alumno[1]}   - {alumno[2]}   - {alumno[3]} \n'''
        print (texto)

    #def list_alumno_condition(self):
    #    id=input('Ingrese el ID a buscar: ')
    #    alumno_condition=self.alumno.get_alumno_one_condition({
    #        'alumno_id':id,
    #        })
    #    print (alumno_condition)

    def lista_alumno_multiple_conditions(self):
        alumno_multiple_condition=self.alumno.get_alumno_by_multiple_condition(self.valores_filtrar())
        texto=''
        for alumno in alumno_multiple_condition:
            texto+=f'''{alumno[0]}  - {alumno[1]}   - {alumno[2]}   - {alumno[3]} \n'''
        print (texto)

    def insert_alumno_data(self):
        nombre=Validacion.validar_texto('Ingrese el nombre del Alumno')
        edad=Validacion.validar_edad('Ingresar la edad del Alumno')
        correo=Validacion.validar_correo('Ingresar el Correo Electrónico del Alumno')
        
        data={
            'nombres':nombre,
            'edad':edad,
            'correo':correo
        }
        self.alumno.insert_alumno(data)
        print('Se creo con exito')  

    def update_alumno(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        nombre=Validacion.validar_texto('Ingrese el NUEVO nombre del Alumno')
        edad=Validacion.validar_edad('Ingresar la NUEVO edad del Alumno')
        correo=Validacion.validar_correo('Ingresar el NUEVO Correo Electrónico del Alumno')
        values_to_update={
            'nombres':nombre,
            'edad':edad,
            'correo':correo
        }
        

        self.alumno.update_alumno(values_to_update, conditions_filter)
        print('Se actualizo con exito')
        
    def delete_alumno(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.alumno.delete_alumno(self.valores_filtrar())
        print('Se elimino con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID',"A")
        if (opcion_ID!=-1):
            diccionario['alumno_id']=opcion_ID
            
        opcion_nombre=self.opcion_filtrar('Desea Filtrar por Nombre',"B")
        if (opcion_nombre!=-1):
            diccionario['nombres']=opcion_nombre
        return diccionario
    
    def opcion_filtrar(self,comentario,valor):
        while(True):
            print(f'''
                   {comentario}?
                    1)Si
                    2)No
                \n''')
            opcionID = input('Ingresa el n° : ')
            if opcionID == '1':
                if(valor=='A'):
                    return self.ingresar_id()
                if(valor=='B'):
                    return self.ingresar_nombre()

            elif opcionID == '2':
                return -1
            else:
                print('No escogiste una opción valida')
    
    def ingresar_nombre(self):
        while(True):
            texto=Validacion.validar_texto('Ingrese el nombre o parte del nombre a buscar')
            if (self.validacion_class.validar_nombre_correcto):
                return texto
            else:
                print('No se encontraron coincidencias')

    def ingresar_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del Alumno : '))
                    if(self.validacion_class.validar_id_correcto_alumno(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
            

        
        
        


    