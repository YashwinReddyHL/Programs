import pandas as pd
import matplotlib.pyplot as plt
wine_reviews = pd.read_csv('winemag.csv')
print(wine_reviews.head())
# create figure and axis 
fig, ax = plt.subplots()
# plot histogram 
ax.hist(wine_reviews['points'])
# set title and labels 
ax.set_title('WineReview Scores') 
ax.set_xlabel('Points')
ax.set_ylabel('Frequency') 
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Let pandas read the headers directly from the CSV
wine_reviews = pd.read_csv('winemag.csv')

# Create figure and axis 
fig, ax = plt.subplots()

# Plot histogram for 'points'
ax.hist(wine_reviews['points'])

# Set title and labels 
ax.set_title('Wine Review Scores') 
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')

plt.show()