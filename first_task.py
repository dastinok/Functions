# Создайте несколько переменных заканчивающихся на s
# Напишите ф-цию меняющую s. Кроме одной. Значения не удаляются
# Помещаются в одноименные переменные

#firsts = 1
#seconds = 'star'
#thirds = 789
#forths = 4.5
#s = 0

#def get_replace(**kwargs):
#    globals
#    result = {}
#    for i, e in kwargs.items():
#        if len(i) != 1 and i.endswith('s'):
#            i = i[:len(i)-1]
#            e = None
#        result[i] = e
#    return result


#print(get_replace(firsts=1, seconds='star', thirds=789,forths=4.5, s=0))
maxim_ = 0
myhfhs = 'sdfsd'
hjygfs = 787
s = 778
print(f'{maxim_=}')
print(f'{myhfhs=}')
print(f'{hjygfs=}')
print(f'{s=}')

for i in globals().copy():
    if not i.startswith('__'):
        if i.endswith('s'):
            if len(i) > 1:
                new_name = i[:1]
                globals()[new_name] = None
            else:
                globals()[i] = globals().get(i)
print('После изменения')

print(f'{maxim_=}')
print(f'{myhfhs=}')
print(f'{hjygfs=}')
print(f'{s=}')
print(f'{myhfh=}')
print(f'{hjygf=}')