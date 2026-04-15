"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini
1bis) quando arriva un ordine lo aggiungo a una cosa, assicurandomi che sia eseguito dopo gli altri
2)avere delle funzionalità per avere statistiche sugli ordini
3)fornire statistiche sulla distribuzione di ordini per categoria di cliente
"""
import random
from collections import deque, Counter, defaultdict

from dao.dao import DAO
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine



class GestorOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati  = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)
        #self._dao = DAO()
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self):
        #Leggo prodotti e clienti dal db, e poi creo  degli ordini randomici per testar la mia app
        self._allP.extend(DAO.getAllProdotti())
        self._allC.extend(DAO.getAllClienti())

        for i in range(10):
            indexP = random.randint(0,len(self._allP)-1)
            indexC = random.randint(0,len(self._allC)-1)
            ordine = Ordine([RigaOrdine(self._allP[indexP],random.randint(1,5))],
                         self._allC[indexC])
            self.add_ordine(ordine)

    def add_ordine(self, ordine:Ordine):
        """Aggiunge un nuovo ordie agli elementi da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da: {ordine.cliente}")
        print(f"Ordini ancora da processare: {len(self._ordini_da_processare)}")


    def _update_DB(self,prod,cliente):
        if not DAO.hasProdotto(prod):
            DAO.addProdotto(prod)

        if not DAO.hasCliente(cliente):
            DAO.addCliente(cliente)



    def crea_ordine(self,nomeP, prezzoP,quantitaP,nomeC, email,categoria):
        prod = ProdottoRecord(nomeP,prezzoP)
        clie = ClienteRecord(nomeC,email,categoria)
        self._update_DB (prod,clie)
        return Ordine([RigaOrdine(prod,quantitaP)],clie)

    def processa_prox_ordine(self):
        """"Legge il prossimo ordine in coda e lo gestisce"""
        #Si assicura che un ordine da processare esista
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False, Ordine([], ClienteRecord("","",""))

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

        return True, ordine


    def processa_tutti_ordini(self):
        """Processa tutti gli ordini presenti"""
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordine")
        ordini = []

        while self._ordini_da_processare:
            _,ordine = self.processa_prox_ordine()
            ordini.append(ordine)

        print("Tutti gli ordini sono stati processati")
        return ordini



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


    def get_riepilogo(self):
        sommario = ""
        sommario += ("\n" + "="*60)
        sommario +=f"\n Ordini correttamente gestiti : {len(self._ordini_processati)}"
        sommario +=f"\n Ordini in coda : {len(self._ordini_da_processare)}"

        sommario +="\n Prodotti più venduti"
        for prodotti,quantita in self.get_statistiche_prodotti():
            sommario +=f"\n {prodotti} : {quantita}"

        sommario += f"\n Fatturato per categoria"
        for cat,total in self.get_distibuzione_categorie():
            sommario += f"\n {cat} : {total}"
        sommario += ("\n" + "=" * 60)

        return sommario

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