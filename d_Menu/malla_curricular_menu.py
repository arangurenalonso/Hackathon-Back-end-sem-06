from c_Controllers.malla_curricular import MallaCurricularController
class MenuMallaCurricular:
    def __init__(self):
        self.malla_curricular=MallaCurricularController()
        
    def menu_malla_curricular(self):
        while True:
            print('''
                Menú Malla Curricular
                1) Listar Todos las mallas Curricular.
                2) Listar mediante una condicion
                3) Agregar Curricular
                4) Editar Curricular
                5) Eliminar Curricular
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.malla_curricular.list_malla_curricular()
            elif opcion == '2':
                self.malla_curricular.lista_malla_curricular_multiple_conditions()
            elif opcion == '3':
                self.malla_curricular.insert_malla_curricular()
            elif opcion == '4':
                self.malla_curricular.update_malla_curricular()
                pass
            elif opcion == '5':
                self.malla_curricular.delete_malla_curricular()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')



