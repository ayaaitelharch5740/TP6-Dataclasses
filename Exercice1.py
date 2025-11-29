from dataclasses import dataclass, asdict
import json
from functools import total_ordering

@total_ordering
@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        """Sérialise l’objet Livre en chaîne JSON."""
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit: float):
        """Retourne un NOUVEAU livre avec un prix réduit (objet immuable)."""
        return Livre(
            titre=self.titre,
            auteur=self.auteur,
            annee=self.annee,
            prix=prix_reduit
        )

    @staticmethod
    def from_json(json_str: str):
        """Reconstitue un Livre depuis une chaîne JSON."""
        data = json.loads(json_str)
        return Livre(**data)


    def __lt__(self, other):
        if not isinstance(other, Livre):
            return NotImplemented
        return self.prix < other.prix



livre = Livre("1984", "George Orwell", 1949, 9.90)
print(livre.to_json())
