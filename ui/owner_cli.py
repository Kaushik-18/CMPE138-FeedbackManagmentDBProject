import sys
sys.path.append('..')
import Core
import actions


class owner_cli:
    def show_owner_login(self):
        while 1:
            prompt_username = 'Enter owner username: '
            inp_username = raw_input(prompt_username)
            if inp_username == '1':
                prompt_paswsword = 'Enter your password: '
                inp_password = raw_input(prompt_paswsword)
                if inp_password == '1':
                    break
                else:
                    print('Invalid password. Please try again!')
            else:
                print('Invalid username. Please try again!')

        while 1:
            main_menu_next_operation = None
            prompt = ("\n"
                      "Press # at any screen to exit\n"
                      "Press 0 at any screen to go back\n"
                      "Enter action:\n"
                      "     1. Average Ratings\n"
                      "     2. Product wise Average Rating\n"
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
                    main_menu_next_operation = actions.show_average_rating_all_products(self)
                elif choice == 2:
                    main_menu_next_operation = actions.show_product_wise_rating(self)
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



if __name__ == '__main__':
    while 1:
        cli = owner_cli()
        next_operation = cli.show_owner_login()
        if next_operation == 1:
            break
        elif next_operation == 0:
            continue
