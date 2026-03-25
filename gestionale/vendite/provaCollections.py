import copy
from collections import Counter, deque

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1,p2,p3,ProdottoRecord("Tablet", 700.0)]

print("Prodotto nel carrello")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

carrello.append(ProdottoRecord("Monitor", 150.0)) #AGGIUNGO

carrello.sort(key=lambda x: x.prezzo_unitario, reverse = True) #ORDINO

print("Prodotto nel carrello")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)  #cicla su carrello lo mette in una lista p.prezzo_unitario
print(f"Totale del carrello: {tot}")

#Aggiungere

carrello.append(ProdottoRecord("Laptop", 250.0)) #Aggiungo elemento in coda
carrello.extend([ProdottoRecord("aaa", 450.0),ProdottoRecord("bbb", 100.0)]) #Aggiungere un'altra lista in coda
carrello.insert(2,ProdottoRecord("aaa", 450.0)) #Aggiungere elemento in un pos specifica

#Rimuovere
carrello.pop() #Rimuovere ultimo elemento
carrello.pop(2) #Rimuovere elemento in pos 2
carrello.remove(p1)#Rimuove un elemento specifico, il primo p1 trovato nella lista
#carrello.clear()#Svuota l'intera lista

#Sorting
#carrello.sort()#ordina seguendo ordinamento naturale -- questo non funziona se gli oggetti contenuti non hanno __lt__
#carrello.sort(reverse = True)#ordina al contrario
#carrello.sort(key = function)  tipo lambda
#carrello_ordinato = sorted(carrello) #copia una lista e la ordina
carrello.reverse() #inverte l'ordine
carrello_copia = carrello.copy() #shallow copy, qualsiasi elemento modificato da un parte viene modificato anche dall'altra
carrello_copia2 =copy.deepcopy(carrello) #crea una copia stand-alone

#Tuple

sede_principale=(45,8) #Lat e long della sede di Torino
sede_milano = (45,9) #Lat e long della sede di Milano

print(f"Sede_principale: lat {sede_principale[0]} long {sede_principale[1]} ")

AliquoteIva = (
("Standard", 0.22),
("Alimentari", 0.04),
("Ridotta", 0.10),
("Esente", 0.0),
)

for desc, valore in AliquoteIva:
    print(f"{desc}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    #Restituisce prezzo totale, prezzo medio, prezzo max e min
    prez = [p.prezzo_unitario for p in carrello]
    return sum(prez), sum(prez) / len(prez),max(prez),min(prez)

tot,media,mas,mini = calcola_statistiche_carrello(carrello)
tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#Set
categorie = {"Gold","Silver","Bronze"}
print(categorie)
print(len(categorie))
categorie_2 = {"Platinum", "Elite", "Gold"}
#categorie_all= categorie.union(categorie_2)
categorie_all= categorie |categorie_2
print(categorie_all)

categorie_comuni = categorie & categorie_2 #va a prendere solo gli elementi in comune
print(categorie_comuni)

categorie_esclusive = categorie - categorie_2 #prende gli elementi di un set e toglie quelli degli altri
print(categorie_esclusive)

categorie_esclusive_simmetriche = categorie ^ categorie_2 #differenza simmetrica, tutti tranne quelli uguali
print(categorie_esclusive_simmetriche)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                     ProdottoRecord("Mouse", 250.0),
                     ProdottoRecord("Auricolari", 150.0)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0),
                     ProdottoRecord("Mouse2", 250.0),
                     ProdottoRecord("Auricolari2", 150.0)}

#Metodi utili per i set
s = set()
s1 = set()

#aggiungere
prodotti_ordine_A.add(ProdottoRecord("aaa", 20.0))  #Aggiung un elemento 7
s.update([ProdottoRecord("aaa", 1200.0),ProdottoRecord("bbb", 250.0)])

#togliere
#s.remove(elem) rimuove un elemento. Raise KeyError se non c'è
#s.discard(elem) #rimuove un elemento anche se non c'è
s.pop() # rimuove e restituisce uno
s.clear()

#operazioni insiemistiche
s.union(s1) # s|s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero elementi comuni
s.difference(s1) #s-s1 ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^ s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s


s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) #se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) #se gli elementi di s e quelli di s1 sono diversi

#Dizionario
catalogo = {
    "Lap001" : ProdottoRecord("Laptop", 1200.0),
    "Lap002" : ProdottoRecord("Laptop Pro", 2300.0),
    "Mau001" : ProdottoRecord("Mouse", 250.0),
    "Aur001" : ProdottoRecord("Auricolari", 150.0),
}

cod = "Lap002"
prod = catalogo[cod]
print(f"Il prodotto con codice {cod} è {prod}")

prod1 = catalogo.get("Non Esiste")
if prod1 in catalogo:
    print (f"Prodotto Non Trovato")


