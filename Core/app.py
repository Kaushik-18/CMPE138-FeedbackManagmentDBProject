from flask import Flask
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'LabelInfo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

class Entity(object):
    """Abstract base class for all Entities"""
    def persist(self):
        """for all variable in the (respective) class, it checks if not None and fires
        an SQL INSERT query to persist (or rollback and some custom Exception)"""
        raise NotImplementedError("Class %s does not (yet) implement method persist()" %(self.__class__.__name__))
    def prettyPrint(self):
        # After thought: should be replaced by overriding __repr__
        """Optional function.
        Should return a pretty String to be displayed to the user"""

class Customer(Entity):
    id = 0
    name = ""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass


class Employee(Entity):
    id = 0
    name = ""
    franchise_id = 0
    manager_id = 0

    def __init__(self, name, franchise_id, manager_id):
        self.name = name
        self.manager_id = manager_id
        self.franchise_id = franchise_id


class Franchise(Entity):
    id = 0
    name = ""
    st_address = ""
    address = ""
    city = ""
    state = ""
    zip = ""
    manager_id = 0

    def __init__(self, name, st_address, address, city, state, zip, manager_id):
        self.name = name
        self.st_address = st_address
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.manager_id = manager_id


class Product(Entity):
    id = 0
    name = ""

    def __init__(self, name):
        self.name = name


class Service(Entity):
    id = 0
    name = ""

    def __init__(self, name):
        self.name = name


class Feedback(Entity):
    """abstract"""
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

class ProductFeedback(Feedback):
    def __repr__(self):
        pass

class ServiceFeedback(Feedback):
    def __repr__(self):
        pass

@app.route("/")
def index():
    return ""
