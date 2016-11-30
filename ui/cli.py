from __future__ import print_function

import getpass
import sys

sys.path.append('..')

import Core.DB
import Core.app
import actions
import utils
import logging


# TODO: define the methods for db access and printing in separate class,
# keep only flow related code in cli.py
class Cli:
    def show_customer_feedback_entry(self):
        customer_id = None
        custList = None
        while 1:
            prompt = ' Enter customer ID (or "new"): '
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1('../..')
            elif inp.isdigit():
                customer_id = int(inp)
                if customer_id == 0:
                    return 0
                else:  # success case
                    db = Core.DB.DB()
                    custList = db.query('customer', {"customer_id": str(customer_id)})
                    db.close()
                    # Error cases
                    if len(custList) > 1:
                        print('Internal Error. Please contact administrator\n')
                        print('Fatal Error: Duplicate Customer IDs present!!!!')
                        sys.exit(1)
                    elif len(custList) == 0:
                        print('No customer with ID ' + str(customer_id))
                        print('\nTry again')
                        continue
                    elif len(custList) == 1:  # success
                        break
            elif inp == "new":
                new_id = actions.signup()
                print('Your customer ID is: ' + str(new_id))
                continue
            else:
                print('Customer ID is a numeric ID number given to each '
                      'customer.\n'
                      'Please try again.\n')

        # everything okay
        cust = custList[0]
        cust.print_item()
        while 1:
            feedback_type_choice_next_operation = None
            prompt = ("\n"
                      "   Enter action:\n"
                      "     1. Product feedback\n"
                      "     2. Service feedback\n"
                      "     0. back\n"
                      "   ")
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                choice = int(inp)
                if choice == 1:
                    feedback_type_choice_next_operation = \
                        actions.insert_product_feedback(
                            self, customer_id=customer_id)
                elif choice == 2:
                    feedback_type_choice_next_operation = \
                        actions.insert_service_feedback(
                            self, customer_id=customer_id)
                elif choice == 0:
                    return 0
                else:
                    print('Invalid choice. Please try choosing from'
                          ' the options given.\n')
            else:
                print('Please enter the number shown in front of the'
                      ' choices.\n')
            if feedback_type_choice_next_operation == 1:
                return 1
            elif feedback_type_choice_next_operation == 0:
                continue

    def show_emp_login(self):
        employee_id = None
        emp_list = None
        while 1:
            prompt = 'Enter employee ID: '
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                employee_id = int(inp)
                if employee_id == 0:
                    return 0
                else:
                    db = Core.DB.DB()
                    emp_list = db.query(
                        'employee', {"employee_id": str(employee_id)})
                    db.close()

                    if len(emp_list) > 1:
                        print('Internal Error. Please try contacting '
                              'the administrator.')
                        return 1
                    elif len(emp_list) == 0:
                        print('No employee with ID ' + str(employee_id) + '\n'
                                                                          'Try again')
                        continue
                    else:
                        break
            else:
                print('Employee ID is a numeric ID number given to '
                      'each employee.\n'
                      'Please try again.\n')

        emp = emp_list[0]

        while 1:
            emp.print_employee_entity()
            print('Home.\n'
                  'Welcome !\n')
            prompt = ("\n"
                      "Enter action:\n"
                      "     1. List all open action items\n"
                      "     2. List all closed action items\n"
                      "     3. List all action items\n"
                      "     >      ")
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                choice = int(inp)
                if choice == 0:
                    return 0
                items = []
                if choice == 1:
                    items = actions.list_action_items(self, employee_id, action_status=0)
                elif choice == 2:
                    items = actions.list_action_items(self, employee_id, action_status=1)
                elif choice == 3:
                    items = actions.list_action_items(self, employee_id)

                if len(items) > 0:
                    for item in items:
                        print(item.print_item())
                else:
                    print("No items available")

                break

            else:
                print('Invalid choice. Please try choosing from the '
                      'options given.\n')

    def show_manager_login(self):
        # TODO by mgr, franchise for all 7 options
        # for testing action item add ; in ui show manager option to create
        # service action item or feedback action item
        # db = Core.DB.DB()
        # db.insert_action_item(("2016-06-2", "2016-06-3", 4, 1, "finish", 1), "product")

        # @author Gurnoor
        # I did not understand what/ why is happening above in this function.

        manager_id = None
        mgr_list = None
        while 1:
            prompt = 'Enter manager ID: '
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                manager_id = int(inp)
                if manager_id == 0:
                    return 0
                else:
                    db = Core.DB.DB()
                    mgr_list = db.query(
                        'employee', {"employee_id": str(manager_id),
                                     "manager_id": ""})
                    db.close()

                    if len(mgr_list) > 1:
                        print('Internal Error. Please try contacting '
                              'the administrator.')
                        return 1
                    elif len(mgr_list) == 0:
                        print('No manager with ID ' + str(manager_id) + '\n'
                                                                        'Try again')
                        continue
                    else:
                        break
            else:
                print('Manager ID is a numeric ID number given to '
                      'each manager.\n'
                      'Please try again.\n')

        tries = 3
        while 1:
            prompt = 'Enter password: '
            pswd = getpass.getpass(prompt)
            if utils.checkPass('employee', manager_id, pswd) == False:
                tries -= 1
                if tries != 0:
                    print("Incorrect password. Try again\n"
                          + str(tries) + " tries left")
                else:
                    print("Maximum tries exceeded. Exiting now...")
                    return 0

            else:
                break  # everything okay, proceed further

        emp = mgr_list[0]
        emp.print_employee_entity()
        print('Home.\n'
              'Welcome !\n')
        while 1:

            prompt = ("\n"
                      "Enter action:\n"
                      "     1. List all unassigned feedbacks\n"
                      "     2. List all feedbacks\n"
                      "     3. List all open action items\n"
                      "     4. List all closed action items\n"
                      "     5. List all action items\n"
                      "     6. Assign an action item\n"
                      "     7. Close an action item\n"
                      "     #. Exit\n"
                      "     0. Back\n"
                      "     >      ")
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                choice = int(inp)
                if choice == 0:
                    return 0
                if choice not in (6, 7):
                    items = []
                    if choice == 1:
                        items = actions.list_unassigned_feedbacks(self, emp.franchise_id)
                    elif choice == 2:
                        items = actions.list_all_feedbacks(self, emp.franchise_id)
                    elif choice == 3:
                        items = actions.list_fran_action_items(self, action_status=0,
                                                               manager_id=emp.id)
                    elif choice == 4:
                        items = actions.list_fran_action_items(self, action_status=1,
                                                               manager_id=emp.id)
                    elif choice == 5:
                        items = actions.list_fran_action_items(self,
                                                               manager_id=emp.id)
                    else:
                        print('Invalid choice. Please try choosing from the '
                              'options given.\n')

                    if len(items) > 0:
                        for item in items:
                            print(item.print_item())
                    else:
                        print("No items available")

                    continue
                else:  # choice in (6, 7)
                    if choice == 6:
                        # Assign an action item
                        actions.insert_action_item(
                            manager_id=emp.id,
                            franchise_id=emp.franchise_id)
                    elif choice == 7:
                        actions.close_action_item(manager_id=emp.id)
                    continue

    def show_main_menu(self):
        while 1:
            main_menu_next_operation = None
            prompt = ("\n"
                      "Press # at any screen to exit\n"
                      "Press 0 at any screen to go back\n"
                      "Enter action:\n"
                      "     1. Customer feedback\n"
                      "     2. Employee login\n"
                      "     3. Manager login\n"
                      "     #. Exit\n"
                      "     0. Exit\n"
                      "> ")
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                choice = int(inp)
                if choice == 1:
                    main_menu_next_operation = \
                        self.show_customer_feedback_entry()
                elif choice == 2:
                    main_menu_next_operation = self.show_emp_login()
                elif choice == 3:
                    main_menu_next_operation = self.show_manager_login()
                elif choice == 0:
                    return 1
                else:
                    print(
                        'Invalid choice. Please try choosing from the options '
                        'given.\n')
            else:
                print('Please enter the number shown in front of the'
                      ' choices.\n')
            if main_menu_next_operation == 1:
                return 1
            elif main_menu_next_operation == 0:
                continue


def show_owner_login(self):
    prompt = 'Enter employee ID: '
    emp_id = int(raw_input(prompt))
    db = Core.DB.DB()
    empList = db.query('Employee', '{"id" : "' + str(emp_id) + '"}')
    db.close()

    # Error cases
    if len(empList) > 1:
        print('Fatal Error: Duplicate Employee IDs present!!!!')
        sys.exit(1)
    elif len(empList) == 0:
        print('No employee with ID ' + str(emp_id))
        print('Try again')
        self.show_emp_login()

    # everything okay

    emp = empList[0]
    prompt = ("\n"
              "Enter action:\n"
              "     1. List all open action items\n"
              "     2. List all closed action items\n"
              "     3. List all action items\n"
              "     >       ")
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
        print('Invalid option. Exiting now')
        sys.exit(0)

        # TODO: implement back on inp ==0


def setupLogging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('rootLogger.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)5s - '
                                  '%(levelname)7s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


if __name__ == '__main__':
    setupLogging()
    while 1:
        cli = Cli()
        next_operation = cli.show_main_menu()
        if next_operation == 1:
            break
        elif next_operation == 0:
            continue
