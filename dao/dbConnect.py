import mysql


class DBConnect:

    @classmethod
    def getConnection(cls):
        try:
            cnx = mysql.connector.connect(
                user="root",
                password="Monte290703@",
                host="127.0.0.1",
                database="sw_gestionale",
            )
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al db")
            print(err)
            return None
