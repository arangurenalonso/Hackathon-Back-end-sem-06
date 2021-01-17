from psycopg2 import connect


class Conection:
    def __init__(self,table_name):
        self.table_name=table_name
        self.db=connect(
            host='127.0.0.1',
            user='postgres',
            password='123456',
            database='sistema_colegio',
            port='5432'
        )
        self.cursor=self.db.cursor()
    
    def execute_query(self,query):
        self.cursor.execute(query)
        self.commit()

    def get_all(self,colum_order):
        query=f'SELECT * FROM {self.table_name} ORDER BY {colum_order}'
        self.cursor.execute(query)
        # fetchall= Devuelve toda la información de la consulta realizada
        #           devuelve la información como una lista de diccionarios [{},{},{}]
        # fetchone= Devuelve un registro de la consulta que acabas de realizar
        #           devuelve la información como un diccionario {}
        # fetchmany= Devuelve un bloque de registros según la consulta realizada
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
    
    def create_condition_where(self,field_key,field_value):
        
        if isinstance(field_value, str):
            if('>' in field_value or '<' in field_value):
                return (f"{field_key} {field_value}")
            else:
                return (f"{field_key} like '%{field_value}%'")
        else:
            return (f"{field_key} = {field_value}")


    def insert(self, data):
        values = "'" + "', '".join(map(str, data.values())) + "'"
        query = f'''
        INSERT INTO {self.table_name} 
        ({", ".join(data.keys())}) VALUES ({values})
        '''
        self.execute_query(query)
        return True

    def update(self, values_to_update, conditions_filter):
        list_update = []
        for field_name, field_value in values_to_update.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_update.append(f"{field_name}={value}")

        list_where = []
        for field_key, field_value in conditions_filter.items():
            list_where.append(self.create_condition_where(field_key,field_value))

        query = f'''
            UPDATE {self.table_name} SET {", ".join(list_update)} 
            WHERE 
            {" AND ".join(list_where)}
        '''
        self.execute_query(query)
        return True

    def delete(self, id_object):
        list_where = []
        for field_key, field_value in id_object.items():
            list_where.append(self.create_condition_where(field_key,field_value))
        
        query = f'''
            DELETE FROM {self.table_name}
            WHERE 
            {" AND ".join(list_where)}
        '''
        self.execute_query(query)
        return True


    def commit(self):
        # El Commit: se utiliza cuando se ejecuta una acción a hacia la base de datos
        #            como: INSERT, UPDATE, DELETE (DDL)
        
        self.db.commit()