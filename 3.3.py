years = float(input('Enter calendar years: '))
if years < 0:
    print('Incorrect value')
elif years <= 2:
    print('Dog years: ', years*10.5)
else:
    print('Dog years: ', (years-2)*4+21)
