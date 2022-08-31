#Square or Cube Calculator
print("*Please use lower case*")

print('Square or Cube?')

option = input('>')

print("enter a number")
x = int(input('>'))

if option == 'Square':
    answer = x*x
    
elif option == 'Cube':
    answer = x*x*x

else:
    print('INVALID OPERATION!')
    print('Run the program again and enter valid operation and number')

print(answer)