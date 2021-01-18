from a_conection.conection import Conection

class Model_Malla_Curricular:
    def __init__(self):
        self.model=Conection('malla_curricular')

    def get_malla_curricular_all(self, colum_order):
        return self.model.get_all(colum_order)
         
    def get_malla_curricular_one_condition(self, condition_filter):
        
        return self.model.get_by_one_condition(condition_filter)

    def get_malla_curricular_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)

    def insert_malla_curricular(self,data):
        return self.model.insert(data)

    def update_malla_curricular(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_malla_curricular(self,conditions_filter):
        return self.model.delete(conditions_filter)