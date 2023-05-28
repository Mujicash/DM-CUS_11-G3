from flask import Flask
from config import URI
from utils.db import db
from routes.propietario import propietario


app = Flask(__name__)
# connection = psycopg2.connect(url)
app.config["SQLALCHEMY_DATABASE_URI"] = URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(propietario)


db.init_app(app)
