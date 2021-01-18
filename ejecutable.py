from d_Menu.menu_salones import MenuSalones
from d_Menu.alumno_menu import MenuAlumno
from d_Menu.curso_menu import MenuCurso
from d_Menu.menu_profesores import Menuprofesor
from d_Menu.menu_periodo import MenuPeriodo
from d_Menu.menu_profesor_curso import Menuprofesor_curso
from d_Menu.malla_curricular_menu import MenuMallaCurricular
from d_Menu.notas_menu import MenuNotas

class Inicio:

    def menu(self):
        while True:
            print('''
                Menú:

                1) Ir a -> ALUMNO
                2) Ir a -> CURSO 
                3) Ir a -> DOCENTE
                4) Ir a -> PERIODO
                5) Ir a -> SALONES
                6) Ir a -> Asignacion de profesor a Curso
                7) Ir a -> Malla Curricular
                8) Ir a -> Notas
                9) SALIR
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                alumno = MenuAlumno()
                alumno.menu_Alumno()
            elif opcion == '2':
                menuCurso=MenuCurso()
                menuCurso.menu_Curso()
            elif opcion == '3':
                menuprofesor=Menuprofesor()
                menuprofesor.menu_profesor()
            elif opcion == '4':
                menuPeriodo=MenuPeriodo()
                menuPeriodo.menu_Periodo()
            elif opcion == '5':
                inicio_salones = MenuSalones()
                inicio_salones.menu()
            elif opcion == '6':
                Menuprofesor_curso=Menuprofesor_curso()
                Menuprofesor_curso.menu_profesor_curso()  
            elif opcion =='7':
                malla=MenuMallaCurricular()
                malla.menu_malla_curricular()
            elif opcion =='8':
                nota=MenuNotas()
                nota.menu_nota()
            elif opcion == '9':
                break
            else:
                print('No escogiste una opción valida')
    


inicio_objecto = Inicio()
inicio_objecto.menu()