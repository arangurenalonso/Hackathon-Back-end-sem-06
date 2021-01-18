from a_conection.conection import Conection

class ModelCurso:
    def __init__(self):
        self.model=Conection('cursos')

    def get_cursos_all(self, colum_order):
        return self.model.get_all(colum_order)
         
    def get_curso_one_condition(self, condition_filter):
        return self.model.get_by_one_condition(condition_filter)

    def get_curso_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)

    def insert_curso(self, data):
        return self.model.insert(data)

    def update_curso(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_curso(self,conditions_filter):
        return self.model.delete(conditions_filter)