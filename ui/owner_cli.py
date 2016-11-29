import Core
import actions
import sys


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



show_owner_login()
