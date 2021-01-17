from Controllers.salon import SalonesController


class MenuSalones:
    def __init__(self):
        self.salones = SalonesController()
    def menu(self):
        while True:
            print('''
                Menú Alumno
                1) Listar salones
                2) Ver salones por ID
                3) Agregar salon
                4) Editar Salon
                5) Eliminar Salon
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.salones.list_salones()
                break
            elif opcion == '2':
                self.salones.list_salones_condition()
                break
            elif opcion == '3':
                #salon_nuevo = input('Ingrese nuevo salon: ')
                #salones.insert_salon(f'{"nombre_salon" : salon_nuevo}')
                self.salones.insert_salon({"nombre_salon" : "4A"})
                break
            elif opcion == '4':
                self.salones.update_salon({
                    "id_salon" : 9
                    },{
                    "nombre_salon" : "4L"
                    })
                break
            elif opcion == '5':
                self.salones.delete_salon({
                    "id_salon" : 10
                    })
                break
            else:
                print('No escogiste una opción valida')



inicio_salones = MenuSalones()
inicio_salones.menu()