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


class Customer(object):
    id = 0
    name = ""

    def __init__(self, name):
        self.name = name


class Employee(object):
    id = 0
    name = ""
    franchise_id = 0
    manager_id = 0

    def __init__(self, name, franchise_id, manager_id):
        self.name = name
        self.manager_id = manager_id
        self.franchise_id = franchise_id


class Franchise(object):
    id = 0
    name = ""
    st_address = ""
    address = ""
    city = ""
    state = ""
    zip = ""
    manager_id = 0;

    def __init__(self, name, st_address, address, city, state, zip, manager_id):
        self.name = name
        self.st_address = st_address
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.manager_id = manager_id


class Product(object):
    id = 0
    name = ""

    def __init__(self, name):
        self.name = name


class Service(object):
    id = 0
    name = ""

    def __init__(self, name):
        self.name = name


class Feedback(object):
    id = 0
    rating = 0
    comments = ""
    customer_id = 0
    item_id = 0

    def __init__(self, rating, comments, customer_id, item_id):
        self.rating = rating
        self.comments = comments
        self.customer_id = customer_id
        self.item_id = item_id


@app.route("/")
def index():
    return ""
