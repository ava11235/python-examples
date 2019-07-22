#sumDiff

def sumDiff(n1, n2):
    sum = n1 +n2
    diff = n1 - n2
    return sum, diff # can return multiple values

def main():
    n1, n2 = input("Enter two numbers: " ).split(",")
   # s,d = sumDiff(float(n1), float(n2))
    #print("Sum: ", s, "Diff: ", d)
    print("Sum, Diff: ", sumDiff(float(n1), float(n2)))

main()
    
