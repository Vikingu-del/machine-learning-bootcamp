kata = "The right format"


def main():
    if len(kata) > 42:
        print("Error: kata must not exceed 42 characters.")
        return
    if not isinstance(kata, str):
        print("Error: kata must be a string.")
        return
    print(f"{kata:->42}", end="\n")


if __name__ == "__main__":
    main()
