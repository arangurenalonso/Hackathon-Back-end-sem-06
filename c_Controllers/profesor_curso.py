from b_Models.profesor_curso import Model_Profesor_Curso
from otro.validar import Validacion

class ProfesorCursoController:
    def __init__(self):
        self.profesor_curso=Model_Profesor_Curso()
        self.validacion_class=Validacion()

    def list_profesor_curso(self):
        profesor_curso=self.profesor_curso.get_profesor_curso_all('id_profesor_curso')
        texto=''
        for prof_cur in profesor_curso:
            texto+=f'''{prof_cur[0]}  - {prof_cur[1]}   - {prof_cur[2]}\n'''
        print (texto)

    #def list_alumno_condition(self):
    #    id=input('Ingrese el ID a buscar: ')
    #    alumno_condition=self.alumno.get_alumno_one_condition({
    #        'alumno_id':id,
    #        })
    #    print (alumno_condition)

    def lista_profesor_curso_multiple_conditions(self):
        profesor_curso_multiple_condition=self.profesor_curso.get_profesor_curso_by_multiple_condition(self.valores_filtrar())
        texto=''
        for prof_cur in profesor_curso_multiple_condition:
            texto+=f'''{prof_cur[0]}  - {prof_cur[1]}   - {prof_cur[2]}\n'''
        print (texto) 

    def insert_profesor_curso(self):
        id_profesor=self.ingresar_profesor_id()
        id_curso=self.ingresar_curso_id()
        
        
        data={
            'id_profesor':id_profesor,
            'id_curso':id_curso,
        }
        self.profesor_curso.insert_profesor_curso(data)
        print('Se creo con exito')  

    def update_profesor_curso(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        id_profesor=self.ingresar_profesor_id()
        id_curso=self.ingresar_curso_id()
        
        
        values_to_update={
            'id_profesor':id_profesor,
            'id_curso':id_curso,
        }
        

        self.profesor_curso.update_profesor_curso(values_to_update, conditions_filter)
        print('Se actualizo con exito')
        
    def delete_profesor_curso(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.profesor_curso.delete_profesor_curso(self.valores_filtrar())
        print('Se elimino con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID',"A")
        if (opcion_ID!=-1):
            diccionario['id_profesor_curso']=opcion_ID
        opcion_ID=self.opcion_filtrar('Desea Filtrar por Profesor',"B")
        if (opcion_ID!=-1):
            diccionario['id_profesor']=opcion_ID
        opcion_ID=self.opcion_filtrar('Desea Filtrar por Curso',"C")
        if (opcion_ID!=-1):
            diccionario['id_curso']=opcion_ID   
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
                    return self.ingresar_profesor_curso_id()
                if(valor=='B'):
                    return self.ingresar_profesor_id()
                if(valor=='C'):
                    return self.ingresar_curso_id()

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

    def ingresar_profesor_curso_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del registro profesor_curso que desea buscar : '))
                    if(self.validacion_class.validar_id_correcto_profesor_curso(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
    
    def ingresar_profesor_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del Profesor: '))
                    if(self.validacion_class.validar_id_correcto_profesor(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
    
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
            

        
        
        


    