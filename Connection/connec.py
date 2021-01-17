from psycopg2 import connect


class Connection:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = connect(host='127.0.0.1',
                    user='postgres', 
                    password='p0o9w3e4lkas', 
                    database='sistema_colegio')
        self.cursor = self.db.cursor()
        
    def execute_query(self, query): # Se usa para ejecutar INSERT, UPDATE, DELETE (DDL)
        self.cursor.execute(query)
        self.commit()

    def get_all(self, order):
        query = f'SELECT * FROM {self.table_name} ORDER BY {order}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, data):
        values = "'" + "', '".join(map(str, data.values())) + "'"
        query = f'INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({values})'
        self.execute_query(query)
        return True

    def update(self, id_object, data):
        list_update = []
        for field_name, field_value in data.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_update.append(f"{field_name}={value}")

        list_where = []
        for field_name, field_value in id_object.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_where.append(f"{field_name}={value}")

        query = f'''
            UPDATE {self.table_name} SET {", ".join(list_update)} 
            WHERE 
            {" AND ".join(list_where)}
        '''
        self.execute_query(query)
        return True

    def delete(self, id_object):
        list_where = []
        for field_name, field_value in id_object.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_where.append(f"{field_name}={value}")

        query = f'''
            DELETE FROM {self.table_name}
            WHERE 
            {" AND ".join(list_where)}
        '''
        self.execute_query(query)
        return True

    def commit(self):
        self.db.commit()
        return True

    def get_by_multiple_condition(self,conditions_filter):
        list_where=[]
        for field_key, field_value in conditions_filter.items():
            list_where.append(self.create_condition_where(field_key,field_value))
        query = f'''
            SELECT 
            * 
            FROM {self.table_name} 
            WHERE {" AND ".join(list_where)}
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_by_one_condition(self,condition_filter):
        query=f'''
        SELECT 
        * 
        FROM {self.table_name} 
        WHERE {"".join(map(str, condition_filter.keys()))} = {"".join(map(str, condition_filter.values()))}
                    '''
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def create_condition_where(self,field_key,field_value):
        
        if isinstance(field_value, str):
            if('>' in field_value or '<' in field_value):
                return (f"{field_key} {field_value}")
            else:
                return (f"{field_key} like '%{field_value}%'")
        else:
            return (f"{field_key} = {field_value}")