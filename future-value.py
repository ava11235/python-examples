# compute the value of an investment


def main():
    print("Calculate the future value of an investment")

    years = 10

    principal, apr = eval(input("Enter the initial principal, APR, separated by comma: "))
    

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in",years,"years is:", round(principal, 2))

main()
