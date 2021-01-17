from connection.conn import Connection

class Salones:
    def __init__(self):
        self.model = Connection('salones')

    def get_salones_all(self, order):
        return self.model.get_all(order)

    def get_salon(self, id_object):
        return self.model.get_by_id(id_object)

    def get_salones_columns(self, id_object):
        return self.model.get_columns(id_object)

    def insert_salon(self, data):
        return self.model.insert(data)

    def update_salon(self, id_object, data):
        return self.model.update(id_object, data)
    
    def delete_salon(self, id_object):
        return self.model.delete(id_object)