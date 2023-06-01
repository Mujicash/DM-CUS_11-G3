from dataclasses import dataclass

from utils.db import db


@dataclass
class Casa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    piso = db.Column(db.Integer)
    bloque = db.Column(db.String(10))
    numero = db.Column(db.Integer)
    area = db.Column(db.Float(10,2))
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id'))
    id_propietario = db.Column(db.Integer, db.ForeignKey('persona.id'))
    id_estado_casa = db.Column(db.Integer, db.ForeignKey('casa_estado.id'))

    def __init__(self, piso, bloque, numero, area, id_predio, id_propietario, id_estado_casa):
        self.piso = piso
        self.bloque = bloque
        self.numero = numero
        self.area = area
        self.id_predio = id_predio
        self.id_propietario = id_propietario
        self.id_estado_casa = id_estado_casa

    def to_json(self):
        return {
            "id": self.id,
            "piso": self.piso,
            "bloque": self.bloque,
            "numero": self.numero,
            "area": self.area
        }