import sys


class Recipe:
    def validate_recipe(self):
        """Validates all attributes.
        Prints specific errors and exits if invalid.
        """
        if not isinstance(self.name, str) or not self.name:
            print("ERROR: 'name' must be a non-empty string.")
            sys.exit()

        if not isinstance(self.cooking_lvl, int) or not (
            1 <= self.cooking_lvl <= 5
        ):
            print("ERROR: 'cooking_lvl' must be an integer between 1 and 5.")
            sys.exit()

        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            print("ERROR: 'cooking_time' must be a non-negative integer.")
            sys.exit()

        if not isinstance(self.ingredients, list) or not self.ingredients:
            print("ERROR: 'ingredients' must be a non-empty list.")
            sys.exit()

        if not all(isinstance(i, str) and i for i in self.ingredients):
            print("ERROR: All items in 'ingredients' must be non-empty strings.")
            sys.exit()

        valid_types = {"starter", "lunch", "dessert"}
        if self.recipe_type not in valid_types:
            print(
                f"ERROR: 'recipe_type' must be one of the following: {', '.join(valid_types)}."
            )
            sys.exit()

        if not isinstance(self.description, str):
            print("ERROR: 'description' must be a string.")
            sys.exit()


    def __init__(
        self, name, cooking_lvl,
        cooking_time, ingredients, recipe_type,
        description=""
    ):
        """Initializes the Recipe object and triggers validation."""
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

        self.validate_recipe()


    def __str__(self):
        """Returns a string representation of the Recipe object."""
        return (
            f"Recipe: {self.name}\n"
            f"Cooking Level: {self.cooking_lvl}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Type: {self.recipe_type}\n"
            f"Description: {self.description}"
        )
    
def main():
    recipe = Recipe(
        name="Pasta",
        cooking_lvl=2,
        cooking_time=15,
        ingredients=["pasta", "tomato sauce", "cheese"],
        recipe_type="lunch",
        description="A simple pasta dish."
    )
    print(recipe)


if __name__ == "__main__":
    main()
