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

def execute_insert():
    inserter = InsertDAO()

    columns = 'USER_ID, AMOUNT, COMPANY_ID, CHARITY_ID'
    value = '007', '1000.15', 'MI5', 'WWF'

    inserter.insert(columns, value)

execute_insert()
