from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Predio(db.Model):

    __tablename__ = 'tipo_predio'

    id_tipo_predio = db.Column(db.Integer, primary_key = True)
    nombre_predio = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre_predio = nombre

    def to_json(self):
        return {
            "id": self.id_tipo_predio,
            "nombre": self.nombre_predio
        }