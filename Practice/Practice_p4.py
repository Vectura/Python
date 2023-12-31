# Заряжаем обойму нужными патронами. Импортируем (подключаем) в наш код необходимые библиотеки (libs), 
# методы и функции, которые встроены в язык Python
from random import randint
import time

# Объявляем переменные посредством ввода данных от пользователя
igr1 = input('Введите имя 1-го играющего ')
igr2 = input('Введите имя 2-го играющего ')
# Объявляем две переменные-счетчика. В них будем инкрементировать единицу после каждой победы игрока 1 и 2
k1 = k2 = 0

# Запускаем цикл посредством встроенной функции range(). 
# С ее помощью мы просто создаем объект, содержащий в себе перечисление натуральных чисел от 0 до 4. 
# Перебор этого объекта обеспечит нас 5-ю итерациями - столько раз игроки должны бросить кубик.
for i in range(5):
    print('Кубик бросает', igr1)
    time.sleep(1) #задержка на 1 секунду для интриги момента
    n1 = randint(1, 6) #встроенная функция, возвращающая рандомное число в заданном интервале
    print('Выпало:', n1)

    print('Кубик бросает', igr2)
    time.sleep(1)
    n2 = randint(1, 6)
    print('Выпало:', n2)

# Запускаем проверку: если выиграл игрок1, то прибавляем единицу к его счетчику к1, если игрок 2, то к счетчику к2. 
# Счетчик накапливает в себе число побед.
    if igr1 > igr2:
        k1 += 1
        print('Победил в раунде ' + igr1)
    elif igr1 < igr2: 
        k2 += 1
        print('Победил в раунде ' + igr2)
    else:
        print('Ничья') 

print('И побеждает!!!...')
time.sleep(3) #Барабанная дробь
if igr1 > igr2:
        print(f"По итогам 5-ти бросков победил игрок {igr1} со счетом {k1}:{k2}") 
elif igr1 < igr2:
        print(f"По итогам 5-ти бросков победил игрок {igr2} со счетом {k2}:{k1}")
else:
        print(f"По итогам 5-ти бросков победила дружба: {k2}:{k1}")



