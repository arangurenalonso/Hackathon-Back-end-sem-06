from Connection.connec import Connection

class model_cursos:
    def __init__(self):
        self.model = Connection('cursos')

    def get_cursos_all(self, order):
        return self.model.get_all(order)
    
    def get_curso_one_condition(self, condition_filter):
        return self.model.get_by_one_condition(condition_filter)

    def get_curso_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)

    def insert_curso(self, data):
        return self.model.insert(data)

    def update_curso(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_curso(self, id_object):
        return self.model.delete(id_object)

    