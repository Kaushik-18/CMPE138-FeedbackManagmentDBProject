from __future__ import print_function
import sys

import Core.DB
import Core.app
import actions


# TODO: define the methods for db access and printing in separate class,
# keep only flow related code in cli.py

class Cli:
    def show_customer_feedback_entry(self):
        customer_id = None
        while 1:
            prompt = ' Enter customer ID: '
            inp = raw_input(prompt)
            if inp is None:
                continue
            elif inp == '#':
                return 1
            elif inp.isdigit():
                customer_id = int(inp)
                if customer_id == 0:
                    return 0
                else:
                    break
            else:
                print('Customer ID is a numeric ID number given to each '
                      'customer.\n'
                      'Please try again.\n')

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
            emp.printEmployee()
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
                    items = actions.list_action_items(self, employee_id,action_status=0)
                elif choice == 2:
                    items = actions.list_action_items(self, employee_id,action_status=1)
                elif choice == 3:
                    items = actions.list_action_items(self)

                if len(items) > 0:
                    for item in items:
                        print(item.printItem())
                else:
                    print("No items available")

                break

            else:
                print('Invalid choice. Please try choosing from the '
                      'options given.\n')

    def show_manager_login(self):
        # for testing action item add ; in ui show manager option to create
        # service action item or feedback action item
        db = Core.DB.DB()
        db.insert_action_item(("2016-06-2", "2016-06-3", 4, 1, "finish", 1), "product")
        pass

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
                    return 0
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


if __name__ == '__main__':
    while 1:
        cli = Cli()
        next_operation = cli.show_main_menu()
        if next_operation == 1:
            break
        elif next_operation == 0:
            continue
