import Core.DB
import Core.app


def insert_product_feedback(self, customer_id):
    while 1:
        fb = Core.app.ProductFeedback()
        db = Core.DB.DB()
        fb.customer_id = customer_id
        franchise_id_input = None
        while 1:
            franchise_id_input = raw_input("Enter franchise id: ")
            if franchise_id_input.isdigit():
                break
            elif franchise_id_input == '#':
                return 1
            else:
                print('Franchise ID is the numeric ID number '
                      'given to each franchise.\n'
                      'Please try again.')
        fb.franchise_id = int(franchise_id_input)
        if db.check_franchise_exists(fb.franchise_id):
            item_id_input = None
            while 1:
                item_id_input = raw_input("Enter product ID: ")
                if item_id_input.isdigit():
                    break
                elif item_id_input == '#':
                    return 1
                else:
                    print('Item ID is the numeric ID number given '
                          'to each item.\n'
                          'Please try again.')
            fb.item_id = int(item_id_input)
            if db.check_product_record(fb.item_id, fb.franchise_id):
                rating_input = None
                while 1:
                    rating_input = raw_input("Enter rating (1 to 5): ")
                    if rating_input.isdigit():
                        if int(rating_input) > 5 or int(rating_input) < 0:
                            print('Ratings should be numeric value between 0 '
                                  'to 5.\n'
                                  'Please try again.')
                        else:
                            break
                    elif rating_input == '#':
                        return 1
                    else:
                        print('Ratings should be numeric value between 0 '
                              'to 5.\n'
                              'Please try again.')
                fb.rating = int(rating_input)
                fb.comments = raw_input("Enter feedback: ")
                conf = raw_input("Submit the above feedback? (yes or no): ")
                if conf == "yes":
                    fb.persist()
                    return 1
                else:
                    print('Feedback submission cancelled. Exiting now...')
            else:
                print (
                    "Product not available for this franchise.Please check "
                    "product id or franchise id !")
        else:
            print ("Invalid franchise id.")
        db.close()


def insert_service_feedback(self, customer_id):
    while 1:
        fb = Core.app.ServiceFeedback()
        db = Core.DB.DB()
        fb.customer_id = customer_id
        franchise_id_input = None
        while 1:
            franchise_id_input = raw_input("Enter franchise id: ")
            if franchise_id_input.isdigit():
                break
            elif franchise_id_input == '#':
                return 1
            else:
                print('Franchise ID is the numeric ID number given to each '
                      'franchise.\n'
                      'Please try again.')
        fb.franchise_id = int(franchise_id_input)
        if db.check_franchise_exists(fb.franchise_id):
            item_id_input = None
            while 1:
                item_id_input = raw_input("Enter service ID: ")
                if item_id_input.isdigit():
                    break
                elif item_id_input == '#':
                    return 1
                else:
                    print('Item ID is the numeric ID number given to each item'
                          '.\nPlease try again.')
            fb.item_id = int(item_id_input)
            if db.check_service_exists(fb.item_id):
                rating_input = None
                while 1:
                    rating_input = raw_input("Enter rating (1 to 5): ")
                    if rating_input.isdigit():
                        if int(rating_input) > 5 or int(rating_input) < 0:
                            print('Ratings should be numeric value between 0 '
                                  'to 5.\n'
                                  'Please try again.')
                        else:
                            break
                    elif rating_input == '#':
                        return 1
                    else:
                        print('Ratings should be numeric value between 0 to 5.'
                              '\nPlease try again.')
                fb.rating = int(rating_input)
                fb.comments = raw_input("Enter feedback: ")
                conf = raw_input("Submit the above feedback? (yes or no): ")
                if conf == "yes":
                    fb.persist()
                    return 1
                else:
                    print('Feedback submission cancelled. Exiting now...')
            else:
                print ("Invalid service ID for this franchise")
        else:
            print ("Invalid Feedback ID ")
        db.close()


