from a_conection.conection import Conection

class ModelAlumno:
    def __init__(self):
        self.model=Conection('alumnos')

    def get_alumno_all(self, colum_order):
        return self.model.get_all(colum_order)
         
    def get_alumno_one_condition(self, condition_filter):
        return self.model.get_by_one_condition(condition_filter)

    def get_alumno_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)

    def insert_mobile(self, data):
        return self.model.insert(data)

    def insert_alumno(self,data):
        return self.model.insert(data)

    def update_alumno(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_alumno(self,conditions_filter):
        return self.model.delete(conditions_filter)