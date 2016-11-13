from flask import Flask
import os, logging
from flask.ext.mysql import MySQL
import json

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'LabelInfo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

class User(object):
    firstName = ""
    lastName = ""
    location = ""
    birthdate = ""
    confidence = 0
    def __init__(self, firstName, lastName, location, birthdate, confidence):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location
        self.birthdate = birthdate
        self.confidence = confidence
