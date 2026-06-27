class Cookbook(dict):
    REQUIRED_KEYS = {"ingredients", "meal", "prep_time"}

    def _validate_recipe(self, recipe):
        if not isinstance(recipe, dict):
            raise TypeError("recipe must be a dictionary")
        
        if not set(recipe.keys()).issuperset(self.REQUIRED_KEYS):
            raise ValueError(f"recipe must contain at least the keys: {self.REQUIRED_KEYS}")
        
        if not isinstance(recipe["ingredients"], list) or not \
            all(isinstance(ingredient, str) for ingredient in recipe["ingredients"]):
            raise TypeError("ingredients must be a list of strings")
        
        if not isinstance(recipe["meal"], str):
            raise TypeError("meal must be a string")
        
        if not isinstance(recipe["prep_time"], int) or recipe["prep_time"] < 0:
            raise ValueError("prep_time must be a non-negative integer")

    def __setitem__(self, key, value):
        self._validate_recipe(value)
        if not isinstance(key, str) or not key:
            raise ValueError("Recipe name must be a non-empty string")
        super().__setitem__(key, value)

    def update(self, other=(), **kwargs):
        if isinstance(other, dict):
            for name, recipe in other.items():
                self._validate_recipe(recipe)
        elif hasattr(other, "__iter__"):
            for name, recipe in other:
                self._validate_recipe(recipe)
        for name, recipe in dict(other, **kwargs).items():
            self._validate_recipe(recipe)
            super().__setitem__(name, recipe)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.update(*args, **kwargs)

    def print_recipe_names(self):
        for name in self.keys():
            print(name)
    
    def print_recipe_details(self, name):
        if name not in self:
            print(f"Recipe '{name}' not found.")
            return
        recipe = self[name]
        for key, value in recipe.items():
            print(f"{key}: {value}")

    def delete_recipe(self, name):
        if name in self:
            del self[name]
        else:
            print(f"Recipe '{name}' not found.")

    def input_recipe(self):
        name = input("Enter a name:")
        print("Enter ingredients:")
        ingredients = []
        while True:
            item = input().strip()
            if item == "":
                break
            ingredients.append(item)
        meal = input("Enter a meal type:")
        prep_time = int(input("Enter a preparation time:"))
        recipe = {
            "ingredients": [ingredient.strip() for ingredient in ingredients],
            "meal": meal,
            "prep_time": prep_time
        }
        self[name] = recipe
