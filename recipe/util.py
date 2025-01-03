import pandas as pd
from .models import Recipe

def import_recipes_from_csv(file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv("recipe/data/food_data.csv")

    # Iterate over rows and create Recipe objects
    for index, row in df.iterrows():
        recipe = Recipe.objects.create(
            image_link=row['Image Link'],
            ingredients=row['Ingredients'],
            dish=row['Dish'],
            recipe=row['Recipe']
        )