from b_Models.malla_curricular import Model_Malla_Curricular
from otro.validar import Validacion

class MallaCurricularController:
    def __init__(self):
        self.malla_curricular=Model_Malla_Curricular()
        self.validacion_class=Validacion()

    def list_malla_curricular(self):
        lista_mallas_curriculares=self.malla_curricular.get_malla_curricular_all('id_malla')
        texto=''
        for malla_curricular in lista_mallas_curriculares:
            texto+=f'''{malla_curricular[0]}  - {malla_curricular[1]}   - {malla_curricular[2]} - {malla_curricular[3]}\n'''
        print (texto)

    #def list_alumno_condition(self):
    #    id=input('Ingrese el ID a buscar: ')
    #    alumno_condition=self.alumno.get_alumno_one_condition({
    #        'alumno_id':id,
    #        })
    #    print (alumno_condition)

    def lista_malla_curricular_multiple_conditions(self):
        lista_mallas_curriculares=self.malla_curricular.get_malla_curricular_by_multiple_condition(self.valores_filtrar())
        texto=''
        for malla_curricular in lista_mallas_curriculares:
            texto+=f'''{malla_curricular[0]}  - {malla_curricular[1]}   - {malla_curricular[2]} - {malla_curricular[3]}\n'''
        print (texto)

    def insert_malla_curricular(self):
        id_periodo=self.ingresar_periodo_id()
        id_salon=self.ingresar_salon_id()
        id_profeso_cursor=self.ingresar_profesor_curso_id()
        
        
        data={
            'id_periodo':id_periodo,
            'id_salon':id_salon,
            'id_profesor_curso':id_profeso_cursor,
            }
        self.malla_curricular.insert_malla_curricular(data)
        print('Se creo con exito')  

    def update_malla_curricular(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
        id_periodo=self.ingresar_periodo_id()
        id_salon=self.ingresar_salon_id()
        id_profeso_cursor=self.ingresar_profesor_curso_id()
        
        
        values_to_update={
            'id_periodo':id_periodo,
            'id_salon':id_salon,
            'id_profesor_curso':id_profeso_cursor,
            }
        

        self.malla_curricular.update_malla_curricular(values_to_update, conditions_filter)
        print('Se actualizo con exito')
        
    def delete_malla_curricular(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.malla_curricular.delete_malla_curricular(self.valores_filtrar())
        print('Se elimino con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID de malla curricular',"A")
        if (opcion_ID!=-1):
            diccionario['id_malla']=opcion_ID

        opcion_ID=self.opcion_filtrar('Desea Filtrar por periodo',"B")
        if (opcion_ID!=-1):
            diccionario['id_periodo']=opcion_ID

        opcion_ID=self.opcion_filtrar('Desea Filtrar por Salon',"C")
        if (opcion_ID!=-1):
            diccionario['id_salon']=opcion_ID   
        
        opcion_ID=self.opcion_filtrar('Desea Filtrar por profesor_curso',"D")
        if (opcion_ID!=-1):
            diccionario['id_profesor_curso']=opcion_ID   
        
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
                    return self.ingresar_malla_curricular_id()
                if(valor=='B'):
                    return self.ingresar_periodo_id()
                if(valor=='C'):
                    return self.ingresar_salon_id()
                if(valor=='D'):
                    return self.ingresar_profesor_curso_id()

            elif opcionID == '2':
                return -1
            else:
                print('No escogiste una opción valida')
    
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
    def ingresar_periodo_id(self):
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

    def ingresar_malla_curricular_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID de la malla curricular : '))
                    if(self.validacion_class.validar_id_correcto_malla_curricular(opcion)):
                        return opcion 
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')

            

        
        
        


    