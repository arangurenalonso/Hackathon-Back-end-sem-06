from Controllers.periodo import PeriodoController


class MenuPeriodo:
    def __init__(self):
        self.periodo=PeriodoController()
        
    def menu_Periodo(self):
        while True:
            print('''
                Menú Periodo Escolar
                1) Listar Todos los Periodos.
                2) Listar mediante una condicion
                3) Agregar Periodo Escolar
                4) Editar Periodo Escolar
                5) Eliminar Periodo Escolar
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.periodo.list_periodos()
            elif opcion == '2':
                self.periodo.lista_periodo_multiple_conditions()
            elif opcion == '3':
                self.periodo.insert_periodo_data()
            elif opcion == '4':
                self.periodo.update_periodo()
            elif opcion == '5':
                self.periodo.delete_periodo()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')

MenuPeriodo=MenuPeriodo()
MenuPeriodo.menu_Periodo()