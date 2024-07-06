from collections import deque

def is_palindrome(s):
    # Привести рядок до нижнього регістру і видалити пробіли
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Створити двосторонню чергу
    dq = deque(s)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

# Приклад використання
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f"Рядок '{test_string}' є паліндромом")
else:
    print(f"Рядок '{test_string}' не є паліндромом")
