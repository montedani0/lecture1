from dataclasses import dataclass


@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria:str

    def __hash__(self): #due oggetti sono uguali se hanno la stessa chiave
                        # (in questo caso la chiave univoca è la email)
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email

    def __str__(self):
        return f"{self.name}--{self.email} ({self.categoria})"