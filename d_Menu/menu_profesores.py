from c_Controllers.profesor import profesorController
class Menuprofesor:
    def __init__(self):
        self.profesor=profesorController()
        
    def menu_profesor(self):
        while True:
            print('''
                Menú profesor
                1) Listar Todos los profesores.
                2) Listar mediante una condicion
                3) Agregar profesor
                4) Editar profesor
                5) Eliminar profesor
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.profesor.list_profesores()
            elif opcion == '2':
                self.profesor.lista_profesor_multiple_conditions()
            elif opcion == '3':
                self.profesor.insert_profesor_data()
            elif opcion == '4':
                self.profesor.update_profesor()
            elif opcion == '5':
                self.profesor.delete_profesor()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')



