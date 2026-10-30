from datetime import datetime,timedelta

def get_upcoming_birthdays(users):
    """функція обробляє дати та дні народження працівників та повертає список працівників у яких дні народження протягом тижня та переносить дні народження на понеділок якщо вони випадають на вихідні"""
       
    today = datetime.today().date()
    result = []
       
    today = datetime.today().date()
    result = []
    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_until_birthday = (birthday_this_year - today).days
        if days_until_birthday < 7:
            congrat_date = birthday_this_year

            if congrat_date.weekday() == 5:  
                congrat_date = congrat_date + timedelta(days=2) 
            elif congrat_date.weekday() == 6:  
                congrat_date = congrat_date + timedelta(days=1)

            result.append({'name': user['name'], 'birthday': congrat_date.strftime('%Y.%m.%d')})

    return result 

users = [
    {"name": "Иван", "birthday": "1990.10.30"},
    {"name": "Ольга", "birthday": "2001.10.31"},
    {"name": "Дмитрий", "birthday": "1995.11.01"},
    {"name": "Анна", "birthday": "2002.11.02"},
    {"name": "Михаил", "birthday": "1988.11.04"},
    {"name": "Елена", "birthday": "1998.11.05"},
    {"name": "Сергей", "birthday": "1992.11.06"},
    {"name": "Мария", "birthday": "1997.10.29"},
    {"name": "Алексей", "birthday": "1993.05.15"},
]    

upcoming_birthdays = get_upcoming_birthdays(users)
print("Ближайшие дни рождения в течение недели:", upcoming_birthdays)
