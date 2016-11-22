import sys

import Core.DB
import Core.app
import actions


# TODO: define the methods for db access and printing in separate class, keep only flow related code in cli.py

class Cli:
    def show_customer_feedback_entry(self):
        prompt = ' Enter customer ID: '
        cust_id = int(raw_input(prompt))

        # db = Core.DB.DB()
        # custList = db.query('Customer', '{"id" : "' + str(cust_id)
        #                     + '"}')
        # db.close()
        #
        # # Error cases
        #
        # if len(custList) > 1:
        #     print 'Fatal Error: Duplicate Customer IDs present!!!!'
        #     sys.exit(1)
        # elif len(custList) == 0:
        #     print 'No customer with ID ' + str(cust_id)
        #     print 'Try again'
        #     self.customerFeedback()
        #
        # # everything okay
        #
        # cust = custList[0]
        # print cust

        prompt = ("\n"
                  "		Enter action:\n"
                  "			1. Product feedback\n"
                  "			2. Service feedback\n"
                  "			0. back\n"
                  "		")
        inp = int(raw_input(prompt))
        if inp == 1:
            actions.insert_product_feedback(self, cust_id=cust_id)
        elif inp == 2:
            actions.insert_service_feedback(self, cust_id=cust_id)
        elif inp == 0:
            self.show_main_menu()
        else:
            print 'Invalid option. Exiting now'
            sys.exit(0)

            # TODO: implement back on inp == 0

    def show_emp_login(self):
        prompt = 'Enter employee ID: '
        emp_id = int(raw_input(prompt))
        db = Core.DB.DB()
        empList = db.query('Employee', '{"id" : "' + str(emp_id) + '"}')
        db.close()

        # Error cases

        if len(empList) > 1:
            print 'Fatal Error: Duplicate Employee IDs present!!!!'
            sys.exit(1)
        elif len(empList) == 0:
            print 'No employee with ID ' + str(emp_id)
            print 'Try again'
            self.show_emp_login()

        # everything okay

        emp = empList[0]
        print emp
        prompt = ("\n"
                  "Enter action:\n"
                  "     1. List all open action items\n"
                  "	    2. List all closed action items\n"
                  "	    3. List all action items\n"
                  "        		")
        inp = int(raw_input(prompt))
        if inp == 1:
            actions.list_action_items(self, action_status='open')
        elif inp == 2:
            actions.list_action_items(self, action_status='closed')
        elif inp == 3:
            actions.list_action_items(self)
        elif inp == 0:
            self.show_main_menu()
        else:
            print 'Invalid option. Exiting now'
            sys.exit(0)

            # TODO: implement back on inp ==0

    def show_manager_login(self):
        # for testing action item add ; in ui show manager option to create service action item or feedback action item
        db = Core.DB.DB()
        # db.insert_action_item(("2016-06-2", "2016-06-3", 4, 1, "finish", 3), "service")
        pass

    def show_main_menu(self):
        prompt = \
            """
		Enter action:
			1. Customer feedback
			2. Employee login
			3. Manager login

		"""
        inp = int(raw_input(prompt))  # TODO: handle invalid inp type
        if inp == None:
            print 'invalid input'
        elif inp == 1:
            self.show_customer_feedback_entry()
        elif inp == 2:
            self.show_emp_login()
        elif inp == 3:
            self.show_manager_login()
        else:
            print 'invalid input'


if __name__ == '__main__':
    cli = Cli()
    cli.show_main_menu()
