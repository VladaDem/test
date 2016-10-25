x = float(input('First number: '))
y = float(input('Second number: '))
operation = input('Operation: ')
result = None

if operation == '+' :
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y  
else:
    print('Not found')
if result is not None:
    print(result)