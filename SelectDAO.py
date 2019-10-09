import mysql.connector
import json


class SelectDAO:
    def __init__(self):
        self.mydb = mysql.connector.connect(user="digsquadadmin@digsquadmysql",
                                            password="digsquad+1",
                                            host="digsquadmysql.mysql.database.azure.com",
                                            port=3306,
                                            database="stub_db")
        self.myCursor = self.mydb.cursor()
        self.table = 'DIG_DEEP'

    def select_all(self, table):
        sql = 'SELECT * FROM {0}'.format(table)
        self.myCursor.execute(sql)
        return json.dumps(self.myCursor.fetchall())

def execute_select():
    selector = SelectDAO()
    return selector.select_all(selector.table)

print(execute_select())