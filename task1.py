from datetime import datetime

def get_days_from_today(date_str): 
    """Створюємо функцію яка обробляє дату у вірний формат та повертає кількість днів між сьогоднішньою датою та введеною датою"""
    try:
        start_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.now()
        today = today.date()
        delta = today - start_date
        return delta.days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
print(get_days_from_today('2008-01-27')) 
    
        