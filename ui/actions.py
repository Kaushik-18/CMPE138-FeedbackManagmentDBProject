import sys

import Core.DB
import Core.app


def insert_product_feedback(self, cust_id):
    fb = Core.app.ProductFeedback()
    db = Core.DB.DB()
    fb.customer_id = cust_id
    fb.franchise_id = int(raw_input("Enter franchise id: "))
    if db.check_franchise_exists(fb.franchise_id):
        fb.item_id = int(raw_input("Enter product ID: "))
        if db.check_product_record(fb.item_id, fb.franchise_id):
            fb.rating = int(raw_input("Enter rating (1 to 5): "))
            fb.comments = raw_input("Enter feedback: ")
            conf = raw_input("Submit the above feedback? (yes or no): ")
            if conf == "yes":
                fb.persist()
            else:
                print('Feedback submission cancelled. Exiting now...')
                sys.exit(0)
        else:
            print ("Product not available for this franchise.Please check product id or franchise id !")
    else:
        print ("Invalid franchise id.")

    db.close()


def insert_service_feedback(self, cust_id):
    fb = Core.app.ServiceFeedback()
    db = Core.DB.DB()
    fb.customer_id = cust_id
    fb.franchise_id = int(raw_input("Enter franchise id: "))
    if db.check_franchise_exists(fb.franchise_id):
        fb.item_id = int(raw_input("Enter service ID: "))
        if db.check_service_exists(fb.item_id):
            fb.rating = int(raw_input("Enter rating (1 to 5): "))
            fb.comments = raw_input("Enter feedback: ")
            conf = raw_input("Submit the above feedback? (yes or no): ")
            if conf == "yes":
                fb.persist()
            else:
                print('Feedback submission cancelled. Exiting now...')
                sys.exit(0)
        else:
            print ("Invalid service ID for this franchise")
    else:
        print ("Invalid Feedback ID ")
    db.close()


def list_action_items(self, action_status=None):
    pass  # TODO


def listAllFeedbacks(self):
    db = Core.DB.DB()
    results = db.query(self, "Feedback")
    db.close()
    if (results == None) and (len(results) == 0):
        print("No Results")
    else:
        for result in results:
            print(result)


def update_action_item():
    pass
