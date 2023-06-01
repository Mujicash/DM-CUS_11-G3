from dataclasses import dataclass

from utils.db import db


@dataclass
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    id_tipo_documento = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'))
    numero_documento = db.Column(db.String(20), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)

    def __init__(self, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, id_tipo_documento, numero_documento):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.id_tipo_documento = id_tipo_documento
        self.numero_documento = numero_documento

    def to_json(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "fecha_nacimiento": self.fecha_nacimiento,
            "id_tipo_documento": self.id_tipo_documento,
            "numero_documento": self.numero_documento
        }