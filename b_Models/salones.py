from a_conection.conection import Conection

class Salones:
    def __init__(self):
        self.model = Conection('salones')

    def get_salones_all(self, order):
        return self.model.get_all(order)

    def get_salon(self, id_object):
        return self.model.get_by_one_condition(id_object)

    def get_salones_multiple_condition(self, id_object):
        return self.model.get_by_multiple_condition(id_object)

    def insert_salon(self, data):
        return self.model.insert(data)

    def update_salon(self, id_object, data):
        return self.model.update(id_object, data)
    
    def delete_salon(self, id_object):
        return self.model.delete(id_object)

