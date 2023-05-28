from flask import Flask

from config import URI
from routes.condominio import condominio
from routes.cuenta import cuenta
from routes.departamento import departamento
from routes.propietario import propietario
from utils.db import db

app = Flask(__name__)
# connection = psycopg2.connect(url)
app.config["SQLALCHEMY_DATABASE_URI"] = URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(propietario)
app.register_blueprint(condominio)
app.register_blueprint(departamento)
app.register_blueprint(cuenta)


db.init_app(app)
