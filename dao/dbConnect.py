import pathlib

import mysql



class DBConnect:

    _myPool = None
    #per implementare il pattern singleton e impedire al chiamante di creare istanze di classe
    def __init__(self):
        raise RuntimeError("Attenzione! Non devi creare un'istanza di questa classe. Usa i metodi di classe")

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            try:
                # cnx = mysql.connector.connect(
                #   user="root",
                #    password="Monte290703@",
                #    host="127.0.0.1",
                #    database="sw_gestionale",
                #)
                #return cnx
                #cls vuol dire che è un attributo della classe
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    #user = "root",
                    #password = "Monte290703@",
                    #host = "127.0.0.1",
                    #database="sw_gestionale",
                    pool_size=3,
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                    )
                return cls._myPool.get_connection()



            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            return cls._myPool.get_connection()
