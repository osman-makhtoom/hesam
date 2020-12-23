from libs import mathmatic

print(25/5)

first_num = input('Please enter first number: ')
last_num = input('Please enter last number: ')
print('\n')

mathh = mathmatic.Mathmatic(int(first_num), int(last_num))
print(mathh.plus())