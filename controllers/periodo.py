from Models.periodo import ModelPeriodo
from otro.validar import Validacion

class PeriodoController:
    def __init__(self):
        self.periodo=ModelPeriodo()
        self.validacion_class=Validacion()

    def list_periodos(self):
        Periodos=self.periodo.get_periodo_all('nombre_periodo')
        texto=''
        for periodo in Periodos:
            texto+=f'''{periodo[0]}  - {periodo[1]}   - {periodo[2]}   - {periodo[3]} \n'''
        print (texto)

    def lista_periodo_multiple_conditions(self):
        periodo_multiple_condition=self.periodo.get_periodo_by_multiple_condition(self.valores_filtrar())
        texto=''
        for periodo in periodo_multiple_condition:
            texto+=f'''{periodo[0]}  - {periodo[1]}   - {periodo[2]}   - {periodo[3]} \n'''
        print (texto)

    def insert_periodo_data(self):
        nombre_periodo = Validacion.validar_texto('Ingrese el periodo escolar')
        fecha_desde = Validacion.validar_fecha_inicio('Ingresar fecha de inicio del periodo escolar')
        fecha_hasta = Validacion.validar_fecha_fin('Ingresar fecha de fin del periodo escolar')
        
        data={
            'nombre_periodo':nombre_periodo,
            'fecha_desde':fecha_desde,
            'fecha_hasta':fecha_hasta
        }
        self.periodo.insert_periodo(data)
        print('Se creo con exito')  

    def update_periodo(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        nombre_periodo=Validacion.validar_texto('Ingrese el nuevo periodo escolar')
        fecha_desde=Validacion.validar_fecha_inicio('Ingrese la nueva fecha de inicio del periodo')
        fecha_hasta=Validacion.validar_fecha_fin('Ingrese la nueva fecha de fin del periodo')
        values_to_update={
            'nombre_periodo':nombre_periodo,
            'fecha_desde':fecha_desde,
            'fecha_hasta':fecha_hasta
        }

        self.periodo.update_periodo(values_to_update, conditions_filter)
        print('Se actualizó con exito')
        
    def delete_periodo(self):
        print('''
                ingrese el ID del periodo que desea eliminar:
            \n''')
        self.periodo.delete_periodo(self.valores_filtrar())
        print('Se eliminó con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID',"A")
        if (opcion_ID!=-1):
            diccionario['id_periodo']=opcion_ID
            
        opcion_periodo=self.opcion_filtrar('Desea Filtrar por Nombre de periodo',"B")
        if (opcion_periodo!=-1):
            diccionario['nombre_periodo']=opcion_periodo
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
                    return self.ingresar_nombre_periodo()

            elif opcionID == '2':
                return -1
            else:
                print('No escogiste una opción valida')
    
    def ingresar_nombre_periodo(self):
        while(True):
            texto=Validacion.validar_texto('Ingrese el nombre del periodo o parte del nombre del periodo a buscar')
            if (self.validacion_class.validar_periodo_correcto):
                return texto
            else:
                print('No se encontraron coincidencias')

    def ingresar_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del periodo escolar : '))
                    if(self.validacion_class.validar_id_correcto_periodo(opcion)):
                        return opcion 
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
            

        
        
        


    