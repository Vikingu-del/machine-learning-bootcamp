import sys
from datetime import datetime
from recipe import Recipe


class Book:

    def validate_book(self):
        """Validates all attributes.

        Prints specific errors and exits if invalid.
        """
        if not isinstance(self.name, str) or not self.name:
            print("ERROR: 'name' must be a non-empty string.")
            sys.exit()

        if not isinstance(self.recipes_list, dict):
            print("ERROR: 'recipes_list' must be a dictionary.")
            sys.exit()

        if set(self.recipes_list.keys()) != self.required_keys:
            print(f"ERROR: 'recipes_list' must contain exactly the keys: {', '.join(self.required_keys)}.")
            sys.exit()

        for key, values in self.recipes_list.items():
            if not isinstance(values, list):
                print(f"ERROR: The value for '{key}' must be a list.")
                sys.exit()
            if not all(isinstance(v, Recipe) for v in values):
                print(f"ERROR: All items in the list for '{key}' must be instances of the Recipe class.")
                sys.exit()
        
        

    def __init__(self, name: str, recipes_list: dict=None):
        """Initializes the Recipe object and triggers validation."""
        self.name: str = name
        self.creation_date: float = datetime.now()
        self.last_update: float = self.creation_date
        self.recipes_list: dict = (
            recipes_list if recipes_list is not None else {
                "starter": [],
                "lunch": [],
                "dessert": []
            }
        )
        self.required_keys = {'starter', 'lunch', 'dessert'}
        self.validate_book()

    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        recipe = next(
            (
                r
                for recipes in self.recipes_list.values()
                for r in recipes
                if r.name == name
            ),
            None,
        )

        if recipe:
            print(recipe)
        return recipe
        

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        if recipe_type not in self.required_keys:
            print(f"ERROR: '{recipe_type}' is not a valid recipe type. Valid types are: {', '.join(self.required_keys)}.")

        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
            print("ERROR: The provided object is not an instance of the Recipe class.")
            sys.exit()
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