def list_action_items(self, employee_id=None, action_status=None):
    db = Core.DB.DB()
    if employee_id is not None:
        action_dict = {"assigned_to": employee_id}
        if action_status is not None:
            action_dict.update({"action_status": action_status})
        items = db.query("action_items", action_dict)
        return items
    else:
        items = db.query("action_items")
        return items


def list_all_feedbacks(self, franchise_id=None):
    db = Core.DB.DB()
    feedback_types = ["product_feedback", "service_feedback"]
    results = []
    for feedback_type in feedback_types:
        if franchise_id is not None:
            results_part = db.query(table=feedback_type, paramsJson={"franchise_id": int(franchise_id)})
        else:
            results_part = db.query(table=feedback_type)

        if (results_part is None) or (len(results_part) == 0):
            continue
        else:
            for result in results_part:
                results.append(result)
    db.close()
    return results


def list_unassigned_feedbacks(self, franchise_id):
    db = Core.DB.DB()
    unassigned_prod_feedbacks = db.select_unassgn_fb('product', franchise_id=franchise_id)
    unassigned_serv_feedbacks = db.select_unassgn_fb('service', franchise_id=franchise_id)

    unassigned_prod_feedbacks.extend(unassigned_serv_feedbacks)
    return unassigned_prod_feedbacks


def insert_action_item(self, manager_id, franchise_id):
    """Assign an action item"""
    db = Core.DB.DB()

    # TODO: mustDo: format date
    start_date = raw_input("Enter start date: ")
    end_date = raw_input("Enter end date: ")

    created_by = manager_id  # input("Enter created by: ")
    # TODO beautify: print employees in his franchise
    while 1:
        assigned_to = input("Enter the ID of assigned employee: ")
        results = db.query(table='employee', paramsJson={"employee_id": assigned_to,
                                                         "franchise_id": franchise_id})
        if len(results) == 1:
            break
        elif len(results) == 0:
            print('The employee ' + str(assigned_to) + ' is not in your franchise ' + str(franchise_id))
            print ('\nTry again.')
            continue
    comm = raw_input("Enter comments: ")
    fb_type = raw_input("Enter feedback type (product or service): ")
    fb_id = input("Enter feedback id: ")
    values = (start_date, end_date, created_by, assigned_to,
              comm, fb_id)
    db.insert_action_item(values=values,
                          feedback_type=fb_type)


def close_action_item(self, manager_id):
    db = Core.DB.DB()
    action_items = db.query(table="action_items")
    for action in action_items:
        action.printItem()
    print("---------------------")

    # check if s/he is closing the action created by himself
    while 1:
        action_item_id = raw_input("Select an action item from the above list: ")
        results = db.query(table='action_items', paramsJson={'created_by': manager_id})
        if len(results) == 1:
            break
        elif len(results) == 0:
            print('The action item ' + str(action_item_id) + ' was not created by you.')
            print('\nTry again')
            continue
        elif len(results) > 1:
            print('Internal Error. Contact administrator')
            print('\nTry again')
            continue

    action_status = None
    while 1:
        action_status_str = raw_input("Enter 'open' or 'close'")
        if action_status_str == 'open':
            action_status = 0
            break
        elif action_status_str == 'close':
            action_status = 1
            break
        else:
            print('"open" or "close" are the only two options \nTry again')
            continue
    values = (action_status, action_item_id)
    db.update_action_item(values=values)

def signup():
    f_name = raw_input("Enter first name: ")
    l_name = raw_input("Enter last name: ")
    values = (f_name, l_name)
    db = Core.DB.DB()
    return db.insert_new_customer(values=values)
    pass  # TODO

def show_average_rating_all_products(self):
    db = Core.DB.DB()
    results = db.fetch_average_ratings()
    print('Franchise            Average Product Rating          Average Service Rating\n')
    for result in results:
        print('' + str(result[0]) + '                    ' + str(result[1]) + '                          ' + str(
            result[2]) + '\n')

def show_product_wise_rating(self):
    db = Core.DB.DB()
    results = db.fetch_product_ratings()
    print('Product            Average Rating\n')
    for result in results:
        print('' + str(result[0]) + '                    ' + str(result[1]) + '\n')
