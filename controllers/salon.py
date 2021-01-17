from lista_salones.salones import Salones

class SalonesController:
    def __init__(self):
        self.salones = Salones()

    def list_salones(self):
        salones = self.salones.get_salones_all('id_salon')
        print(salones)

    def list_salones_condition(self):
        id_salon = int(input('Ingrese el ID del salon a buscar :'))
        un_salon = self.salones.get_salon({'id_salon' : id_salon})
        print(un_salon)

    def list_salones_columns(self):
        salones = self.salones.get_salones_columns({
            'id_salon' : 1,
            'nombre_salon' : '1A'
        })
        print(salones)
    
    def insert_salon(self,data):
        self.salones.insert_salon(data)
        print('Se creo con exito salon')
        return True

    def update_salon(self, id_object, data):
        self.salones.update_salon(id_object, data)
        print('Se actualizo con exito')
        return True

    def delete_salon(self, id_object):
        self.salones.delete_salon(id_object)
        print('Se elimino con exito')
        return True