# python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))
num3 = float(input('Enter 3rd number: '))

if(num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

    print('The largest number is', largest)
