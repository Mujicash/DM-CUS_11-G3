from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Predio(db.Model):

    __tablename__ = 'tipo_predio'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre = nombre

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }