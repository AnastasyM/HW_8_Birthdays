from datetime import datetime, timedelta
from collections import defaultdict
from pprint import pprint



class InvalidBirthdayError(ValueError):
    pass
def check_birthday_year(birthday):
    if birthday.year < 1900:
        raise InvalidBirthdayError('Invalid Birthday year')
    
def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days = diff_days)

def prepare_birthday(text: str):

    try:
        bd = datetime.strptime(text, '%d, %m, %Y')

        try:
            check_birthday_year(bd)   
        except InvalidBirthdayError:
            print(f'You have daid person in the team {bd} ')  


        true_bd = bd.replace(year=datetime.now().year).date()
        
        return true_bd
                      
    except ValueError as e:
        return print(f'You have some mistake in the date {e}')
       


def get_birthdays_per_week(users):

    birthdays = {'Monday':[], 'Tuesday':[], 'Wednesday':[], 'Thursday':[], 'Friday':[], 'Saturday':[], 'Sunday':[]}
    current_day = datetime.now().date()

    next_week_start = get_next_week_start(current_day)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(5)

    happy_users = [user for user in users if start_period <= prepare_birthday(user['birthday']) <= end_period]

    for user in happy_users:
        current_bd = prepare_birthday(user['birthday'])
        if current_bd.weekday() in (5,6):
            birthdays['Monday'].append(user['name'])
        else:
            birthdays[current_bd.strftime('%A')].append(user['name'])

    return birthdays

   
if __name__ == "__main__":
 
    users = [{'name':'Lusia', 'birthday':'10, 04, 1890'},
             {'name':'Miya', 'birthday':'11, 04, 2000'},
             {'name':'Mark', 'birthday':'12, 04, 1999'},
             {'name':'Nick', 'birthday':'13, 04, 1970'},
             {'name':'Dina', 'birthday':'14, 04, 1988'},
             {'name':'Nick', 'birthday':'15, 04, 1991'},
             {'name':'Poman', 'birthday':'16, 04, 1995'},
             {'name':'Petia', 'birthday':'08, 04, 1998'},
             {'name':'Sveta', 'birthday':'09, 04, 1980'}]

    result = get_birthdays_per_week(users)
    
    pprint (result)
   