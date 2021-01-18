from a_conection.conection import Conection

class Model_Profesor_Curso:
    def __init__(self):
        self.model=Conection('profesor_curso')

    def get_profesor_curso_all(self, colum_order):
        return self.model.get_all(colum_order)
         
    def get_profesor_curso_one_condition(self, condition_filter):
        
        return self.model.get_by_one_condition(condition_filter)

    def get_profesor_curso_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)

    def insert_profesor_curso(self,data):
        return self.model.insert(data)

    def update_profesor_curso(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_profesor_curso(self,conditions_filter):
        return self.model.delete(conditions_filter)