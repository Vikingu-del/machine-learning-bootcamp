from cook_book import Cookbook


# print(my_cookbook)


recipe1 = dict(
    ingredients=["ham", "bread", "cheese", "tomatoes"],
    meal="lunch",
    prep_time=10
)

recipe2 = dict(
    ingredients=["flour", "sugar", "eggs"],
    meal="dessert",
    prep_time=60
)

recipe3 = dict(
    ingredients=["avocado", "arugula", "tomatoes", "spinach"],
    meal="lunch",
    prep_time=15
)

# bad_recipe = dict(
#     ingredients=["avocado", "arugula", "tomatoes", "spinach"],
#     meal="lunch",
#     prep_time=-15
# )

# cookbook = dict(Sandwich=recipe1, Cake=recipe2, Salad=recipe3, BadRecipe=bad_recipe)
my_cookbook = Cookbook(Sandwich=recipe1, Cake=recipe2, Salad=recipe3)

def main():
    maps = {
        1: my_cookbook.print_recipe_names,
        2: lambda: my_cookbook.print_recipe_details(input("Please enter a recipe name to get its details:\n")),
        3: lambda: my_cookbook.delete_recipe(input("Please enter a recipe name to delete:\n")),
        4: my_cookbook.input_recipe
    }
    print("Welcome to the Python Cookbook!")
    print("List of the available options:")
    print("\t1. Print recipe names")
    print("\t2. Print recipe details")
    print("\t3. Delete recipe")
    print("\t4. Input new recipe")
    print("\t5. Exit")
    while True:
        try:
            inp = input("Please select an option: ")
            if not inp.isdigit():
                print("Please enter a number.")
                continue

            choice = int(inp)
            if choice == 5:
                break

            action = maps.get(choice)
            if action:
                action()
            else:
                print("Invalid option")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
