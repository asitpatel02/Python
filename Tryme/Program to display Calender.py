# program t display calendar of the given month and year

# importing calender module
import calendar

yy = int(input('Enter a Year: '))
mm = int(input('Enter a Month: '))

print(calendar.month(yy, mm))
