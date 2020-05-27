#linear regression least sqyare implementation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#customize figsize
plt.rcParams['figure.figsize'] = (20.0, 10.0)

# read data
data = pd.read_csv('headbrain.csv')

print(data.shape)
print(data.head())

# collect X and Y values
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

# calculate means Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

print("Head size mean:", mean_x)
print("Brain weight mean:", mean_y)

# number of values
n = len(X)

# calculate m and c
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
    m = numer / denom
    c = mean_y - (m * mean_x)
 
# print coefficients
print("coefficients:",  m, c)

# plot values and regression line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# calculate line values for x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x 
 
# plot Line
plt.plot(x, y, color='red', label='Regression Line')

# plot scatter points
plt.scatter(X, Y, c='purple', label='Scatter Plot')
 
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

#plt.savefig("regline.png")







 
