# take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]

y = int(input('Enter a number of divisible: '))

result = list(filter(lambda x: (x % y == 0), my_list))

# display the result
print('Numbers divisible by ', y, 'are', result)
