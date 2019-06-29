#calculate miles per gallon driven

def mpg():

    #get user input
    milesDriven= float(input("Enter miles driven:\t"))
    gallonsUsed = float(input("Enter gallons of gas used:\t"))

    # calculate mpg
    mpg = milesDriven / gallonsUsed
    mpg = round(mpg, 2)
                
    # format and display 
    print("Miles Per Gallon:\t" + str(mpg))

def main():
    mpg()

main()



