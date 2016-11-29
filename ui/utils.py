import Core.DB


def checkPass(self, entity_type, inp_id, pswd):
    db = Core.DB.DB()
    results = db.query("logins", {"entity_type": entity_type,
                                  "id": inp_id,
                                  "password": pswd})
    if len(results) == 0:
        return False
    elif len(results) > 1:
        print("Internal Server Error. Try contacting administrator")
        return False
    elif len(results == 1):
        return True
