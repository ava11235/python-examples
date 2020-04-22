#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#make a data frame from the csv file 
df = pd.read_csv('covid19countries.csv')

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.set_xticks([0, 1,2,3,4,5,6,7,8,9,10, 11,12 ,13])
ax.set_xticks([0, 3, 6, 9, 11, 13])

ax.set_xticklabels(['Apr 8','Apr 11', 'Apr 13','Apr 16','Apr 19','Apr 21'])

#plot, plot styling and labeling
plt.style.use('seaborn-pastel')

plt.title('Covid-19 Cases April 8-21  ', fontsize=18)
plt.xlabel('Date');
plt.ylabel('Number of Cases')

plt.plot(df["US"],  linewidth = 6, label ='US')
plt.plot(df["China" ], linewidth=6, label = 'China')
plt.plot(df["United_Kingdom"], linewidth=6, label="UK")
plt.plot(df["Spain"], linewidth=6, label="Spain")
plt.plot(df["Germany"], linewidth=6, label="Germany")
plt.legend()


# save the image
plt.savefig("covid19-apr8-21.png")