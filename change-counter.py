#change counter

def main():
    
    print("Enter the count of each coin type to calculate the total change value")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    totalValue = .25*quarters + .10*dimes + .05*nickels + .01*pennies
    print()
    print("You have a total of $" + (str)( round(totalValue,2)))

main()
