from Controllers.CursosC import CursoController

class MenuCurso:
    def __init__(self):
        self.curso = CursoController

    def Menu_Curso(self):
            print('''
                Menú Alumno
                1) Listar Todos los cursos.
                2) Listar mediante una condicion
                3) Agregar curso
                4) Editar curso
                5) Eliminar curso
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.curso.lista_cursos()
            elif opcion == '2':
                self.alumno.lista_alumno_multiple_conditions()
            elif opcion == '3':
                self.alumno.insert_alumno_data()
            elif opcion == '4':
                self.alumno.update_alumno()
            elif opcion == '5':
                self.alumno.delete_alumno()
            elif opcion == '6':
                break
            else:
                print('No escogiste una opción valida')


MenuCurso=MenuCurso()
MenuCurso.Menu_Curso()