prod2 = catalogo.get("Non Esiste2", ProdottoRecord("Sconosciuto", 0.0))

print(prod2)

keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print (k)

for v in values:
    print(v)

for keys2,values2 in catalogo.items():
    print(f"codice {keys2} è associata a: {values2}")

#rimuovere
rimosso = catalogo.pop("Lap002")
print(rimosso)

#dict comprehension
prezzi= {codice:prod.prezzo_unitario for codice, prod in catalogo.items()}

#da ricordare

#v = d[key]     #per leggere
#d[key] = v     #scrivo sul dizionario
#v = d.get(key,default)     # legge senza rischiare key error
#d.pop      #restituisce un valore e lo elimina
#d.clear    #svuota il dizionario
#d.keys()   #mi restituisce tutte le chiavi
#d.values()     # mi restituisce tutti i valori
#d.items()  #mi restituisce la coppia chiave,valore
#key in d   # condizione che verifica se la chiave è presente nel dizionario


"""Esercizio"""

"""1) Memorizzare un elenco di ordini che dovranno poi essere processati in ordine di arrivo"""
ordini_da_processare = []
o1 = Ordine([],ClienteRecord("Mario Rossi","mariorossi@gmail.com","Gold"))
o2 = Ordine([],ClienteRecord("Mario Bianchi","mariobianchi@gmail.com","Silver"))
o3 = Ordine([],ClienteRecord("Fulvio Rossi","fulviorossi@gmail.com","Bronze"))
o4 = Ordine([],ClienteRecord("Carlo Masone","carlomasone@gmail.com","Bronze"))

ordini_da_processare.append((o1,0))
ordini_da_processare.append((o2,10))
ordini_da_processare.append((o3,3))
ordini_da_processare.append((o4,45))

"""2) Memorizzare i CF dei clienti"""
codici_fiscali = {"ascvgfred231","juytfc54","njuytrdc78","juytfc54"}

"""3) Creare un database di prodotti che posso cercare con un codice univoco"""
listino_prodotti = {"LAP001": ProdottoRecord("Laptop", 1200.0),
                    "KEY001": ProdottoRecord("Keyboard", 2300.0),}


"""4)Memorizzare le coordinate gps della nuova sede di Roma"""
magazzino_roma = (45,7)

"""5)Tenere traccia delle categorie dei clienti che hanno fatto un ordine in un certo range temporale"""
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("==============================================")

#COUNTER
lista_clienti = [
ClienteRecord("Mario Rossi","mario@gmail.com","Gold"),
ClienteRecord("Mario Bianchi","bianchi@gmail.com","Silver"),
ClienteRecord("Fulvio Rossi","fulvio@gmail.com","Bronze"),
ClienteRecord("Carlo Masone","carloma@gmail.com","Bronze"),
ClienteRecord("Mario Bianchi", "mario@gmail.com", "Gold"),
ClienteRecord("Giuse Averta", "mariobianchi@gmail.com", "Silver"),
ClienteRecord("Fra Pis", "fulvio@gmail.com", "Bronze"),
ClienteRecord("Carlo Masone", "casone@gmail.com", "Bronze"),
ClienteRecord("Fulvio Corno", "fulvio@polito.it", "Silver")]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)
print(categorie_counter)

print("Categoria più frequente")
print(categorie_counter.most_common(1))
print("2 Categorie più frequenti")
print(categorie_counter.most_common(2))


print("Totale:")
print(categorie_counter.total())

vendite_gennaio = Counter({
    "Laptop" : 13, "Tablet" : 15
})
print(vendite_gennaio)

vendite_febbraio = Counter({
    "Laptop" : 3, "Stampanti" : 1
})

print(vendite_febbraio)

#Aggregare le info
vendite_bimestre = vendite_gennaio+vendite_febbraio
print(vendite_bimestre)

#Sottrarre
vendite_bimestre_diff= vendite_gennaio-vendite_febbraio
print(vendite_bimestre_diff)

#modificarne i valori in the fly

vendite_gennaio["Laptop"] +=4
print(f"vendite_gennaio aggiornato {vendite_gennaio}")

#metodi da ricordare
#c.most_common(n)  #restituisce gli n elementi più frequenti
#c.total   #somma dei conteggi


print("==============================================")


#Deque
coda_ordini = deque()

for i in range(1,10):
    cliente= ClienteRecord(f"Cliente{i}",f"cliente{i}@gmail.com","Gold")
    prodotto = ProdottoRecord(f"Prodotto{i}", 100.0*1)
    ordine = Ordine([RigaOrdine(prodotto,1)], cliente)
    coda_ordini.append(ordine)

print(f"Ordini in coda {len(coda_ordini)}")

while coda_ordini:
    ordine_corrente= coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente: {ordine_corrente.cliente}")
print("Ho processato tutti gli ordini")
