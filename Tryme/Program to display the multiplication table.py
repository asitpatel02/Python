# Multiplication table (from 1 to 10) in python

num = int(input('Display multiplication table of? '))

# Iterate 10 items from i = 1 to 10
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
