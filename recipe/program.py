import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import random

# Load Dataset
recipes = pd.read_csv("recipe/data/food_data.csv")

# Preprocess data for dish of the day
recipes.drop(columns=['Image Link', 'Recipe Link'], axis=1, inplace=True)
recipes_dish_of_the_day = recipes.dropna()

def Dish_recipe(user_Dish):
    tfidf = TfidfVectorizer(stop_words='english')
    Dish_tfidf = tfidf.fit_transform(recipes['Dish'])
   
    # Fit Nearest Neighbors model
    nn_model = NearestNeighbors(metric='cosine')
    nn_model.fit(Dish_tfidf)
    
    # Converting user's Dish input into a TF-IDF vector
    user_Dish_tfidf = tfidf.transform([user_Dish])
    
    # Find nearest recipes based on user's Dish input
    _, top_indices = nn_model.kneighbors(user_Dish_tfidf, n_neighbors=1)  # Recommend top 1 recipe
    selected_indices = random.sample(list(top_indices[0]), 1)
    
    # Return recommended recipes if found
    if len(selected_indices) > 0:
        recommended_recipes = []
        for idx in selected_indices:
            recipe_details = {
                "dish": recipes.iloc[idx]['Dish'],
                "ingredients": recipes.iloc[idx]['Recipe Ingredients'],
                "recipe": recipes.iloc[idx]['Recipe']
            }
            recommended_recipes.append(recipe_details)
        return recommended_recipes
    else:
        print("No recipes available for the dish:", user_Dish)
        return []

def Mood_recipe(user_Mood):
    tfidf = TfidfVectorizer(stop_words='english')
    Mood_tfidf = tfidf.fit_transform(recipes['Mood'])

    nn_model = NearestNeighbors(metric='cosine')
    nn_model.fit(Mood_tfidf)

    # Convert user's mood input into a TF-IDF vector
    user_Mood_tfidf = tfidf.transform([user_Mood])

    # Find nearest recipes based on user's mood input
    _, top_indices = nn_model.kneighbors(user_Mood_tfidf, n_neighbors=10)

    # Randomly select 2 recipes from the nearest neighbors
    selected_indices = random.sample(list(top_indices[0]), 2)

    # Return recommended recipes if found
    
    if len(selected_indices) > 0:
        recommended_recipes = []
        for idx in selected_indices:
            recipe_details = {
                "dish": recipes.iloc[idx]['Dish'],
                "ingredients": recipes.iloc[idx]['Recipe Ingredients'],
                "recipe": recipes.iloc[idx]['Recipe']
            }
            recommended_recipes.append(recipe_details)
        return recommended_recipes
    else:
        print("No recipes available for the mood:", user_Mood)
        return []

def Ingredient_recipe(user_ing):
    tfidf = TfidfVectorizer(stop_words='english')
    ingredients_tfidf = tfidf.fit_transform(recipes['Recipe Ingredients'])
    

    nn_model = NearestNeighbors(metric='cosine')
    nn_model.fit(ingredients_tfidf)
    
    # Convert user's ingredient input into a TF-IDF vector
    user_ing_tfidf = tfidf.transform([user_ing])

    # Find nearest recipes based on user's ingredient input
    _, top_indices = nn_model.kneighbors(user_ing_tfidf, n_neighbors=15)  # Recommend top 2 recipes

    # Randomly select 2 recipes from the nearest neighbors
    selected_indices = random.sample(list(top_indices[0]), 2)

    # Return recommended recipes if found
    if len(selected_indices) > 0:
        recommended_recipes = []
        for idx in selected_indices:
            recipe_details = {
                "dish": recipes.iloc[idx]['Dish'],
                "ingredients": recipes.iloc[idx]['Recipe Ingredients'],
                "recipe": recipes.iloc[idx]['Recipe']
            }
            recommended_recipes.append(recipe_details)
        return recommended_recipes
    else:
        print("No recipes available for the ingredient:", user_ing)
        return []
