import MySQLdb as mysql
import re


class DB(object):
    _queryString = "SELECT {attributes} FROM {table} {condition}"

    def __init__(self):
        self.connection = mysql.connect(user="root", passwd="admin",
                                        db="cmpe138_project_team3_feedback")

    def close(self):
        """close connection"""
        self.connection.close()

    def query(self, table, paramsJson=None, attributes="*"):
        """Will execute the query and return rows as a list of objects.
        Return empty list in case of No results"""
        queryString = self.formatQuerySting(table, paramsJson, attributes)
        cursor = self.connection.cursor()
        cursor.execute(queryString)
        retval = None  # TODO get values
        self.close()
        return retval

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
        return True

    def check_franchise_exists(self, franchise_id):
        return True

    def check_service_exists(self, service_id):
        return True

    def check_feedback_id_action_exists(self, feedback_id, column_id):
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

            cursor.execute(
                "INSERT INTO action_items(start_date,end_date,created_by,"
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
            cursor.execute("UPDATE action_items set action_status=%s where "
                           "action_item_id=%s", values)
            self.connection.commit()
        except mysql.Error:
            print("Invalid ids entered")
        finally:
            self.close()
