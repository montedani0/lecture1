#Sciviamo un codice pyton che modelli un semplice gestionale aziendale.


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

myproduct1 = Prodotto("Laptop",1200.0, 12 ,"ABC")

print( f"Nome Prodotto:{myproduct1.name} - prezzo {myproduct1.price}")

print(f"Il totale lordo di myproduct1 {myproduct1.valore_lordo()}")
p3 = Prodotto.costruttore_con_quantita_uno("Auricolari",200.0,"ABC") #METODO DI CLASSE CLASSE.METODO
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price,0.15)}")



myproduct2 = Prodotto("Mouse",10.0, 25 ,"CDE")
print( f"Nome Prodotto:{myproduct2.name} - prezzo {myproduct2.price}")

Prodotto.iva = 0.24

print(f"Valore lordo modificato di myproduct1 : {myproduct1.valore_lordo()}")


#SCRIVO UNA CLASSE CLIENTE "nome", "email", "categoria" ("Gold", "Silver","Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione" che restituisce una stringa formattata

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

print(c1.descrizione()) #METODO STANDARD OGGETTO.METODO



