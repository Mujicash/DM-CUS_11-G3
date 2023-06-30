from utils.ma import ma
from models.recibo import Recibo

class ReciboSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recibo
        fields = [
            "id_mant_recibo",
            "n_recibo",
            "periodo",
            "importe",
            "ajuste"
        ]

recibo_schema = ReciboSchema()
recibos_schema = ReciboSchema(many=True)