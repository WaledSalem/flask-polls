from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# App Config (this app is not meant for production)
app.config['DEBUG'] = True

## DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/poll'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Marshmallow
ma = Marshmallow(app)

# API 
api = Api(app, prefix='/api')

from app import resources, routes

# Create dtabases and tables if it is the first run
db.create_all()
db.session.commit()
