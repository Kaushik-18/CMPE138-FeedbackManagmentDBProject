import re

import MySQLdb as mysql

from app import *

# TODO refactor: put below params in .properties file
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'cmpe138_project_team3_feedback'


class DB(object):
    _queryString = "SELECT {attributes} FROM {table} {condition}"

    def __init__(self):
        self.connection = mysql.connect(user=DB_USERNAME, passwd=DB_PASSWORD,
                                        db=DB_NAME)

    def close(self):
        """close connection"""
        self.connection.close()

    def query(self, table, paramsJson=None, attributes="*"):
        """Will execute the query and return rows as a list of objects.
        Return empty list in case of No results"""
        queryString = self.formatQuerySting(table, paramsJson, attributes)
        cursor = self.connection.cursor(mysql.cursors.DictCursor)
        cursor.execute(queryString)

        rows = cursor.fetchall()
        retval = []
        for row in rows:  # row is a a dict here
            retval.append(self._getObject(table, row))
        return retval

    def _getObject(self, table, args):
        # TODO use consistent attribute names and order across python classes
        # and SQL tables so that we can dynamically generate objects and
        # we don't need to write a dirty highly coupled if else ladder like
        # the one below :(
        row = args
        if table == 'customer':
            cust = Customer(name=args['f_name'] + " " + args['l_name'])
            cust.id = args['customer_id']
            return cust
        elif table == 'product':
            prod = Product(name=args['product_name'])
            prod.id = args['product_id']
            return prod
        elif table == 'service':
            serv = Service(name=args['service_name'])
            serv.id = args['service_id']
            return serv
        elif table == 'service_feedback':
            service_feedback = ServiceFeedback()
            return service_feedback.from_dict(row)
        elif table == 'product_feedback':
            product_feedback = ProductFeedback()
            return product_feedback.from_dict(row)
        elif table == 'employee':
            return Employee(name=args["f_name"] + args["l_name"], franchise_id=args["franchise_id"],
                            manager_id=args["manager_id"])
        elif table == 'franchise':
            fran = Franchise()
            fran = fran.from_dict(init_dict=row)
            return fran
            # return Franchise(name=args['name'], st_address=args[2], address=args[3],
            #                 city=args[4], state=args[5], zip=args[6],
            #                manager_id=args[7])
        elif table == "action_items":
            action = ActionItems()
            action = action.from_dict(init_dict=row)
            return action
            # return ActionItems(action_item_id=args["action_item_id"], action_status=args["action_status"],
            #                   start_date=args["start_date"], end_date=args["end_date"],
            #                   )
        elif table == "Logins":
            logins = Logins()
            logins = logins.from_dict(init_dict=row)
            logins.pswd = row['pass']
            return logins

    @classmethod
    def formatQuerySting(clss, table, paramsJson, attributes):
        """
        Return a SQL query string for selecting attributes
        """
        assert type(table) == str
        if paramsJson is not None:
            assert type(paramsJson) == dict
        assert type(attributes) == str
        assert re.match("\s*(\*|(\w+,?\s*)+)\s*", attributes)

        if paramsJson:
            condition = "WHERE "
            flag = False
            for key in paramsJson:
                temp = None
                # handle 'X is null query'
                if (paramsJson[key] is None) or (paramsJson[key] == ""):
                    temp = "%s is null" % (key)
                else:
                    if type(paramsJson[key]) is str:
                        temp = '%s = "%s"' % (key, paramsJson[key])
                    else:
                        temp = "%s = %s" % (key, paramsJson[key])
                if flag:
                    condition += " AND " + temp
                else:
                    condition += temp
                    flag = True
        else:
            condition = ""

        return clss._queryString.format(attributes=attributes, table=table,
                                        condition=condition)

    def insert_feedback_record(self, tablename, values):
        cursor = self.connection.cursor()
        if tablename == "product":
            cursor.execute(
                "INSERT INTO product_feedback(ratings,customer_id,"
                "product_id,comments,franchise_id)VALUES (%s,%s,%s,%s,%s)",
                values)
        else:
            cursor.execute(
                "INSERT INTO service_feedback(ratings,customer_id,service_id,"
                "comments,franchise_id)VALUES (%s,%s,%s,%s,%s)",
                values)
        self.connection.commit()
        self.close()

    def update_record(self):
        pass

    # TODO add query to check if product id is available for particular
    # franchise record
    def check_product_record(self, check_id, franchise_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from sold_by  where product_id =%s AND franchise_id =%s",
                       (check_id, franchise_id))

        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_franchise_exists(self, franchise_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from franchise  where franchise_id =%s",
                       (franchise_id,))
        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_service_exists(self, service_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from service where service_id =%s",
                       (service_id,))
        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_feedback_id_action_exists(self, feedback_id, feedback_name):
        cursor = self.connection.cursor()
        if feedback_name == "service":
            cursor.execute("SELECT * from service where service_feedback_id =%s", (feedback_id,))

        cursor.execute("SELECT * from service where product_feedback_id =%s",
                       (feedback_id,))

        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_customer_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from customer  where customer_id =%s",
                       (customer_id,))
        if cursor.rowcount == 1:
            return True
        else:
            return False

    # possible issue here ...we can add same feedback id in action item ...
    # 1 solution is to make feedback id columns unique and null,but some
    #   suggest this is actually a bug in MySql
    # 2 solution is to check if feedback id is already entered using above
    #   function
    def insert_action_item(self, values, feedback_type, manager_id):
        try:
            cursor = self.connection.cursor()
            if feedback_type == "product":
                item_type = "product_feedback_id"
            else:
                item_type = "service_feedback_id"

            cursor.execute(
                "INSERT INTO action_items(start_date,end_date,created_by,"
                "assigned_to,comments, " + item_type +
                ")VALUES(%s,%s,%s,%s,%s,%s)", values)
            self.connection.commit()
        except mysql.Error:
            print("Invalid ids entered")
        finally:
            self.close()

    def update_action_item(self, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE action_items set action_status=%s where "
                           "action_item_id=%s", values)
            self.connection.commit()
        except mysql.Error:
            print("Invalid ids entered")
        finally:
            self.close()

    def insert_new_customer(self, values):
        id = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO customer(f_name, l_name)"
                " VALUES(%s,%s)", values)
            id = cursor.lastrowid
            self.connection.commit()
        except mysql.Error:
            print ("Invalid IDs entered")
        finally:
            self.close()
        return id

    def fetch_average_ratings(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT product_feedback.franchise_id, AVG(product_feedback.ratings), AVG(service_feedback.ratings) FROM product_feedback LEFT JOIN service_feedback ON product_feedback.franchise_id = service_feedback.franchise_id GROUP BY franchise_id UNION SELECT service_feedback.franchise_id, AVG(product_feedback.ratings), AVG(service_feedback.ratings) FROM product_feedback RIGHT JOIN service_feedback ON product_feedback.franchise_id = service_feedback.franchise_id GROUP BY franchise_id")
        if cursor.rowcount > 0:
            return cursor.fetchall()
        else:
            return []

    def fetch_product_ratings(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT product_id, AVG(ratings) FROM product_feedback GROUP BY product_id")
        if cursor.rowcount > 0:
            return cursor.fetchall()
        else:
            return []

    def select_unassgn_fb(self, type, franchise_id):
        table = None
        column = None
        franchise_id = str(franchise_id)
        if type == 'product':
            table = 'product_feedback'
            column = 'product_feedback_id'
        elif type == 'service':
            table = 'service_feedback'
            column = 'service_feedback_id'
        query = "SELECT * FROM " + table + \
                " WHERE franchise_id = " + franchise_id + \
                " AND " + table + "." + column + " not in (" + \
                " SELECT action_items." + column + " FROM action_items" \
                                                   " WHERE action_items." + column + " is not null)"

        retval = []
        cursor = self.connection.cursor()
        cursor = self.connection.cursor(mysql.cursors.DictCursor)
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            retval.append(self._getObject(table, row))

        return retval
