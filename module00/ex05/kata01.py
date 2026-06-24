kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


def main():
    if not isinstance(kata, dict):
        print("Error: kata must be a dictionary.")
        return
    if any(not isinstance(key, str) or not isinstance(value, str)
            for key, value in kata.items()):
        print("Error: all keys in kata must be strings "
              "and all values must be strings.")
        return
    for key, value in kata.items():
        print(f"{key} was created by {value}")


if __name__ == "__main__":
    main()
