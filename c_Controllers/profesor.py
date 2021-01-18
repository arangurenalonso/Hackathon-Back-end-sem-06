from b_Models.profesor import ModelProfesor
from otro.validar import Validacion

class profesorController:
    def __init__(self):
        self.profesor=ModelProfesor()
        self.validacion_class=Validacion()

    def list_profesores(self):
        profesores=self.profesor.get_profesor_all('nombres')
        texto=''
        for profesor in profesores:
            texto+=f'''{profesor[0]}  - {profesor[1]}   - {profesor[2]}   - {profesor[3]} \n'''
        print (texto)

    #def list_profesor_condition(self):
    #    id=input('Ingrese el ID a buscar: ')
    #    profesor_condition=self.profesor.get_profesor_one_condition({
    #        'profesor_id':id,
    #        })
    #    print (profesor_condition)

    def lista_profesor_multiple_conditions(self):
        profesor_multiple_condition=self.profesor.get_profesor_by_multiple_condition(self.valores_filtrar())
        texto=''
        for profesor in profesor_multiple_condition:
            texto+=f'''{profesor[0]}  - {profesor[1]}   - {profesor[2]}   - {profesor[3]} \n'''
        print (texto)

    def insert_profesor_data(self):
        nombre=Validacion.validar_texto('Ingrese el nombre del profesor')
        edad=Validacion.validar_edad('Ingresar la edad del profesor')
        correo=Validacion.validar_correo('Ingresar el Correo Electrónico del profesor')
        
        data={
            'nombres':nombre,
            'edad':edad,
            'correo':correo
        }
        self.profesor.insert_profesor(data)
        print('Se creo con exito')  

    def update_profesor(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        nombre=Validacion.validar_texto('Ingrese el NUEVO nombre del profesor')
        edad=Validacion.validar_edad('Ingresar la NUEVO edad del profesor')
        correo=Validacion.validar_correo('Ingresar el NUEVO Correo Electrónico del profesor')
        values_to_update={
            'nombres':nombre,
            'edad':edad,
            'correo':correo
        }
        

        self.profesor.update_profesor(values_to_update, conditions_filter)
        print('Se actualizo con exito')
        
    def delete_profesor(self):
        print('''
                ingrese el ID del profesor que desea eliminar:
            \n''')
        self.profesor.delete_profesor(self.valores_filtrar())
        print('Se elimino con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID',"A")
        if (opcion_ID!=-1):
            diccionario['profesor_id']=opcion_ID
            
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
                    opcion = int(input('Ingresa el ID del profesor : '))
                    if(self.validacion_class.validar_id_correcto_profesore(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
            

        
        
        


    