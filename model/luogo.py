from dataclasses import dataclass

@dataclass
class Luogo:
    id : int
    nome : str
    tipo : str
    quota_m : int

    def __str__(self):
        return f"{self.id} {self.nome} {self.tipo} {self.quota_m} m"

    # Questa per poter usare i luoghi come nodi del grafo
    def __hash__(self):
        return hash(self.id)