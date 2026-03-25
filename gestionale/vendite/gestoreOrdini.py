"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini
1bis) quando arriva un ordine lo aggiungo a una cosa, assicurandomi che sia eseguito dopo gli altri
2)avere delle funzionalità per avere statistiche sugli ordini
3)fornire statistiche sulla distribuzione di ordini per categoria di cliente
"""
from collections import deque, Counter, defaultdict

from gestionale.core.cliente import Cliente
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

    def processa_prox_ordine(self):
        """"Legge il prossimo ordine in coda e lo gestisce"""

        #Si assicura che un ordine da processare esista
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
        print(f"Processando{len(self._ordini_da_processare)} ordine")
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
            total = sum([o.totale_lordo() for o in ordini])
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

