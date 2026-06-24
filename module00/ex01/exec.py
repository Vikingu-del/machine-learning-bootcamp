import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python exec.py <one or more strings>")
        sys.exit(1)

    lst = []
    for s in sys.argv[1:]:
        lst.append(s)
    concatenated_str = " ".join(lst)
    print(concatenated_str.swapcase()[::-1])


if __name__ == "__main__":
    main()
