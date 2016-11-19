import sys

import Core.DB
import Core.app
import actions


# TODO: define the methods for db access and printing in separate class, keep only flow related code in cli.py

class Cli:
    def customerFeedback(self):
        prompt = ' Enter customer ID: '
        cust_id = int(raw_input(prompt))
        """
        db = Core.DB.DB()
        custList = db.query('Customer', '{"id" : "' + str(cust_id)
                            + '"}')
        db.close()

        # Error cases

        if len(custList) > 1:
            print 'Fatal Error: Duplicate Customer IDs present!!!!'
            sys.exit(1)
        elif len(custList) == 0:
            print 'No customer with ID ' + str(cust_id)
            print 'Try again'
            self.customerFeedback()

        # everything okay

        cust = custList[0]
        print cust
        """
        prompt = ("\n"
                  "		Enter action:\n"
                  "			1. Product feedback\n"
                  "			2. Service feedback\n"
                  "			0. back\n"
                  "		")
        inp = int(raw_input(prompt))
        if inp == 1:
            actions.productFeedback(self, cust_id=cust_id)
        elif inp == 2:
            actions.serviceFeedback(self, cust_id=cust_id)
        else:
            print 'Invalid option. Exiting now'
            sys.exit(0)

            # TODO: implement back on inp == 0

    def empLogin(self):
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
            self.empLogin()

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
            actions.listActionItems(self, action_status='open')
        elif inp == 2:
            actions.listActionItems(self, action_status='closed')
        elif inp == 3:
            actions.listActionItems(self)
        else:
            print 'Invalid option. Exiting now'
            sys.exit(0)

            # TODO: implement back on inp ==0

    def mgrLogin(self):
        pass

    def mainLoop(self):
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
            self.customerFeedback()
        elif inp == 2:
            self.empLogin()
        elif inp == 3:
            self.mgrLogin()
        else:
            print 'invalid input'


if __name__ == '__main__':
    cli = Cli()
    cli.mainLoop()
