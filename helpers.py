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

def generateVisitationID(qs, prefix='V'):
    today = date.today()
    year = str(today.year)[-2:] #last 2 digits of current year
    month = str(today.month).zfill(2) # if month is single character, prefix with 0
    day = str(today.day).zfill(2) # if day is single character, prefix with 0
    prefix = prefix + year + month + day
    if qs.count() == 0:
        id_post_fix = '001'
        visitationID = prefix + id_post_fix
    else:
        last_visit_id = qs.last().VisitationID
        if last_visit_id[0:6] != prefix:
            id_post_fix = '001'
            visitationID = prefix + id_post_fix
        else:
            postfix = last_visit_id[-3:]
            increase_id = int(postfix) + 1
            id_post_fix = str(increase_id)
            visitationID = prefix + id_post_fix
    return visitationID