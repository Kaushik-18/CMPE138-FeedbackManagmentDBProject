import argparse

import app
import DB

class cli:
    def mainLoop(self):
        pass#TODO

    def productFeedback(self, cust_id, productId, rating, feedback):
        fb = app.ProductFeedback(rating, feedback, cust_id, productId)
        print(fb.prettyPrint())
        #TODO confirm from user and persist
        fb.persist()

    def listAllFeedbacks(self):
        db = DB()
        results = db.query(self, "Feedback")
        db.close()
        if(results == None || len(results) == 0):
            print( "No Results")
        else:
            for result in results:
                print(result)

