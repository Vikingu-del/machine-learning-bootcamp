import sys


def main():
    if len(sys.argv) == 1:
        print("Usage: python whois.py <one integer>")
        sys.exit(1)
    assert len(sys.argv) == 2, "more than one argument is provided"
    try:
        x = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if x == 0:
        print("I'm Zero.")
    elif x % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
