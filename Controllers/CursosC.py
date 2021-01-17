from Models.CursosM import model_cursos

class CursoController:
    def __init__(self):
        self.curso=model_cursos()
        

    def lista_cursos(self):
        cursos=self.curso.get_cursos_all('nombres')
        texto=''
        for curso in cursos:
            texto+=f'''{curso[0]}  - {curso[1]}   - {curso[2]}   - {curso[3]} \n'''
        print (texto)
    
    def lista_alumno_multiple_conditions(self):
        curso_multiple_condition=self.curso.get_curso_by_multiple_condition(self.valores_filtrar())
        texto=''
        for curso in curso_multiple_condition:
            texto+=f'''{curso[0]}  - {curso[1]}   - {curso[2]}   - {curso[3]} \n'''
        print (texto)

    def insert_curso_data(self):
        nombre= str(input(('Ingrese el nombre del Alumno')))
        edad= input(('Ingresar la edad del Alumno'))
        correo= str(input(('Ingresar el Correo Electrónico del Alumno')))
        
        data={
            'nombres':nombre,
            'edad':edad,
            'correo':correo
        }
        self.curso.insert_curso(data)
        print('Se creo con exito')  

    def update_curso(self):
        
        print('''
                ingrese los campos que desea editar:
                \n''')
        conditions_filter=self.data()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        nombre=str(input(('Ingrese el NUEVO nombre del Alumno')))
        edad=input(('Ingresar la NUEVO edad del Alumno'))
        correo=str(input(('Ingresar el NUEVO Correo Electrónico del Alumno')))
        values_to_update={
            'nombres':nombre,
            'edad':edad,
            'correo':correo
        }
        

        self.curso.update_alumno(values_to_update, conditions_filter)
        print('Se actualizo con exito')
    
    def delete_alumno(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.curso.delete_curso(self.valores_filtrar())
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
            texto= str(input('Ingrese el nombre o parte del nombre a buscar'))
            cursos =self.curso.get_alumno_all('curso_id')
            for texto in cursos:
            if(nombre_ingresado in alumno[1]):
                valor=True
                return texto
            else
            print('Valor Incorrecto')

    def ingresar_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del Alumno : '))
                    if(self.validacion_class.validar_id_correcto(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
