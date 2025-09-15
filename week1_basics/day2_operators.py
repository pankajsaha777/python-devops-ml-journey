num1 = float(input('Enter first number'))
num2 = float(input('Enter second number'))

add = num1 + num2
print(f'Sum of the numbers {num1} and {num2} is {add:.2f}')
sub = num1 - num2
print(f'Difference of the numbers {num1} and {num2} is {sub:.2f}')
mul = num1 * num2
print(f'Multiplication of the numbers {num1} and {num2} is {mul:.2f}')
if num2!=0:
    div = num1 / num2
    print(f'Division of the numbers {num1} and {num2} is {div:.2f}')
    mod = num1 % num2
    print(f'Modulus of the numbers {num1} and {num2} is {mod:.2f}')
else:
    print('Division and modulus not possible as the denominator can not be zero')
exp = num1 ** num2
print(f'Exponentiation of the numbers {num1} and {num2} is {exp:.2f}')