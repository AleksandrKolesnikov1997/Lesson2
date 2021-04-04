a = int(input('А = '))
b = float(input('B = '))
c = a * b
print('C = a * b')
print('C =', c)
d = input('Введите слово :')
e = bool(input('False or True'))
edd_list = [a, b, c, d, e]
for i in range(len(edd_list)):
    print(edd_list[i], type(edd_list[i]))
