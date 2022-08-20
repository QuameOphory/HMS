from datetime import date

def generateID(prefix, qs, length=10):
    '''
    This function helps to generate custom IDs for DB models
    '''
    if qs.count() == 0:
        id = prefix + str(1).zfill((length - len(prefix)))
    else:
        last_id = qs.last().id
        new_id = int(last_id) + 1
        id = prefix + str(new_id).zfill(length - len(prefix))
    return id

def calculateAge(birthdate):
    '''
    this function returns a date given a birthdate
    '''
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age