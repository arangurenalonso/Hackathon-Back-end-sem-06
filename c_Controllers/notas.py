from b_Models.notas import Notas
from otro.validar import Validacion

class MallaNotas:
    def __init__(self):
        self.notas=Notas()
        self.validacion_class=Validacion()

    def list_nota(self):
        lista_notas=self.notas.get_nota_all('id_nota')
        texto=''
        for nota in lista_notas:
            texto+=f'''{nota[0]}  - {nota[1]}   - {nota[2]} - {nota[3]}\n'''
        print (texto)

    #def list_alumno_condition(self):
    #    id=input('Ingrese el ID a buscar: ')
    #    alumno_condition=self.alumno.get_alumno_one_condition({
    #        'alumno_id':id,
    #        })
    #    print (alumno_condition)

    def lista_nota_multiple_conditions(self):
        lista_notas=self.notas.get_nota_multiple_condition(self.valores_filtrar())
        texto=''
        for nota in lista_notas:
            texto+=f'''{nota[0]}  - {nota[1]}   - {nota[2]} - {nota[3]}\n'''
        print (texto)

    def insert_nota(self):
        id_alumno=self.ingresar_alumno_id()
        id_malla_curricular=self.ingresar_malla_curricular_id()
        nota=self.validacion_class.validar_nota()
        
        
        
        data={
            'id_alumno':id_alumno,
            'id_malla':id_malla_curricular,
            'nota':nota
            }
        self.notas.insert_nota(data)
        print('Se creo con exito')  

    def update_nota(self):
        
        print('''
                ingrese los campos que desea editar:
            \n''')
        conditions_filter=self.valores_filtrar()

        print('''
                ingrese los nuevos valores del registro a EDITAR:
            \n''')
                
        id_alumno=self.ingresar_alumno_id()
        id_malla_curricular=self.ingresar_malla_curricular_id()
        nota=self.validacion_class.validar_nota()
        values_to_update={
            'id_alumno':id_alumno,
            'id_malla':id_malla_curricular,
            'nota':nota
            }
        self.notas.update_nota(values_to_update, conditions_filter)
        print('Se actualizo con exito')
        
    def delete_nota(self):
        print('''
                ingrese el ID del alumno que desea eliminar:
            \n''')
        self.notas.delete_nota(self.valores_filtrar())
        print('Se elimino con exito')
        
       
    def valores_filtrar(self):
        diccionario={}
        opcion_ID=self.opcion_filtrar('Desea Filtrar por ID del registro de nota',"A")
        if (opcion_ID!=-1):
            diccionario['id_nota']=opcion_ID

        opcion_ID=self.opcion_filtrar('Desea Filtrar por id_alumno',"B")
        if (opcion_ID!=-1):
            diccionario['id_alumno']=opcion_ID

        opcion_ID=self.opcion_filtrar('Desea Filtrar por id_malla_Curricular',"C")
        if (opcion_ID!=-1):
            diccionario['id_malla']=opcion_ID     
        
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
                    return self.ingresar_nota_id()
                if(valor=='B'):
                    return self.ingresar_alumno_id()
                if(valor=='C'):
                    return self.ingresar_malla_curricular_id()

            elif opcionID == '2':
                return -1
            else:
                print('No escogiste una opción valida')
    

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

    def ingresar_alumno_id(self):
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

    def ingresar_nota_id(self):
        while(True):
            try:
                while(True): 
                    opcion = int(input('Ingresa el ID del registro de nota : '))
                    if(self.validacion_class.validar_id_correcto_notas(opcion)):
                        return opcion
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')

        
        
        


    