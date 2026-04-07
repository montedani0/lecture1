"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini
1bis) quando arriva un ordine lo aggiungo a una cosa, assicurandomi che sia eseguito dopo gli altri
2)avere delle funzionalità per avere statistiche sugli ordini
3)fornire statistiche sulla distribuzione di ordini per categoria di cliente
"""
from collections import deque, Counter, defaultdict

from gestionale.core.cliente import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import RigaOrdine
from gestionale.vendite.provaCollections import Ordine, ordine


class GestorOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati  = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def add_ordine(self, ordine:Ordine):
        """Aggiunge un nuovo ordie agli elementi da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da: {ordine.cliente}")
        print(f"Ordini ancora da processare: {len(self._ordini_da_processare)}")


    def crea_ordine(self,nomeP, prezzoP,quantitaP,nomeC, email,categoria):
        return Ordine([RigaOrdine(ProdottoRecord(nomeP,prezzoP),quantitaP)],ClienteRecord(nomeC,email,categoria))

    def processa_prox_ordine(self):
        """"Legge il prossimo ordine in coda e lo gestisce"""
        #Si assicura che un ordine da processare esista
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False

        #Se esiste gestiamo il primo in cosa
        ordine = self._ordini_da_processare.popleft()
        print(ordine.riepilogo())

        #Aggiornare stat sui prodotti venduti
        #Laptop - 10 +1
        #Mouse - 5 + 2
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        #Raggruppare per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #Archiviamo
        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato")

        return True


    def processa_tutti_ordini(self):
        """Processa tutti gli ordini presenti"""
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordine")
        while self._ordini_da_processare:
            self.processa_prox_ordine()

        print("Tutti gli ordini sono stati processati")



    def get_statistiche_prodotti(self, top_n:int = 5):
        """Questo metodo restituisce info sui prodotti più venduti"""
        valori = []
        for prodotto,quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto,quantita))
        return valori


    def get_distibuzione_categorie(self):
        """Questo metodo restituisce info su totale dei prod più venduti"""
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            total = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat,total))
        return valori


    def stampa_riepilogo(self):
        print("\n" + "="*60)
        print("Stampa attuale business")
        print(f"Ordini correttamente gestiti : {len(self._ordini_processati)}")
        print(f"Ordini in coda : {len(self._ordini_da_processare)}")

        print("Prodotti più venduti")
        for prodotti,quantita in self.get_statistiche_prodotti():
            print(f"{prodotti} : {quantita}")

        print(f"Fatturato per categoria")
        for cat,total in self.get_distibuzione_categorie():
            print(f"{cat} : {total}")

def test_modulo():
    sistema = GestorOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200),1),
                RigaOrdine(ProdottoRecord("Mouse",10.0),3)],
               ClienteRecord("Mario Rossi", "mariorossi@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200),1),
                RigaOrdine(ProdottoRecord("Mouse",10.0),3),
                RigaOrdine(ProdottoRecord("Tablet",500),1),
                RigaOrdine(ProdottoRecord("Cuffie",250.0),3)],
               ClienteRecord("Fulvio Bianchi", "fulviobianchi@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200),2),
                RigaOrdine(ProdottoRecord("Mouse",10.0),2)],
               ClienteRecord("Giuse Averta", "giuaverta@gmail.com", "Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Tablet",900),1),
                RigaOrdine(ProdottoRecord("Cuffie",250),3)],
               ClienteRecord("Carlo Masone", "camasone@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200),1),
                RigaOrdine(ProdottoRecord("Mouse",10.0),3)],
               ClienteRecord("Fra Pistilli", "frapis@gmail.com", "Bronze"))]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()

    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()