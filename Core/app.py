from abc import ABCMeta

import Core.DB


class Entity(object):
    __metaclass__ = ABCMeta

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

    def printItem(self):
        print("Customer ID: ", self.id
              , "Customer Name: ", self.name)


class Employee(Entity):
    def __init__(self, name, franchise_id, manager_id):
        self.id = None
        self.name = name
        self.manager_id = manager_id
        self.franchise_id = franchise_id

    def  printEmployee(self):
        print self.name, "  manager id : ", self.manager_id, " franchise id : ", self.franchise_id


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

    def printItem(self):
        pass  # TODO

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

    def printItem(self):
        pass  # TODO

    def persist(self):
        db = Core.DB.DB()
        db.insert_feedback_record("service",
                                  (self.rating, self.customer_id, self.item_id,
                                   self.comments, self.franchise_id))


class ActionItems:
    def __init__(self, action_item_id, start_date, end_date, action_status,assigned_to= None,
                 created_by=None, comments=None, service_feedback_id=None, product_feedback_id=None):
        self.assigned_to = assigned_to
        self.action_item_id = action_item_id
        self.start_date = start_date
        self.end_date = end_date
        self.service_feedback_id = service_feedback_id
        self.product_feedback_id = product_feedback_id
        self.comments = comments
        self.created_by = created_by
        self.action_status = action_status

    def printItem(self):
        print (
            "ID : ", self.action_item_id, " comments : ", self.comments, "start date : ", self.start_date,
            "end date : ",
            self.end_date)
