from c_Controllers.curso import CursosController

class MenuCurso:
    def __init__(self):
        self.curso=CursosController()
        
    def menu_Curso(self):
        while True:
            print('''
                Menú Curso
                1) Listar Todos los Curso.
                2) Listar mediante una condicion
                3) Agregar Curso
                4) Editar Curso
                5) Eliminar Curso
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.curso.list_cursos()
            elif opcion == '2':
                self.curso.lista_curso_multiple_conditions()
            elif opcion == '3':
                self.curso.insert_curso_data()
            elif opcion == '4':
                self.curso.update_curso()
            elif opcion == '5':
                self.curso.delete_curso()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')




