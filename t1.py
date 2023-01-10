# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

koef_list = list(range(101))
random.shuffle(koef_list)

k = input('Input number: ')
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)

with open('text.txt', 'w') as mnogochlen:
    mnogochlen.write(f'{a} * x**{k} + {b} * x + {c} = 0 \n{k}')

b = random.randint(0, 100)
with open('text2.txt', 'w') as mnogochlen2:
    mnogochlen2.write(f'x**{k} + {b} = 0')