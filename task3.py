import re

def normalize_phone(phone_number):
    """фукнція обробляє номери телефонів прибераючи всі зайві символи та пробіли та приводе до вірного формату починаючи з +38 та повертає нормалізований номер телефону"""
    clean = re.sub(r'[^\d+]', '', phone_number)
    if clean.startswith('+'):
        return clean   
    elif clean.startswith('380'):
        return '+' + clean
    else:
        return '+38' + clean
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized_numbers = [normalize_phone(number) for number in raw_numbers] 
print("Нормалізовані номери телефонів:", normalized_numbers)