#Sciviamo un codice pyton che modelli un semplice gestionale aziendale.

from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard  # DEVO IMPORTARLO PER POTERLO UTILIZZARE
import networkx as nx

print("===========================================")
p1 = Prodotto("Ebook",120.0,1,"AAA")
p2 = crea_prodotto_standard("Tablet",750)

print(p1)
print(p2)

#MODI DI IMPORTARE
#1

#2
from gestionale.core.prodotti import ProdottoScontato as ps
p3 = ps("Auricolari",230,1,"ABC",10)

#3
p4 = ps("Auricolari", 230, 1, "ABC", 10)
#4

p5 = ps("Auricolari",230,1,"ABC",10)


print("------------------------------------------------------------")

from gestionale.core import cliente as c, prodotti

c1 = c.Cliente("Mario Rossi","mail@gmial.com", "Gold")

print("Sperimentiamo con dataclass")

cliente1  = c.ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = prodotti.ProdottoRecord("Laptop", 1200.0)
p2 = prodotti.ProdottoRecord("Mouse", 20)
ordine = Ordine([RigaOrdine(p1,2),RigaOrdine(p2,10)], cliente1)
ordine_con_sconto = OrdineConSconto([RigaOrdine(p1,2),RigaOrdine(p2,10)], cliente1,0.10)

print(ordine)
print(f"Numero righe nell'ordine: {ordine.numero_righe()}")
print(f"Totale netto: {ordine.totale_netto()} euro")
print(f"Totale lordo (IVA 22%): {ordine.totale_lordo(0.22)} euro")
print(ordine_con_sconto)
print(f"Totale netto scontato: {ordine_con_sconto.totale_netto()} euro")
print(f"Totale lordo (IVA 22%): {ordine_con_sconto.totale_lordo(0.22)} euro")






