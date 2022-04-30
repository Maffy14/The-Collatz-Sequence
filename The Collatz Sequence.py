
print('Enter number:')
number = int(input())

def collatz(number):
    if number % 2 == 0:
       return number // 2
    elif number % 2 == 1:
       return 3 * number + 1

while number != 1:
    number = collatz(number)
    print(number)

