from a_conection.conection import Conection

class Notas:
    def __init__(self):
        self.model = Conection('notas')

    def get_nota_all(self, order):
        return self.model.get_all(order)

    def get_nota(self, id_object):
        return self.model.get_by_one_condition(id_object)

    def get_nota_multiple_condition(self, id_object):
        return self.model.get_by_multiple_condition(id_object)

    def insert_nota(self, data):
        return self.model.insert(data)

    def update_nota(self, id_object, data):
        return self.model.update(id_object, data)
    
    def delete_nota(self, id_object):
        return self.model.delete(id_object)

