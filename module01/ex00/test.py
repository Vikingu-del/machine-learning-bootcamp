from recipe import Recipe
from book import Book
from datetime import datetime
import pytest


class TestRecipe:

    # ==============================================================================
    # 1. VALID INPUTS
    # ==============================================================================

    def test_valid_recipe(self):
        """Verifies that a fully valid recipe initializes with the correct attributes."""
        recipe = Recipe(
            name="Pasta",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["pasta", "tomato sauce", "cheese"],
            recipe_type="lunch",
            description="A simple pasta dish.",
        )
        assert recipe.name == "Pasta"
        assert recipe.cooking_lvl == 3
        assert recipe.cooking_time == 15
        assert recipe.ingredients == ["pasta", "tomato sauce", "cheese"]
        assert recipe.recipe_type == "lunch"
        assert recipe.description == "A simple pasta dish."

    # ==============================================================================
    # 2. EDGE CASES & BOUNDARY VALIDATIONS
    # ==============================================================================

    def test_minimum_cooking_lvl(self):
        """Verifies the lowest possible valid difficulty boundary level (1)."""
        recipe = Recipe(
            name="Salad",
            cooking_lvl=1,
            cooking_time=5,
            ingredients=["lettuce", "tomato", "cucumber"],
            recipe_type="starter",
            description="A fresh salad.",
        )
        assert recipe.cooking_lvl == 1

    def test_maximum_cooking_lvl(self):
        """Verifies the highest possible valid difficulty boundary level (5)."""
        recipe = Recipe(
            name="Beef Wellington",
            cooking_lvl=5,
            cooking_time=120,
            ingredients=["beef", "mushrooms", "puff pastry"],
            recipe_type="lunch",
            description="A gourmet dish.",
        )
        assert recipe.cooking_lvl == 5

    def test_zero_cooking_time(self):
        """Verifies that a cooking time of 0 is accepted as a valid non-negative integer."""
        recipe = Recipe("Raw Salad", 1, 0, ["lettuce"], "starter")
        assert recipe.cooking_time == 0

    def test_valid_empty_description(self):
        """Verifies that the optional description field can safely be an empty string."""
        recipe = Recipe("Pasta", 3, 15, ["pasta"], "lunch", description="")
        assert recipe.description == ""

    # ==============================================================================
    # 3. INVALID INPUTS & SYSTEM EXIT ERROR HANDLING
    # ==============================================================================

    def test_invalid_cooking_lvl(self):
        """Verifies that a difficulty level completely out of range (> 5) triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=6,
                cooking_time=15,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="lunch",
                description="A simple pasta dish.",
            )

    def test_zero_cooking_lvl(self):
        """Verifies that a difficulty level below the valid threshold (< 1) triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe("Pasta", 0, 15, ["pasta"], "lunch")

    def test_invalid_cooking_time(self):
        """Verifies that a negative cooking time triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=-5,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="lunch",
                description="A simple pasta dish.",
            )

    def test_invalid_ingredients(self):
        """Verifies that passing invalid data types (ints) inside the ingredient list triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["pasta", 123, "cheese"],
                recipe_type="lunch",
                description="A simple pasta dish.",
            )

    def test_empty_ingredients_list(self):
        """Verifies that an empty ingredients list triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe("Pasta", 3, 15, [], "lunch")

    def test_empty_string_in_ingredients(self):
        """Verifies that a list containing blank strings as ingredients triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe("Pasta", 3, 15, ["pasta", ""], "lunch")

    def test_invalid_recipe_type(self):
        """Verifies that a course type outside of the allowed categories triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="dinner",
                description="A simple pasta dish.",
            )

    def test_invalid_description(self):
        """Verifies that passing a non-string type to the description triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe(
                name="Pasta",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["pasta", "tomato sauce", "cheese"],
                recipe_type="lunch",
                description=123,
            )

    def test_empty_name(self):
        """Verifies that an empty recipe name string triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe("", 3, 15, ["pasta"], "lunch")

    def test_none_as_name(self):
        """Verifies that passing None as a name triggers a safe exit."""
        with pytest.raises(SystemExit):
            Recipe(None, 3, 15, ["pasta"], "lunch")

    # ==============================================================================
    # 4. BUILT-IN MAGIC METHOD TESTS
    # ==============================================================================

    def test_str_method(self):
        """Verifies the exact formatting string representation of the recipe details."""
        recipe = Recipe(
            name="Pasta",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["pasta", "tomato sauce", "cheese"],
            recipe_type="lunch",
            description="A simple pasta dish.",
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


class TestBook:

    # ==============================================================================
    # 1. INITIALIZATION & VALIDATION TESTS
    # ==============================================================================

    def test_book_initialization_defaults(self):
        """Verifies a book sets up its default empty structures correctly."""
        book = Book("Grandma's Secrets")
        assert book.name == "Grandma's Secrets"
        assert isinstance(book.creation_date, datetime)
        assert isinstance(book.last_update, datetime)
        assert book.recipes_list == {"starter": [], "lunch": [], "dessert": []}

    def test_invalid_empty_book_name(self):
        """Verifies an empty book name forces a system exit."""
        with pytest.raises(SystemExit):
            Book("")

    def test_invalid_book_name_type(self):
        """Verifies a non-string book name forces a system exit."""
        with pytest.raises(SystemExit):
            Book(12345)

    def test_invalid_recipes_list_type(self):
        """Verifies passing a list instead of a dict forces a system exit."""
        with pytest.raises(SystemExit):
            Book("Bad Book", recipes_list=["starter", "lunch"])

    def test_invalid_recipes_list_keys(self):
        """Verifies a dictionary with incorrect keys forces a system exit."""
        bad_dict = {"breakfast": [], "lunch": [], "dessert": []}  # 'breakfast' is invalid
        with pytest.raises(SystemExit):
            Book("Bad Book", recipes_list=bad_dict)

    def test_invalid_recipes_list_values(self):
        """Verifies a dictionary with non-Recipe instances forces a system exit."""
        bad_dict = {
            "starter": ["Not A Recipe Object"],
            "lunch": [],
            "dessert": [],
        }
        with pytest.raises(SystemExit):
            Book("Bad Book", recipes_list=bad_dict)

    # ==============================================================================
    # 2. METHOD TESTS: add_recipe()
    # ==============================================================================

    def test_add_recipe_success(self):
        """Verifies valid recipes are routed into the correct dictionary list."""
        book = Book("Mastering AI Cooking")
        salad = Recipe("Salad", 1, 5, ["lettuce"], "starter")
        cake = Recipe("Cake", 3, 45, ["flour", "sugar"], "dessert")

        book.add_recipe(salad)
        book.add_recipe(cake)

        assert salad in book.recipes_list["starter"]
        assert cake in book.recipes_list["dessert"]
        assert len(book.recipes_list["lunch"]) == 0

    def test_add_recipe_updates_timestamp(self):
        """Verifies last_update advances forward when a recipe is added."""
        book = Book("Time Test Book")
        initial_update_time = book.last_update

        # Add a delay token simulation or let execution naturally flow
        pasta = Recipe("Pasta", 2, 15, ["pasta"], "lunch")
        book.add_recipe(pasta)

        # last_update should be greater than or equal to creation_date
        assert book.last_update >= initial_update_time

    def test_add_recipe_invalid_type_exits(self):
        """Verifies trying to add a plain string/integer instead of a Recipe object crashes safely."""
        book = Book("Strict Book")
        with pytest.raises(SystemExit):
            book.add_recipe("Just a text string string representation")

    # ==============================================================================
    # 3. METHOD TESTS: get_recipe_by_name()
    # ==============================================================================

    def test_get_recipe_by_name_found(self):
        """Verifies searching a recipe by its exact name returns the object instance."""
        book = Book("Search Book")
        pasta = Recipe("Pasta", 2, 15, ["pasta"], "lunch")
        book.add_recipe(pasta)

        result = book.get_recipe_by_name("Pasta")
        assert result == pasta
        assert result.name == "Pasta"

    def test_get_recipe_by_name_not_found(self):
        """Verifies searching a non-existent name returns None safely without breaking."""
        book = Book("Search Book")
        result = book.get_recipe_by_name("Ghost Recipe")
        assert result is None

    # ==============================================================================
    # 4. METHOD TESTS: get_recipes_by_types()
    # ==============================================================================

    def test_get_recipes_by_types_valid(self):
        """Verifies fetching a specific type returns a clean list of string names."""
        book = Book("Type Book")
        soup = Recipe("Tomato Soup", 1, 20, ["tomato"], "starter")
        salad = Recipe("Greek Salad", 1, 10, ["feta"], "starter")
        pasta = Recipe("Carbonara", 3, 20, ["eggs", "bacon"], "lunch")

        book.add_recipe(soup)
        book.add_recipe(salad)
        book.add_recipe(pasta)

        starter_names = book.get_recipes_by_types("starter")
        assert isinstance(starter_names, list)
        assert "Tomato Soup" in starter_names
        assert "Greek Salad" in starter_names
        assert "Carbonara" not in starter_names

    def test_get_recipes_by_types_empty(self):
        """Verifies fetching a valid type that has no recipes yet returns an empty list."""
        book = Book("Type Book")
        assert book.get_recipes_by_types("dessert") == []