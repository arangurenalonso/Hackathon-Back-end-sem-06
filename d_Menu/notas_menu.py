from c_Controllers.notas import MallaNotas
class MenuNotas:
    def __init__(self):
        self.notas=MallaNotas()
        
    def menu_nota(self):
        while True:
            print('''
                Menú Notas
                1) Listar Todos los notas de los alumnos.
                2) Listar mediante una condicion
                3) Agregar nota
                4) Editar nota
                5) Eliminar nota
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.notas.list_nota()
            elif opcion == '2':
                self.notas.lista_nota_multiple_conditions()
            elif opcion == '3':
                self.notas.insert_nota()
            elif opcion == '4':
                self.notas.update_nota()
                pass
            elif opcion == '5':
                self.notas.delete_nota()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')



