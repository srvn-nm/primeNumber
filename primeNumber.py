import math
num = int(input('Please enter the number you want to be checked: '))
i = 2
while num % i != 0:
    if i >= int(math.sqrt(num)) :
        print('the number is prime ^-^')
        break
    i += 1
else :
    print('the number is not prime >-<')