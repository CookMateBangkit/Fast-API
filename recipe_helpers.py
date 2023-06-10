import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset_recipes = None
dataset_ingredients = None

def load_dataset():
  dataset_recipes = pd.read_excel('./dataset_recipes.xlsx')
  dataset_ingredients = pd.read_excel('./dataset_ingredients.xlsx')
  return dataset_recipes, dataset_ingredients

def get_recommendation(keyword):
  
  global dataset_recipes
  global dataset_ingredients
  if dataset_recipes is None or dataset_ingredients is None: 
    dataset_recipes, dataset_ingredients = load_dataset()
    
  vectorizer = TfidfVectorizer()
  recipe_matrix = vectorizer.fit_transform(dataset_recipes['main_ingredient'])
  
  query_vector = vectorizer.transform([keyword])
  similarity_scores = cosine_similarity(query_vector, recipe_matrix)
  
  top_recipe_indices = similarity_scores.argsort()[0][::-1]
  top_10_recipes = dataset_recipes.iloc[top_recipe_indices][:10]
  recipes = top_10_recipes.reset_index().to_dict(orient='index')
  
  recipes_cleaned = list(recipes.values())
  
  for dictionary in recipes_cleaned:
    del dictionary['index']
    del dictionary['main_ingredient']
  
  return recipes_cleaned

def get_all_ingredients():
  
  global dataset_recipes
  global dataset_ingredients
  if dataset_recipes is None or dataset_ingredients is None: 
    dataset_recipes, dataset_ingredients = load_dataset()
  
  ingredients = dataset_ingredients.reset_index().to_dict(orient='index')
  ingredients = list(ingredients.values())
  
  for dictionary in ingredients:
    del dictionary['index']
  
  return ingredients

def get_all_recipes():
  
  global dataset_recipes
  global dataset_ingredients
  if dataset_recipes is None or dataset_ingredients is None: 
    dataset_recipes, dataset_ingredients = load_dataset()
    
  recipes = dataset_recipes.reset_index().to_dict(orient='index')
  recipes = list(recipes.values())
  
  for dictionary in recipes:
    del dictionary['index']
    del dictionary['main_ingredient']
    
  return recipes
    
def get_detail_recipe(id):

  global dataset_recipes
  global dataset_ingredients
  if dataset_recipes is None or dataset_ingredients is None: 
    dataset_recipes, dataset_ingredients = load_dataset()
  
  recipe = dataset_recipes.loc[dataset_recipes['id'] == id]
  recipe = recipe.to_dict('records')[0]
    
  return recipe
    