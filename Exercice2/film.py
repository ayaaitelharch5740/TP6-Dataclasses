from dataclasses import dataclass, asdict
from functools import total_ordering
import json

@total_ordering
@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not (0 <= self.note <= 10):
            raise ValueError("note hors limites")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    @staticmethod
    def from_json(s):
        data = json.loads(s)
        return Film(**data)

    def est_classique(self):
        return self.annee < 2000

    def __lt__(self, other):
        if not isinstance(other, Film):
            return NotImplemented
        return self.note < other.note
