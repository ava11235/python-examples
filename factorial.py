#calculate factorial using a loop

def main():
    num = int(input("Enter a number to calculate its factorial: "))
 
    fac = 1
 
    for i in range(1, num + 1):
        fac = fac * i
 
    print("Factorial of ", num, " is ", fac)


main()
