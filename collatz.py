def collatz(number):
    if (number%2):
        print("The number is odd : 3*number+1 = " + str(3*number+1))
        return 3*number+1
    else:
        print("The number is even: number//2 = " + str(number//2))
        return number//2

print("Enter a number: ", end='')
stdin = input()
try:
    num   = int(stdin)
except ValueError:
    print("INPUT=" + stdin)
    print("The input must be an integer only! Exiting...")

while (num > 1):
    num = collatz(num)
    print("collatz(num) = " + str(num))
