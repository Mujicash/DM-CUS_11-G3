from utils.db import db
from dataclasses import dataclass

@dataclass
class Propietario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    telefono = db.Column(db.String(9))
    correo = db.Column(db.String(100))

    def __init__(self, nombres, apellidos, telefono, correo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo

    def to_json(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "telefono": self.telefono,
            "correo": self.correo
        }