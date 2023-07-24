import clips
import pandas as pd

# Load the CLIPS environment
env = clips.Environment()

# Load the rules.clp file
env.load("rules.clp")

# Read the CSV file into a DataFrame
df = pd.read_csv('restaurantDATA.csv')

# Extract the relevant columns from the DataFrame
locations = df['LOCATION']
categories = df['CATEGORY']
cuisines = df['CUISINE']
prices = df['PRICE']
ratings = df['RATING']
restaurantnames = df['RESTAURANT NAME']

# Iterate over the DataFrame rows
# for i in range(len(df)):
#     # Create a Restaurant fact in CLIPS for each row in the DataFrame
#     env.assert_string(f'(Restaurant (city "{cities[i]}") (category "{categories[i]}") (cuisine "{cuisines[i]}") (price "{prices[i]}") (rating "{ratings[i]}"))')

# Define the user's preferences
location = input("Enter the location: ")
category = input("Enter the category (Veg/Non-Veg): ")
cuisine = input("Enter the cuisine (Indian/Chinese/Italian): ")
price = input("Enter the price range (Under150/150-300/Above300): ")
rating = input("Enter the minimum rating (1-3): ")
# location = "Hyderabad"
# category = "Veg"
# cuisine = "Italian"
# price = "Under150"
# rating = "2"

# Create a UserRecommendation fact in CLIPS based on user inputs
env.assert_string(f'(Restaurant (location {location}) (category {category}) (cuisine {cuisine}) (price {price}) (rating {rating}))')

# Run the CLIPS engine
# DOES NOT DO ANYTHING...
num = env.run()
for fact in env.facts():
    if(fact):
        print(fact)

# Reset the CLIPS environment
env.reset()
