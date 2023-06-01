from flask import Flask

from config import URI
from routes.predio import predio
from routes.cuenta import cuenta
from routes.casa import casa
from routes.propietario import persona
from routes.recaudacion import recaudacion
from routes.recibo import recibo
from routes.tipo_predio import tipo_predio
from routes.banco import banco
from routes.casa_estado import casa_estado
from routes.tipo_documento import tipo_documento
from routes.recibo_estado import recibo_estado
from utils.db import db

app = Flask(__name__)
# connection = psycopg2.connect(url)
app.config["SQLALCHEMY_DATABASE_URI"] = URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(persona)
app.register_blueprint(predio)
app.register_blueprint(casa)
app.register_blueprint(cuenta)
app.register_blueprint(recibo)
app.register_blueprint(recaudacion)
app.register_blueprint(tipo_predio)
app.register_blueprint(banco)
app.register_blueprint(casa_estado)
app.register_blueprint(tipo_documento)
app.register_blueprint(recibo_estado)


db.init_app(app)
