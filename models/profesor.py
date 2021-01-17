from conection.conection import Conection

class ModelProfesor:
    def __init__(self):
        self.model=Conection('profesores')

    def get_profesor_all(self, colum_order):
        return self.model.get_all(colum_order)
         
    def get_profesor_one_condition(self, condition_filter):
        return self.model.get_by_one_condition(condition_filter)

    def get_profesor_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)

    def insert_mobile(self, data):
        return self.model.insert(data)

    def insert_profesor(self,data):
        return self.model.insert(data)

    def update_profesor(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_profesor(self,conditions_filter):
        return self.model.delete(conditions_filter)