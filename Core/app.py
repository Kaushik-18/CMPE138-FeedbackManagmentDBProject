import Core.DB


class Entity(object):
    """Abstract base class for all Entities"""

    def persist(self):
        """for all variable in the (respective) class,
        it checks if not None and fires
        an SQL INSERT query to persist (or rollback and
        some custom Exception)"""
        # print ("inside Entity.persist()")
        # raise NotImplementedError("Class %s does not (yet) implement"
        #                           "method persist()" %
        #                           (self.__class__.__name__))

        # def prettyPrint(self):
        #     # After thought: should be replaced by overriding __str__
        #     """Optional function.
        #     Should return a pretty String to be displayed to the user"""


class Customer(Entity):
    def __init__(self, name):
        self.name = name
        self.id = None

    def __repr__(self):
        pass


class Employee(Entity):
    def __init__(self, name, franchise_id, manager_id):
        self.id = None
        self.name = name
        self.manager_id = manager_id
        self.franchise_id = franchise_id


class Franchise(Entity):
    def __init__(self, name, st_address, address, city, state, zip,
                 manager_id):
        self.id = None
        self.name = name
        self.st_address = st_address
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.manager_id = manager_id


class Product(Entity):
    def __init__(self, name):
        self.id = None
        self.name = name


class Service(Entity):
    def __init__(self, name):
        self.id = None
        self.name = name


class Feedback(Entity):
    def __init__(self, rating, comments, customer_id, item_id, franchise_id):
        self.rating = rating
        self.comments = comments
        self.customer_id = customer_id
        self.item_id = item_id
        self.franchise_id = franchise_id


class ProductFeedback(Feedback):
    def __init__(self, rating=0, comments="", customer_id=0, item_id=0,
                 franchise_id=0):
        super(ProductFeedback, self).__init__(rating, comments, customer_id,
                                              item_id, franchise_id)

    def __str__(self):
        pass

    def persist(self):
        db = Core.DB.DB()
        db.insert_feedback_record("product",
                                  (self.rating, self.customer_id, self.item_id,
                                   self.comments, self.franchise_id))


class ServiceFeedback(Feedback):
    def __init__(self, rating=0, comments="", customer_id=0, item_id=0,
                 franchise_id=0):
        super(ServiceFeedback, self).__init__(rating, comments, customer_id,
                                              item_id, franchise_id)

    def __str__(self):
        pass

    def persist(self):
        db = Core.DB.DB()
        db.insert_feedback_record("service",
                                  (self.rating, self.customer_id, self.item_id,
                                   self.comments, self.franchise_id))
