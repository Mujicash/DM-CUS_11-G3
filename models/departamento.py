from utils.db import db
from dataclasses import dataclass

@dataclass
class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    piso = db.Column(db.Integer)
    torre = db.Column(db.String(10))
    id_condo = db.Column(db.Integer, db.ForeignKey('condominio.id'))
    id_owner = db.Column(db.Integer, db.ForeignKey('propietario.id'))

    def __init__(self, piso, torre, id_condo, id_owner):
        self.piso = piso
        self.torre = torre
        self.id_condo = id_condo
        self.id_owner = id_owner

    def to_json(self):
        return {
            "id": self.id,
            "piso": self.piso,
            "torre": self.torre,
            "id_condo": self.id_condo,
            "id_owner": self.id_owner
        }