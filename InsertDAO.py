  
import mysql.connector


class InsertDAO:
    def __init__(self):
        self.mydb = mysql.connector.connect(user="digsquadadmin@digsquadmysql",
                                  password="digsquad+1",
                                  host="digsquadmysql.mysql.database.azure.com",
                                  port=3306,
                                  database="stub_db")
        self.myCursor = self.mydb.cursor()
        self.table = 'DIG_DEEP'

    def insert(self, columns, value):
        sql = "INSERT INTO {0} ({1}) VALUES {2};".format(self.table, columns.replace("'", ""), value)
        print(sql)
        self.myCursor.execute(sql)
        self.mydb.commit()

def execute_insert(columns, value):
    inserter = InsertDAO()
    inserter.insert(columns, value)

columns = 'USER_ID, AMOUNT, COMPANY_ID, CHARITY_ID'
value1 = '002', '10.67', 'Asda', 'Greenpeace Fund'
value2 = '002', '74734.99', 'DB', 'Earth Justice'
value3 = '003', '1000.15', 'DB', 'WWF'
value4 = '004', '10.15', 'DB', 'Greenpeace Fund'
value5 = '005', '760.15', 'MI5', 'Earth Justice'
value6 = '006', '180.15', 'MI5', 'WWF'
value7 = '007', '1.15', 'MI5', 'Green Peace'

execute_insert(columns, value1)
execute_insert(columns, value2)
execute_insert(columns, value3)
execute_insert(columns, value4)
execute_insert(columns, value5)
execute_insert(columns, value6)
execute_insert(columns, value7)