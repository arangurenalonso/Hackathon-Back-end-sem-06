from controllers.salon import SalonesController
salones = SalonesController()

class MenuSalones:
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
                salones.list_salones()
                break
            elif opcion == '2':
                salones.list_salones_condition()
                break
            elif opcion == '3':
                #salon_nuevo = input('Ingrese nuevo salon: ')
                #salones.insert_salon(f'{"nombre_salon" : salon_nuevo}')
                salones.insert_salon({"nombre_salon" : "4A"})
                break
            elif opcion == '4':
                salones.update_salon({
                    "id_salon" : 9
                    },{
                    "nombre_salon" : "4L"
                    })
                break
            elif opcion == '5':
                salones.delete_salon({
                    "id_salon" : 10
                    })
                break
            else:
                print('No escogiste una opción valida')

    # def agregar(self):
        
    #     aa=array_alumno()
    #     codigo=aa.codigo_correlativo()
    #     nombre=Validacion.validar_texto('Ingrese el nombre del Alumno')
    #     apellido=Validacion.validar_texto('Ingrese el Apellido del Alumno')
    #     dni=Validacion.validar_dni('Ingresar el DNI del Alumno')
    #     edad=Validacion.validar_edad('Ingresar la edad del Alumno')
    #     aa.agregar(Alumno(codigo,nombre,apellido,dni,edad))
    #     self.menu()

    # def eliminar(self):
    #     Validacion.validar_codigo('alumno')
    #     self.menu()