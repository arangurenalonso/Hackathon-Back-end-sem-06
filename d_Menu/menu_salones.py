from c_Controllers.salon import SalonesController


class MenuSalones:
    def __init__(self):
        self.salones = SalonesController()
    def menu(self):
        while True:
            print('''
                Menú Salones
                1) Listar salones
                2) Listar Salones por condicion
                3) Agregar salon
                4) Editar Salon
                5) Eliminar Salon
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.salones.list_salones()
            elif opcion == '2':
                self.salones.list_salones_condition()
            elif opcion == '3':
                self.salones.insert_salon_data()
            elif opcion == '4':
                self.salones.update_salon()
            elif opcion == '5':
                self.salones.delete_salon()
            elif opcion =='6':
                break
            else:
                print('No escogiste una opción valida')



