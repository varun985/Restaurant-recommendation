import clips
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the CLIPS environment
env = clips.Environment()

# Load the rules.clp file
env.load("rules.clp")

# Read the CSV file into a DataFrame
df = pd.read_csv('restaurantDATA.csv')

# Extract the relevant columns from the DataFrame
cities = df['CITY']
categories = df['CATEGORY']
cuisines = df['CUISINE']
prices = df['PRICE']
ratings = df['RATING']
restaurantnames = df['RESTAURANT NAME']

# Function to handle the recommendation logic
def recommend_restaurant():
    # Get the user's preferences from the input fields
    city = city_entry.get()
    category = category_entry.get()
    cuisine = cuisine_entry.get()
    price = price_entry.get()
    rating = rating_entry.get()

    # Create a UserRecommendation fact in CLIPS based on user inputs
    env.assert_string(f'(Restaurant (city {city}) (category {category}) (cuisine {cuisine}) (price {price}) (rating {rating}))')

    # Run the CLIPS engine
    num = env.run()

    # Retrieve the recommendation from CLIPS
    recommendation = None
    for fact in env.facts():
        if 'recommended' in str(fact):
            recommendation = str(fact)
            break

    # Reset the CLIPS environment
    env.reset()

    # Show the recommendation in a message box
    if recommendation:
        messagebox.showinfo("Recommendation", recommendation)
    else:
        messagebox.showinfo("Recommendation", "No restaurant found matching your criteria.")

# Create the main window
window = tk.Tk()
window.title("Restaurant Recommendation System")

# Create labels and input fields
city_label = tk.Label(window, text="City:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()

category_label = tk.Label(window, text="Category (Veg/Non-Veg):")
category_label.pack()
category_entry = tk.Entry(window)
category_entry.pack()

cuisine_label = tk.Label(window, text="Cuisine (Indian/Chinese/Italian):")
cuisine_label.pack()
cuisine_entry = tk.Entry(window)
cuisine_entry.pack()

price_label = tk.Label(window, text="Price Range (Under150/150-300/Above300):")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

rating_label = tk.Label(window, text="Minimum Rating (1-3):")
rating_label.pack()
rating_entry = tk.Entry(window)
rating_entry.pack()

# Create a button to trigger the recommendation
button = tk.Button(window, text="Recommend Restaurant", command=recommend_restaurant)
button.pack()

# Run the main event loop
window.mainloop()
