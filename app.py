from flask import Flask
from config import URI
from utils.db import db
from routes.propietario import propietario
from routes.condominio import condominio
from routes.departamento import departamento


app = Flask(__name__)
# connection = psycopg2.connect(url)
app.config["SQLALCHEMY_DATABASE_URI"] = URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(propietario)
app.register_blueprint(condominio)
app.register_blueprint(departamento)


db.init_app(app)
