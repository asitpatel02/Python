# python program to find the factorial of a number provided by the user

# change the value for a different result
num = int(input('Enter a number: '))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print('sorry, factorial dose not exist for negative numbers')
elif num == 0:
    print('the factorial of 0 is 1')
else:
    for i in range(1 , num + 1):
        factorial = factorial*i
    print('the factorial of ', num, ' is ', factorial)
