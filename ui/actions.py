import sys

import Core.DB
import Core.app


def productFeedback(self, cust_id):
    fb = Core.app.ProductFeedback()
    fb.customer_id = cust_id
    fb.item_id = int(raw_input("Enter product ID: "))
    fb.rating = int(raw_input("Enter rating (1 to 5): "))
    fb.comments = raw_input("Enter feedback: ")
    print(fb)
    conf = raw_input("Submit the above feedback? (yes or no): ")
    if conf == "yes":
        fb.persist()
    else:
        print('Feedback submission cancelled. Exiting now...')
        sys.exit(0)


def serviceFeedback(self, cust_id):
    fb = Core.app.ServiceFeedback()
    fb.customer_id = cust_id
    fb.item_id = int(raw_input("Enter product ID: "))
    fb.rating = int(raw_input("Enter rating (1 to 5): "))
    fb.comments = raw_input("Enter feedback: ")
    print(fb)
    conf = raw_input("Submit the above feedback? (yes or no): ")
    if conf == "yes":
        fb.persist()
    else:
        print('Feedback submission cancelled. Exiting now...')
        sys.exit(0)


def listActionItems(self, action_status=None):
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
