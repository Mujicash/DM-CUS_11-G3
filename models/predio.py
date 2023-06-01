from utils.db import db
from dataclasses import dataclass

@dataclass
class Predio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    distrito = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id'))

    def __init__(self, nombre, direccion, distrito, telefono, id_tipo_predio):
        self.nombre = nombre
        self.direccion = direccion
        self.distrito = distrito
        self.telefono = telefono
        self.id_tipo_predio = id_tipo_predio

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "distrito": self.distrito,
            "telefono": self.telefono,
            "id_tipo_predio": self.id_tipo_predio
        }