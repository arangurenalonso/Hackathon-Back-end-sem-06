from conection.conection import Conection

class ModelPeriodo:
    def __init__(self):
        self.model=Conection('periodo_escolar')

    def get_periodo_all(self, colum_order):
        return self.model.get_all(colum_order)
         
    def get_periodo_one_condition(self, condition_filter):
        return self.model.get_by_one_condition(condition_filter)

    def get_periodo_by_multiple_condition(self, condition_filter):
        return self.model.get_by_multiple_condition(condition_filter)
    #revisar mobile
    def insert_mobile(self, data):
        return self.model.insert(data)

    def insert_periodo(self,data):
        return self.model.insert(data)

    def update_periodo(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_periodo(self,conditions_filter):
        return self.model.delete(conditions_filter)