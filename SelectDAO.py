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

    def select_user(self, user):
        sql = 'SELECT * FROM {0} WHERE USER_ID={1}'.format(self.table, user)
        self.myCursor.execute(sql)
        return json.dumps(self.myCursor.fetchall())

    def select_comp_agg(self, user):
        sql = 'SELECT COMPANY_ID, ROUND(SUM(AMOUNT),2) AS AGGREGATE FROM {0} WHERE USER_ID={1} GROUP BY COMPANY_ID;'.format(self.table, user)
        self.myCursor.execute(sql)
        row_headers = [x[0] for x in self.myCursor.description]
        rv = self.myCursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    def select_char_agg(self, user):
        sql = 'SELECT CHARITY_ID, ROUND(SUM(AMOUNT),2) AS AGGREGATE FROM {0} WHERE USER_ID={1} GROUP BY CHARITY_ID;'.format(self.table, user)
        self.myCursor.execute(sql)
        row_headers = [x[0] for x in self.myCursor.description]
        rv = self.myCursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)