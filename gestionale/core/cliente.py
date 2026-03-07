#Si modifichi la classe cliente inn maniera tale che la proprietà categoria sia "protetta2 e accetti solo ("Gold","Silver","Bronze")
from dataclasses import dataclass

cateorie_valide = {"Gold","Silver","Bronze"}

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
        if categoria not in cateorie_valide:
            raise ValueError("Categoria inserita non valida. Scegliere tra Gold,Silver,Bronze")
            pass
        self._categoria = categoria

    def descrizione(self):
       return f"Cliente {self.name} {self.email} ({self.categoria})"

@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria:str

def _test_modulo():

    c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.com", "Gold")
    c2 = Cliente("Carlo Masone", "carlo.masone@gmail.com", "Silver")

    print(c1.descrizione()) #METODO STANDARD "OGGETTO.METODO"

if __name__ == "__main__":
    _test_modulo()

