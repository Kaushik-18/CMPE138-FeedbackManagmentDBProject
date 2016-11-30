import Core.DB
import Core.app
import ui.utils


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


def list_all_feedbacks(self):
    db = Core.DB.DB()
    feedback_types = ("product_feedback", "service_feedback")
    results = []
    for feedback_type in feedback_types:
        results_part = db.query(self, feedback_type)
        db.close()
        if (results_part is None) or (len(results_part) == 0):
            continue
        else:
            for result in results_part:
                results.append(result)
    return results


def list_unassigned_feedbacks(self, franchise_id):
    # TODO: test: test object set difference separately
    # TODO: optimize: fire direct sql query
    db = Core.DB.DB()
    all_prod_feedback_id_objs = db.query(table='product_feedback',
                                         paramsJson={"franchise_id": franchise_id, },
                                         attributes='product_feedback_id')
    all_prod_feedback_ids = ui.utils.prodfbs_to_set(all_prod_feedback_id_objs)

    assigned_prod_feedback_id_objs = db.query(table='action_items',
                                              paramsJson={"service_feedback_id": ""},
                                              attributes='product_feedback_id')
    assigned_prod_feedback_ids = ui.utils.prodfbs_to_set(assigned_prod_feedback_id_objs)

    unassigned_prod_feedback_ids = all_prod_feedback_ids.difference(assigned_prod_feedback_ids)

    unassigned_prod_feedbacks = []
    for uid in unassigned_prod_feedback_ids:
        unassigned_prod_feedbacks.extend(db.query(table='product_feedback',
                                                  paramsJson={"product_feedback_id": uid}))

    # for service feedbacks
    all_serv_feedback_id_objs = db.query(table='service_feedback',
                                         paramsJson={"franchise_id": franchise_id, },
                                         attributes='service_feedback_id')
    all_serv_feedback_ids = ui.utils.servfbs_to_set(all_serv_feedback_id_objs)

    assigned_serv_feedback_id_objs = db.query(table='action_items',
                                              paramsJson={"product_feedback_id": ""},
                                              attributes='service_feedback_id')
    assigned_serv_feedback_ids = ui.utils.servfbs_to_set(assigned_serv_feedback_id_objs)

    unassigned_serv_feedback_ids = all_serv_feedback_ids.difference(assigned_serv_feedback_ids)

    unassigned_serv_feedbacks = []
    for uid in unassigned_serv_feedback_ids:
        unassigned_serv_feedbacks.extend(db.query(table='product_feedback',
                                                  paramsJson={"product_feedback_id": uid}))
    unassigned_prod_feedbacks.extend(unassigned_serv_feedbacks)
    return unassigned_prod_feedbacks


def update_action_item():
    pass  # use DB.py


# TODO by mgr, franchise


def insert_action_item(self):
    start_date = input("Enter start date: ")
    end_date = input("Enter end date: ")
    created_by = input("Enter created by: ")
    assigned_to = input("Enter the ID of assigned employee: ")
    comm = raw_input("Enter comments: ")
    fb_type = raw_input("Enter feedback type (product or service): ")
    fb_id = input("Enter feedback id: ")
    db = Core.DB.DB()
    values = (start_date, end_date, created_by, assigned_to,
              comm, fb_id)
    db.insert_action_item(values=values,
                          feedback_type=fb_type)

# TODO use DB.py


def close_action_item(self):
    db = Core.DB.DB()
    action_items = db.query(table="action_items")
    for action in action_items:
        action.printItem()
    print("---------------------")
    action_item_id = raw_input("Select an action item from the above list: ")
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
