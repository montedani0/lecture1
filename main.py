#Sciviamo un codice pyton che modelli un semplice gestionale aziendale.
from urllib.request import ProxyDigestAuthHandler


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

my_Prod_Scontato = ProdottoScontato(name="Auricolari", price=320, quantity=1, supplier="ABC", sconto= 10)
my_Service = Servizio(name="Consulenza", tariffa_oraria=100, ore=3)

myList.append(my_Prod_Scontato)
myList.append(my_Service)

myList.sort(reverse=True)

for e in myList:
    print(e.name, "-->", e.prezzo_finale(), "euro")

#Definire una classe abbonamento che come attributi (nome, prezzo mensile, mesi). Abbonamento dovrà avere un metodo
#per calcolare il prezzo finale
print("------------------------------------------------------------")
class Abbonamento:
    def __init__(self, name: str, price_mensile:float, mesi:int):
        self.name = name
        self.price_mensile = price_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.price_mensile*self.mesi

abb =  Abbonamento("Software gestionale", 30,24)
myList.append(abb)
for e in myList:
    print(e.name, "-->", e.prezzo_finale(), "euro")

def calcola_totale(elementi):
    tot = 0
    for e in elementi:
        tot += e.prezzo_finale()

    return tot

print(f"Il totale è : {calcola_totale(myList)} euro")


from typing import Protocol

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self) -> float:
        ... #i tre puntini è una delega vuol dire che non verranno implementati qui main altri metodo

def calcola_totale(elementi:list[HaPrezzoFinale]) -> float:#vuol dire che tutti gli elementi hanno un prezzo finale
    return sum(e.prezzo_finale() for e in elementi) #somma tutti i prezzi finali di tutti gli elementi presenti in una lista

print(f"Il totale è : {calcola_totale(myList)} euro")

print("------------------------------------------------------------")
print("Sperimentiamo con dataclass")

from dataclasses import dataclass
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario:float
@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria:str

@dataclass
class RigaOrdine:
    prodotto : ProdottoRecord
    quantita : int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario*self.quantita

@dataclass
class Ordine:
    righe: list[RigaOrdine]
    cliente : ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self, aliquota_iva):
        return self.totale_netto()*(1+aliquota_iva)

    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineConSconto(Ordine):
    sconto : float

    def totale_scontato(self,aliquota_iva):
        return self.totale_lordo(aliquota_iva)*(1-self.sconto)

    def totale_netto(self):
        netto_base = super().totale_netto()
        return netto_base*(1-self.sconto)

cliente1  = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20)
ordine = Ordine([RigaOrdine(p1,2),RigaOrdine(p2,10)], cliente1)
ordine_con_sconto = OrdineConSconto([RigaOrdine(p1,2),RigaOrdine(p2,10)], cliente1,0.10)

print(ordine)
print(f"Numero righe nell'ordine: {ordine.numero_righe()}")
print(f"Totale netto: {ordine.totale_netto()} euro")
print(f"Totale lordo (IVA 22%): {ordine.totale_lordo(0.22)} euro")
print(ordine_con_sconto)
print(f"Totale netto scontato: {ordine_con_sconto.totale_netto()} euro")
print(f"Totale lordo (IVA 22%): {ordine_con_sconto.totale_lordo(0.22)} euro")






print("------------------------------------------------------------")



#SCRIVO UNA CLASSE CLIENTE "nome", "email", "categoria" ("Gold", "Silver","Bronze").
#Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione" che restituisce una stringa formattata

#Si modifichi la classe cliente inn maniera tale che la proprietà categoria sia "protetta2 e accetti solo ("Gold","Silver","Bronze")

class Cliente:
    def __init__(self, name: str, email:str, categoria=None):
        self.name = name
        self.email = email
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self,categoria):
        cateorie_valide = {"Gold","Silver","Bronze"}
        if categoria not in cateorie_valide:
            raise ValueError("Categoria inserita non valida. Scegliere tra Gold,Silver,Bronze")
            pass
        self._categoria = categoria

    def descrizione(self):
       return f"Cliente {self.name} {self.email} ({self.categoria})"


c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.com", "Gold")
c2 = Cliente("Carlo Masone", "carlo.masone@gmail.com", "Silver")

print(c1.descrizione()) #METODO STANDARD "OGGETTO.METODO"



