b=10

try:
    a=10/b
    print(a)
    print('Try completed')
except ZeroDivisionError:
    print('Number cant divide by 0')

print('Completed')