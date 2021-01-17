from Controllers.alumno import AlumnoController
class MenuAlumno:
    def __init__(self):
        self.alumno=AlumnoController()
        
    def menu_Alumno(self):
        while True:
            print('''
                Menú Alumno
                1) Listar Todos los alumnos.
                2) Listar mediante una condicion
                3) Agregar Alumno
                4) Editar Alumno
                5) Eliminar Alumno
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.alumno.list_alumnos()
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


MenuAlumno=MenuAlumno()
MenuAlumno.menu_Alumno()
