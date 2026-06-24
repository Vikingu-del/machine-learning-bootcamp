kata = (19, 42, 21)


def main():
    if not isinstance(kata, tuple):
        print("Error: kata must be a tuple.")
        return
    if any(not isinstance(i, int) for i in kata):
        print("Error: all elements of kata must be integers.")
        return
    numbers_str = ", ".join(str(i) for i in kata)
    print(f"The {len(kata)} numbers are: {numbers_str}")


if __name__ == "__main__":
    main()
