r = int(input('Enter your grade: '))
if r < 0 or r > 100:
    print('Incorrect value')
elif r <= 59:
    print('Unsatisfactory')
elif r <= 64:
    print('Marginal')
elif r <= 74:
    print('Satisfactory')
elif r <= 84:
    print('Good')
elif r <= 94:
    print('Very good')
else:
    print('Excellent')
