#Sciviamo un codice pyton che modelli un semplice gestionale aziendale.


class Prodotto:
    iva = 0.22 #variabile di classe -- ovvero la stessa per tutte le istanze
    def __init__(self, name: str, price:float, quantity:int , supplier= None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def value(self):
        return self.price*self.quantity

    def valore_netto(self):
        return self.price*self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo =  netto * (1+self.iva)
        return lordo

    @classmethod
    def costruttore_con_quantita_uno(cls, name,price,supplier):
        cls(name,price,1,supplier)


    @staticmethod  #ESSENDO STATICO NON DEVO PASSARE cls o self ( non sono associati a nessuna istanza)
    def applica_sconto(prezzo,percentuale):
        return prezzo*(1-percentuale)


myproduct1 = Prodotto("Laptop",1200.0, 12 ,"ABC")
myproduct2 = Prodotto("Mouse",10.0, 25 ,"CDE")


print( f"Nome Prodotto:{myproduct1.name}")
print( f"Prezzo Prodotto:{myproduct1.price}")


#SCRIVO UNA CLASSE CLIENTE "nome", "email", "categoria" ("Gold", "Silver","Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione" che restituisce una stringa formattata

class Cliente:
    def __init__(self, name: str, email:str, categoria=None):
        self.name = name
        self.email = email
        self.categoria = categoria

    def descrizione(self):
       return f"Cliente {self.name} {self.email} ({self.categoria})"


c1 = Cliente("Mario Bianchi", "mario.bianchi@gmail.com", "Gold")
print(c1.descrizione())

print(f"Il totale lordo di myproduct1 {myproduct1.valore_lordo()}")
p3 = Prodotto.costruttore_con_quantita_uno("Auricolaro",200.0,"ABC")
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price,0.15)}")