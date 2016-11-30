import re
import logging
import MySQLdb as mysql

from app import *

# TODO refactor: put below params in .properties file
DB_USERNAME = 'root'
DB_PASSWORD = 'makmakmak'
DB_NAME = 'cmpe138_project_team3_feedback'


class DB(object):
    _queryString = "SELECT {attributes} FROM {table} {condition}"

    def __init__(self):
        self.connection = mysql.connect(user=DB_USERNAME, passwd=DB_PASSWORD,
                                        db=DB_NAME)
        self.logFile = 'DB.log'
        self._setupLogging()

    def _setupLogging(self):
        self.logger = logging.getLogger('DB')
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(self.logFile)
        fh.setLevel(logging.DEBUG)

        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)5s - '
                                      '%(levelname)7s - %(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    def close(self):
        """close connection"""
        self.connection.close()

    def _execute(self, cursor, queryString):
        self.logger.debug("Executing query '%s'" % queryString)
        try:
            retval = cursor.execute(queryString)
            if getattr(cursor, 'rowcount', None):
                logging.debug("Returned %s rows" % cursor.rowcount)
            return retval
        except:
            logging.exception("Caught execption while executing query, '%s'" %
                              queryString)
            raise

    def query(self, table, paramsJson=None, attributes="*"):
        """Will execute the query and return rows as a list of objects.
        Return empty list in case of No results"""
        queryString = self.formatQuerySting(table, paramsJson, attributes)
        cursor = self.connection.cursor(mysql.cursors.DictCursor)
        self._execute(cursor, queryString)
        rows = cursor.fetchall()
        retval = []
        for row in rows:
            retval.append(self._getObject(table, row))
        return retval

    def _getObject(self, table, args):
        # TODO use consistent attribute names and order across python classes
        # and SQL tables so that we can dynamically generate objects and
        # we don't need to write a dirty highly coupled if else ladder like
        # the one below :(
        if table == 'customer':
            return Customer(args[1] + " " + args[2])
        elif table == 'product':
            return Product(args[1])
        elif table == 'service':
            return Service(args[1])
        elif table == 'service_feedback':
            return ServiceFeedback(rating=args[1], comments=args[2],
                                   customer_id=args[3], item_id=args[4],
                                   franchise_id=args[5])
        elif table == 'product_feedback':
            return ProductFeedback(rating=args[1], customer_id=args[2],
                                   item_id=args[3], comments=args[4],
                                   franchise_id=args[5])
        elif table == 'employee':
            return Employee(name=args["f_name"] + args["l_name"],
                            franchise_id=args["franchise_id"],
                            manager_id=args["manager_id"])
        elif table == 'franchise':
            return Franchise(name=args[1], st_address=args[2], address=args[3],
                             city=args[4], state=args[5], zip=args[6],
                             manager_id=args[7])
        elif table == "action_items":
            return ActionItems(action_item_id=args["action_item_id"],
                               action_status=args["action_status"],
                               start_date=args["start_date"],
                               end_date=args["end_date"],
                               )

    @classmethod
    def formatQuerySting(clss, table, paramsJson, attributes):
        """
        Return a SQL query string for selecting attributes
        """
        assert type(table) == str
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
            self._execute(cursor,
                          "INSERT INTO product_feedback(ratings,customer_id,"
                          "product_id,comments,franchise_id)VALUES "
                          "(%s,%s,%s,%s,%s)",
                          values)
        else:
            self._execute(cursor,
                          "INSERT INTO service_feedback(ratings,customer_id,"
                          "service_id,"
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
        self._execute(cursor, "SELECT * from sold_by  where product_id =%s AND"
                      " franchise_id =%s",
                      (check_id, franchise_id))

        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_franchise_exists(self, franchise_id):
        cursor = self.connection.cursor()
        self._execute(cursor, "SELECT * from franchise  where "
                      "franchise_id =%s",
                      (franchise_id,))
        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_service_exists(self, service_id):
        cursor = self.connection.cursor()
        self._execute(cursor, "SELECT * from service where service_id =%s",
                      (service_id,))
        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_feedback_id_action_exists(self, feedback_id, feedback_name):
        cursor = self.connection.cursor()
        if feedback_name == "service":
            self._execute(cursor, "SELECT * from service where "
                          "service_feedback_id =%s", (feedback_id,))

        self._execute(cursor, "SELECT * from service where "
                      "product_feedback_id =%s",
                      (feedback_id,))

        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_customer_id(self, customer_id):
        cursor = self.connection.cursor()
        self._execute(cursor, "SELECT * from customer  where customer_id =%s",
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
    def insert_action_item(self, values, feedback_type):
        try:
            cursor = self.connection.cursor()
            if feedback_type == "product":
                item_type = "product_feedback_id"
            else:
                item_type = "service_feedback_id"

            self._execute(cursor,
                          "INSERT INTO "
                          "action_items(start_date,end_date,created_by,"
                          "assigned_to,comments," + item_type +
                          ")VALUES(%s,%s,%s,%s,%s,%s)", values)
            self.connection.commit()
        except mysql.Error:
            print("Invalid ids entered")
        finally:
            self.close()

    def update_action_item(self, values):
        try:
            cursor = self.connection.cursor()
            self._execute(cursor,
                          "UPDATE action_items set action_status=%s where "
                          "action_item_id=%s", values)
            self.connection.commit()
        except mysql.Error:
            print("Invalid ids entered")
        finally:
            self.close()
