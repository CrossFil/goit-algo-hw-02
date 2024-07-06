import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Лічильник для унікальних ідентифікаторів заявок
request_id_counter = 1

def generate_request():
    global request_id_counter
    # Створити нову заявку з унікальним ідентифікатором
    request_id = request_id_counter
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги")
    request_id_counter += 1

def process_request():
    if not request_queue.empty():
        # Видалити заявку з черги
        request_id = request_queue.get()
        print(f"Заявка {request_id} обробляється")
        # Імітувати час обробки заявки
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Заявка {request_id} оброблена")
    else:
        print("Черга пуста")

def main():
    start_time = time.time()
    while True:
        # Перевірка на закінчення 5 секунд
        if time.time() - start_time > 5:
            print("Програма завершена через 5 секунд")
            break
        
        # Імітувати генерацію нових заявок
        if random.random() < 0.7:  # 70% ймовірність додавання нової заявки
            generate_request()
        
        # Обробляти заявки
        process_request()
        
        # Імітувати затримку між операціями
        time.sleep(1)

if __name__ == "__main__":
    main()
