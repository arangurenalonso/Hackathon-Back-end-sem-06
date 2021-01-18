from c_Controllers.profesor_curso import ProfesorCursoController
class Menuprofesor_curso:
    def __init__(self):
        self.profesor_curso=ProfesorCursoController()
        
    def menu_profesor_curso(self):
        while True:
            print('''
                Menú Profesor_curso
                1) Listar Todos los Profesor_curso.
                2) Listar mediante una condicion
                3) Agregar Profesor_curso
                4) Editar Profesor_curso
                5) Eliminar Profesor_curso
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.profesor_curso.list_profesor_curso()
            elif opcion == '2':
                self.profesor_curso.lista_profesor_curso_multiple_conditions()
            elif opcion == '3':
                self.profesor_curso.insert_profesor_curso()
            elif opcion == '4':
                self.profesor_curso.update_profesor_curso()
                pass
            elif opcion == '5':
                self.profesor_curso.delete_profesor_curso()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')



