import pytest
from film import Film
import json

def test_creation_valide():
    f = Film("Inception", "Nolan", 2010, 8.7)
    assert f.titre == "Inception"
    assert f.note == 8.7

def test_note_invalide():
    with pytest.raises(ValueError):
        Film("X", "Y", 2000, 11)

def test_est_classique():
    assert Film("Old", "A", 1995, 7).est_classique() is True
    assert Film("New", "B", 2005, 7).est_classique() is False

def test_to_json():
    f = Film("Test", "Dir", 1999, 9)
    js = f.to_json()
    d = json.loads(js)
    assert d["titre"] == "Test"
    assert d["annee"] == 1999

def test_from_json():
    js = '{"titre":"A","realisateur":"B","annee":1980,"note":6}'
    f = Film.from_json(js)
    assert f.realisateur == "B"
    assert f.note == 6

def test_comparaison():
    f1 = Film("A", "X", 2000, 5)
    f2 = Film("B", "Y", 2000, 8)
    assert f1 < f2

def test_favoris_serialisation():
    films = [
        Film("A", "X", 2000, 5),
        Film("B", "Y", 1990, 9),
    ]
    js = json.dumps([json.loads(f.to_json()) for f in films], ensure_ascii=False)
    data = json.loads(js)
    assert len(data) == 2
    assert data[1]["note"] == 9
