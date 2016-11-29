import Core.DB


def checkPass(entity_type, inp_id, pswd):
    db = Core.DB.DB()
    results = db.query("logins", {"entity_type": entity_type,
                                  "id": inp_id,
                                  "pass": pswd})
    if len(results) == 0:
        return False
    elif len(results) > 1:
        print("Internal Server Error. Try contacting administrator")
        return False
    elif len(results) == 1:
        return True


def prodfbs_to_set(obj):
    to_ret = set()
    for x in obj:
        to_ret.add(x.product_feedback_id)
    return to_ret


def servfbs_to_set(obj):
    to_ret = set()
    for x in obj:
        to_ret.add(x.service_feedback_id)
    return to_ret
