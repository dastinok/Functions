

a = 5
b = 7
c = 'sdfsdf'

print(globals())

for var, value in globals().copy().items():
    if not var.startswith('__'):
        print(var, value)

        globals()[var] = 900
print(globals())


