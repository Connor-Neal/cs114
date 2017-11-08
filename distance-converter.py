print('')
print('Hello')
print('')
print('Give me a number')
print('')
num = int(input())
print('')
print('Give me the first unit')
print('')
unit1 = input()
print('')
print('Give me the second unit')
print('')
unit2 = input()
print('')

if unit1 == 'miles' or unit1 == 'mi' and unit2 == 'kilometers' or unit2 == 'km':
    dist=(num * 1.60934)

elif unit1 == 'miles' or unit1 == 'mi' and unit2 == 'meters' or unit2 == 'm':
    dist=(num * 1609.34)

elif unit1 == 'miles' or unit1 == 'mi' and unit2 == 'feet' or unit2 == 'ft':
    dist=(num * 5280)


elif unit1 == 'feet' or unit1 == 'ft' and unit2 =='kilometers' or unit2 == 'km':
    dist=(num * 0.0003048)

elif unit1 == 'feet' or unit1 == 'ft' and unit2 == 'miles' or unit2 == 'mi':
    dist=(num * 0.000189394)

elif unit1 == 'feet' or unit1 == 'ft' and unit2 == 'meters' or unit2 == 'km':
    dist=(num * 0.3048)


elif unit1 == 'kilometers' or unit1 == 'km' and unit2 == 'miles' or unit2 == 'mi':
    dist=(num * 0.621371)

elif unit1 == 'kilometers' or unit1 == 'km' and unit2 == 'feet' or unit2 == 'ft':
    dist=(num * 3280.84)

elif unit1 == 'kilometers' or unit1 == 'km' and unit2 == 'meters' or unit2 == 'm':
    dist=(num * 1000)


elif unit1 == 'meters' or unit1 == 'm' and unit2 == 'kilometers' or unit2 == 'km':
    dist=(num * 0.001)

elif unit1 == 'meters' or unit1 == 'm' and unit2 == 'feet' or unit2 == 'ft':
    dist=(num * 3.28084)

elif unit1 == 'meters' or unit1 == 'm' and unit2 == 'miles' or unit2 == 'km':
    dist=(num * 0.621371)

print('')
print(dist)
print('')
print('GOOOOOOOOD BYYYYYYYYE')
print('')
