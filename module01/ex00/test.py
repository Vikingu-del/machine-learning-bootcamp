from recipe import Recipe
import pytest


class TestRecipe:
    def test_valid_recipe(self):
        recipe = Recipe(
            name="Pasta",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["pasta", "tomato sauce", "cheese"],
            recipe_type="lunch",
            description="A simple pasta dish."
        )
        assert recipe.name == "Pasta"
        assert recipe.cooking_lvl == 3
        assert recipe.cooking_time == 15
        assert recipe.ingredients == ["pasta", "tomato sauce", "cheese"]
        assert recipe.recipe_type == "lunch"
        assert recipe.description == "A simple pasta dish."


    def test_invalid_cooking_lvl(self):
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=6,
                cooking_time=15,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="lunch",
                description="A simple pasta dish."
            )


    def test_invalid_cooking_time(self):
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=-5,  # Invalid cooking time
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="lunch",
                description="A simple pasta dish."
            )


    def test_invalid_ingredients(self):
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["pasta", 123, "cheese"],  # Invalid ingredient type
                recipe_type="lunch",
                description="A simple pasta dish."
            )


    def test_invalid_recipe_type(self):
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="dinner",
                description="A simple pasta dish."
            )


    def test_invalid_description(self):
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="lunch",
                description=123  # Invalid description type
            )


    def test_str_method(self):
        recipe = Recipe(
            name="Pasta",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["pasta", "tomato sauce", "cheese"],
            recipe_type="lunch",
            description="A simple pasta dish."
        )
        expected_str = (
            "Recipe: Pasta\n"
            "Cooking Level: 3\n"
            "Cooking Time: 15 minutes\n"
            "Ingredients: pasta, tomato sauce, cheese\n"
            "Type: lunch\n"
            "Description: A simple pasta dish."
        )
        assert str(recipe) == expected_str


    def test_minimum_cooking_lvl(self):
        recipe = Recipe(
            name="Salad",
            cooking_lvl=1,  # Edge case: minimum valid cooking level
            cooking_time=5,
            ingredients=["lettuce", "tomato", "cucumber"],
            recipe_type="starter",
            description="A fresh salad."
        )
        assert recipe.cooking_lvl == 1


    def test_maximum_cooking_lvl(self):
        recipe = Recipe(
            name="Beef Wellington",
            cooking_lvl=5,  # Edge case: maximum valid cooking level
            cooking_time=120,
            ingredients=["beef", "mushrooms", "puff pastry"],
            recipe_type="lunch",
            description="A gourmet dish."
        )
        assert recipe.cooking_lvl == 5


    def test_empty_name(self):
        with pytest.raises(SystemExit):
            Recipe("", 3, 15, ["pasta"], "lunch")


    def test_none_as_name(self):
        with pytest.raises(SystemExit):
            Recipe(None, 3, 15, ["pasta"], "lunch")


    def test_empty_ingredients_list(self):
        with pytest.raises(SystemExit):
            Recipe("Pasta", 3, 15, [], "lunch")


    def test_empty_string_in_ingredients(self):
        with pytest.raises(SystemExit):
            Recipe("Pasta", 3, 15, ["pasta", ""], "lunch")


    def test_zero_cooking_time(self):
        # 0 is non-negative, so it should be valid!
        recipe = Recipe("Raw Salad", 1, 0, ["lettuce"], "starter")
        assert recipe.cooking_time == 0

    def test_zero_cooking_lvl(self):
        with pytest.raises(SystemExit):
            Recipe("Pasta", 0, 15, ["pasta"], "lunch")
    

    def test_valid_empty_description(self):
        # This should NOT raise an error
        recipe = Recipe("Pasta", 3, 15, ["pasta"], "lunch", description="")
        assert recipe.description == ""


    def test_str_method_with_no_description(self):
        recipe = Recipe("Pasta", 3, 15, ["pasta"], "lunch", description="")
        # Verify that your string format handles the empty description gracefully
        assert "No description provided" in str(recipe)
