from dataclasses import dataclass


class Prodotto:
    iva = 0.22 #variabile di classe -- ovvero la stessa per tutte le istanze
    def __init__(self, name: str, price:float, quantity:int , supplier= None):
        self.name = name
        self._price = None #serve per mettere privato l'attributo
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def value(self):
        return self._price*self.quantity

    def valore_netto(self):
        return self._price*self.quantity

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


    @property
    def price(self): #eq. getter
        return self._price

    @price.setter  #eq. setter
    def price(self,valore):
        if valore<0:
            raise ValueError("Attenzione il valore non può essere negativo") #errore nel valore inserito
            pass
        self._price = valore


    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price} euro"

    def __repr__(self):
        return f"Prodotto(name = {self.name}, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other: object):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self,other:"Prodotto") -> bool:  #anticipa che questo ritorna un valore booleano
        return self.price < other.price

    def prezzo_finale(self) -> float:
        return self.price*(1+self.iva)

class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price:float, quantity:int, supplier: str, sconto : float):
        super().__init__(name,price,quantity,supplier)
        self.sconto = sconto

    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto/100)

class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria:float, ore:int):
        super().__init__(name =name ,price = tariffa_oraria, quantity=1 , supplier=None )
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price*self.ore

class Abbonamento:
    def __init__(self, name: str, price_mensile:float, mesi:int):
        self.name = name
        self.price_mensile = price_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.price_mensile*self.mesi


@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    def __hash__(self):
        return hash((self.name,self.prezzo_unitario))

    def __str__(self):
        return f"{self.name} -- {self.prezzo_unitario}"

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome:str,price:float):
    return Prodotto(nome,price, quantity=1, supplier=None)

def _test_modulo():
    print("STO TESTANDO IL MODULO prodotti.py")
    myproduct1 = Prodotto("Laptop",1200.0, 12 ,"ABC")

    print( f"Nome Prodotto:{myproduct1.name} - prezzo {myproduct1.price}")

    print(f"Il totale lordo di myproduct1 {myproduct1.valore_lordo()}")
    p3 = Prodotto.costruttore_con_quantita_uno("Auricolari",200.0,"ABC") #METODO DI CLASSE CLASSE.METODO
    print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price,0.15)}")

    myproduct2 = Prodotto("Mouse",10.0, 25 ,"CDE")
    print( f"Nome Prodotto:{myproduct2.name} - prezzo {myproduct2.price}")

    Prodotto.iva = 0.24
    print(f"Valore lordo modificato di myproduct1 : {myproduct1.valore_lordo()}")

    print(myproduct1)

    p_a = Prodotto("Laptop",1200.0, 12 ,"ABC")
    p_b = Prodotto("Mouse",10.0, 14 ,"CDE")

    print("myproducts1 == pa?",myproduct1 == p_a) #va a chiamare il metodo __eq__ mi aspetto True
    print("pa == pb?",p_a == p_b)  # mi aspetto False

    myList = [p_a,p_b, myproduct1]
    myList.sort(reverse=True) #ordinata in modo decrescente
    print(f"lista ordinata dei prodotti")
    for p in myList:
        print(f"- {p}")


if __name__ == "__main__": #questo vuol dire che tutte le stampe in questo modulo partono se runno qui dentro (stand alone)
    _test_modulo() #se il main è un altro non stampa nulla