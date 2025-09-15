while True:
    num1 = float(input('Enter first number'))
    num2 = float(input('Enter second number'))

    operation = input('Enter operation + , -, *, /, %,**').strip()

    if operation == '+':
        print(f'{num1} + {num2} = {num1+num2}')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1-num2}')
    elif operation == '*':
        print(f'{num1} * {num2} = {num1*num2}')
    elif operation == '/':
        if num2!=0:
            print(f'{num1} / {num2} = {num1/num2}')
        else:
            print('Division by zero not allowed')
    elif operation == '%':
        if num2 != 0:
            print(f'{num1} % {num2} = {num1%num2}')
        else:
            print('Modulus by zero is not allowed')
    elif operation == '**':
        print(f'{num1} ^ {num2} = {num1**num2}')
    else:
        print('Invalid operation')

    cont = input('Do you want to continue? y/n').strip().lower()
    if cont == 'n':
        break

