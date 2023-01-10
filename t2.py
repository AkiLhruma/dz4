# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('text.txt', 'r') as f:
    mnogochel1 = (f.readline())
    k = (f.readline(2))

with open('text2.txt', 'r') as f:
    mnogochel2 = (f.read())

mnogochel1 = mnogochel1.split()
mnogochel2 = mnogochel2.split()

d = {a: mnogochel1[a] for a in range(len(mnogochel1))}
print(d.values())
d2 = {a: mnogochel2[a] for a in range(len(mnogochel2))}
print(d2.values())

x2sum = 0
xsum = 0
sum = 0

for i in range(len(mnogochel1)):
    if d.get(i).isdigit():
        if d.get(i+2) == f'x**{k}':
            x2sum += int(d.get(i))
        elif d.get(i+2) == 'x':
            xsum += int(d.get(i))
        else:
            sum += int(d.get(i))
    else:
        if d.get(i) == f'x**{k}':
            if d.get(i-2).isdigit():
                continue
            else:
                x2sum += 1
        elif d.get(i) == 'x':
            if d.get(i-2).isdigit():
                continue
            else:
                xsum += 1
        else:
            if d.get(i).isdigit():
                sum += int(d.get(i))

for i in range(len(mnogochel2)):
    if d2.get(i).isdigit():
        if d2.get(i+2) == f'x**+{k}':
            x2sum += int(d2.get(i))
        elif d2.get(i+2) == 'x':
            xsum += int(d2.get(i))
        else:
            sum += int(d2.get(i))
    else:
        if d2.get(i) == f'x**{k}':
            if d2.get(i-2, 'net digetov').isdigit():
                continue
            else:
                x2sum += 1
        elif d2.get(i) == 'x':
            if d2.get(i-2, 'net digetov').isdigit():
                continue
            else:
                xsum += 1
        else:
            if d2.get(i).isdigit():
                sum += int(d2.get(i))

print(f'{x2sum}x**{k} + {xsum}x + {sum} = 0')

with open('text3.txt', 'w') as text:
    text.write(f'{x2sum}x**{k} + {xsum}x + {sum} = 0')



# или вот это надо было сделать?

# mnogochel3 = mnogochel1 + mnogochel2
# mnogochel3.remove('=')
# ind = mnogochel3.index('0')
# mnogochel3.remove('0')
# mnogochel3.insert(ind, '+')
# print(mnogochel3)

# with open('text3.txt', 'w') as text:
#     text.writelines(mnogochel3)