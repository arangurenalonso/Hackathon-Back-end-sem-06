from b_Models.curso import ModelCurso
from otro.validar import Validacion

class CursosController:
    def __init__(self):
        self.curso=ModelCurso()
        self.validacion_class=Validacion()

    def list_cursos(self):
        cursos=self.curso.get_cursos_all('nombre')
        texto=''
        for curso in cursos:
            texto+=f'''{curso[0]}  - {curso[1]} \n'''
        print (texto)

    #def list_alumno_condition(self):
    #    id=input('Ingrese el ID a buscar: ')
    #    alumno_condition=self.alumno.get_alumno_one_condition({
    #        'alumno_id':id,
    #        })
    #    print (alumno_condition)

    def lista_curso_multiple_conditions(self):
        curso_multiple_condition=self.curso.get_curso_by_multiple_condition(self.valores_filtrar())
        texto=''
        for curso in curso_multiple_condition:
            texto+=f'''{curso[0]}  - {curso[1]} \n'''
        print (texto)

    def insert_curso_data(self):
        nombre=Validacion.validar_texto('Ingrese el nombre del Curso')
                
        data={
            'nombre':nombre,
        }
        self.curso.insert_curso(data)
        print('Se creo con exito')   

    def update_curso(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        nombre=Validacion.validar_texto('Ingrese el NUEVO nombre del Curso')
        values_to_update={
            'nombre':nombre,
        }
        

        self.curso.update_curso(values_to_update, conditions_filter)
        print('Se actualizo con exito')
        
    def delete_curso(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.curso.delete_curso(self.valores_filtrar())
        print('Se elimino con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID',"A")
        if (opcion_ID!=-1):
            diccionario['curso_id']=opcion_ID
            
        opcion_nombre=self.opcion_filtrar('Desea Filtrar por Nombre',"B")
        if (opcion_nombre!=-1):
            diccionario['nombre']=opcion_nombre
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
                    return self.ingresar_curso_id()
                if(valor=='B'):
                    return self.ingresar_nombre_curso()

            elif opcionID == '2':
                return -1
            else:
                print('No escogiste una opción valida')
    
    def ingresar_nombre_curso(self):
        while(True):
            texto=Validacion.validar_texto('Ingrese el nombre o parte del nombre a buscar')
            if (self.validacion_class.validar_nombreCurso_correcto):
                return texto
            else:
                print('No se encontraron coincidencias')

    def ingresar_curso_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del Curso: '))
                    if(self.validacion_class.validar_id_correcto_curso(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
            

        
        
        


    