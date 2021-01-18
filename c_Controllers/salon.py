from b_Models.salones import Salones
from otro.validar import Validacion

class SalonesController:
    def __init__(self):
        self.salones = Salones()
        self.validacion_class=Validacion()

    def list_salones(self):
        lista_salones = self.salones.get_salones_all('id_salon')
        texto=''
        for salon in lista_salones:
            texto+=f'''{salon[0]}  - {salon[1]} \n'''
        print (texto)
 
    def list_salones_condition(self):
        lista_salones=self.salones.get_salones_multiple_condition(self.valores_filtrar())
        texto=''
        for salon in lista_salones:
            texto+=f'''{salon[0]}  - {salon[1]} \n'''
        print (texto)

    def insert_salon_data(self):
        nombre=Validacion.validar_texto('Ingrese el nombre del Curso')
                
        data={
            'nombre_salon':nombre,
        }
        self.salones.insert_salon(data)
        print('Se creo con exito') 

    def update_salon(self):
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        nombre=Validacion.validar_texto('Ingrese el NUEVO nombre del Curso')
        values_to_update={
            'nombre_salon':nombre,
        }
        

        self.salones.update_salon(values_to_update, conditions_filter)
        print('Se actualizo con exito')

    def delete_salon(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.salones.delete_salon(self.valores_filtrar())
        print('Se elimino con exito')

##############################################################################################
##############################################################################################
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID del salon',"A")
        if (opcion_ID!=-1):
            diccionario['id_salon']=opcion_ID
            
        opcion_nombre=self.opcion_filtrar('Desea Filtrar por Nombre del Salon',"B")
        if (opcion_nombre!=-1):
            diccionario['nombre_salon']=opcion_nombre
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
                    return self.ingresar_salon_id()
                if(valor=='B'):
                    return self.ingresar_nombre_salon()

            elif opcionID == '2':
                return -1
            else:
                print('No escogiste una opción valida')
    
    def ingresar_nombre_salon(self):
        while(True):
            texto=Validacion.validar_texto('Ingrese el nombre o parte del nombre a buscar')
            if (self.validacion_class.validar_nombresalon_correcto):
                return texto
            else:
                print('No se encontraron coincidencias')

    def ingresar_salon_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del Salon: '))
                    if(self.validacion_class.validar_id_correcto_salon(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')