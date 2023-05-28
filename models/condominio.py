from utils.db import db
from dataclasses import dataclass

@dataclass
class Condominio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(100))

    def __init__(self, nombre, direccion):
        self.nombres = nombre
        self.apellidos = direccion

    def to_json(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.direccion
        }