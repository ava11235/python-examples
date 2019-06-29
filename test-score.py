# calculate 3 test scores average


print("Enter 3 test scores")

# get scores from the user
totalScore = 0       # initialize variable
#use the accumulator pattern (+=)
totalScore += int(input("Enter test score: "))
totalScore += int(input("Enter test score: "))
totalScore += int(input("Enter test score: "))

# calculate average score
averageScore = round(totalScore / 3)
             
# display the result
print("Total Score:  ", totalScore,
      "\nAverage Score:", averageScore)



