import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord



class DAO:

    def getAllProdotti(self):
        """cnx = mysql.connector.connect(
            user= "root",
            password= "Monte290703@",
            host= "127.0.0.1",
            database= "sw_gestionale"
        )
        """
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from prodotti")
        row = cursor.fetchall()
        res=[]
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from clienti")
        row = cursor.fetchall()
        res=[]
        for p in row:
            res.append(ClienteRecord(p["nome"], p["email"], p["categoria"]))

        cursor.close()
        cnx.close()
        return res

    def addProdotto(self, prodotto):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query ="insert into prodotti (nome, prezzo) values (%s, %s)"
        cursor.execute(query,(prodotto.name, prodotto.prezzo_unitario))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def addCliente(self, cliente):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query ="insert into clienti(nome,email,categoria) values (%s, %s,%s)"
        cursor.execute(query,(cliente.name,cliente.email,cliente.categoria))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def hasCliente(self, cli):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "select * from clienti where email = %s"
        cursor.execute(query, (cli.email,))
        row = cursor.fetchall()
        cursor.close()
        cnx.close()
        return len(row)>0

    def hasProdotto(self, prod):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prod.name,))
        row = cursor.fetchall()
        cursor.close()
        cnx.close()
        return len(row)>0


if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()
