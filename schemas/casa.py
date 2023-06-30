from utils.ma import ma
from models.casa import Casa

class CasaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Casa
        fields = [
            "id_casa",
            "numero",
            "piso",
            "area",
            "participacion",
        ]

casa_schema = CasaSchema()
casas_schema = CasaSchema(many=True)