from dataclasses import dataclass
from datetime import date

from gestionale.core.cliente import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura : str
    data : date


    def genera_fattura(self):
        linee = [
            f"="*60,
            #intestazione fattura
            f"FATTURA N.: {self.numero_fattura} DEL {self.data}",
            f"=" * 50,
            #dettaggli cliente
            f"Cliente: {self.ordine.cliente.name}  ",
            f"Email: {self.ordine.cliente.email}",
            f"Categoria:{self.ordine.cliente.categoria}",
            f"-" * 50,
            f"DETTAGLIO FATTURA"


        ]

        for i, riga in enumerate(self.ordine.righe):
            linee.append(
            f"{i+1}. "
            f"{riga.prodotto.name} "
            f"Q.ta {riga.quantita} x {riga.prodotto.prezzo_unitario} "
            f"Tot. {riga.totale_riga()}"
            )
        linee.extend([
            f"-"*60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"Iva(22%): {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            f"=" * 50
            ]

        )

        return "\n".join(linee)


def _test_modulo():
    p1 = ProdottoRecord("Laptop",1200.0)
    p2 = ProdottoRecord("Mouse",20.0)
    p3 = ProdottoRecord("Tablet",600.0)
    cliente = ClienteRecord("Mario Bianchi","mariobianchi@polito.it","Gold")
    ordine = Ordine(righe=[
        RigaOrdine(p1,1),
        RigaOrdine(p2, 5),
        RigaOrdine(p3, 2)],cliente=cliente)
    fattura = Fattura(ordine, "2026/01",date.today())
    print(fattura.genera_fattura())

if __name__ == "__main__":
    _test_modulo()

