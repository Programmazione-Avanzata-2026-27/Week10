from dataclasses import dataclass


@dataclass
class Sentiero:
    id : int
    id_luogo_1 : int
    id_luogo_2 : int
    nome : str
    lunghezza_km : float
    difficolta : str

    def __str__(self):
        return f"{self.id} {self.id_luogo_1} {self.id_luogo_2} {self.nome}"