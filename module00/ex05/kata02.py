import sys


kata = (2019, 9, 25, 3, 30)


def main():
    if len(kata) != 5:
        print("Error: kata must contain exactly 5 elements.")
        return
    if not all(isinstance(i, int) for i in kata):
        print("Error: all elements of kata must be integers.")
        return
    if not isinstance(kata, tuple):
        print("Error: kata must be a tuple.")
        return
    if any(i < 0 for i in kata):
        print("Error: all elements of kata must be non-negative.")
        return
    print(f"{kata[1]:02d}/{kata[2]:02d}/{kata[0]:04d} "
          f"{kata[3]:02d}:{kata[4]:02d}")


if __name__ == "__main__":
    main()
