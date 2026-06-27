import sys

class GotCharacter:

    def __init__(self, first_name: str = None, is_alive: bool = True):
        if first_name is not None:
            if not isinstance(first_name, str):
                raise TypeError("first_name must be a string.")
            if not first_name.strip():
                raise ValueError("first_name cannot be an empty string.")

        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean.")

        self.first_name = first_name
        self.is_alive = is_alive
    
    def __str__(self):
        return self.first_name

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def __str__(self):
        return f"{self.first_name} {self.family_name}"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        if self.is_alive == True:
            self.is_alive = False
        else:
            print(f"{self} has already died")

class Lanister(GotCharacter):
    """A class representing the Lanister family"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lanister"
        self.house_words = "Pure Blood"

    def __str__(self):
        return f"{self.first_name} {self.family_name}"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        if self.is_alive == True:
            self.is_alive = False
        else:
            print(f"{self} has already died")
        