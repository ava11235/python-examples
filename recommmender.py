'''Simple recommender system:
    Recommends top 10 movies based on rankings
    if the movie has more votes than 75% of the 45,000 movies
    in the Full MovieLens dataset (movies_metadata.csv)'''


# Import Pandas
import pandas as pd

# Load dataframe
data = pd.read_csv('movies_metadata.csv', low_memory=False)

# Print the first 5 rows
print(data.head(5))


# Calculate mean of vote average column
C = data['vote_average'].mean()
print("Average rating on scale of 10: ", C)

# Calculate value of minimum number of votes required to be in the chart, m
m = data['vote_count'].quantile(0.75)
print("Minimum number of votes required to be in the chart:", m)

# Copy filtered movies into a new DataFrame
movies = data.copy().loc[data['vote_count'] >= m]
movies.shape

# Define function to compute weighted rating of each movie
def weightedRating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # use the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

# Define a new column 'score' and calculate its value 
movies['score'] = movies.apply(weightedRating, axis=1)

#Sort movies based on score calculated above
movies = movies.sort_values('score', ascending=False)

#Print the top 10 movies
print(movies[['title', 'vote_count', 'vote_average', 'score']].head(10))


