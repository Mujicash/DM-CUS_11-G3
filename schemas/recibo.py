from utils.ma import ma
from models.recibo import Recibo

from schemas.casa import CasaSchema
from schemas.recibo_estado import ReciboEstadoSchema

class ReciboSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recibo
        fields = [
            "id_mant_recibo",
            "n_recibo",
            "periodo",
            "importe",
            "ajuste",
            "recibo_casa",
            "estado_recibo"
        ]

    recibo_casa = ma.Nested(CasaSchema, only = ["numero", "piso", "area", "participacion"])
    estado_recibo = ma.Nested(ReciboEstadoSchema, only = ["descripcion"]) 

recibo_schema = ReciboSchema()
recibos_schema = ReciboSchema(many=True)