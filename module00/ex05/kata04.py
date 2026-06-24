kata = (0, 4, 132.42222, 10000, 12365.67)


def main():
    if len(kata) != 5:
        print("Error: kata must contain exactly 5 elements.")
        return
    if not isinstance(kata[0], int) or not isinstance(kata[1], int):
        print("Error: kata[0] and kata[1] must be integers.")
        return
    if kata[0] < 0 or kata[1] < 0:
        print("Error: kata[0] and kata[1] must be non-negative.")
        return
    if not isinstance(kata[2], (int, float)) \
        or not isinstance(kata[3], (int, float)) \
            or not isinstance(kata[4], (int, float)):
        print("Error: kata[2], kata[3], and kata[4] must be numbers.")
        return
    print(f"module_{kata[0]:02d}, ex_{kata[1]:02d} "
          f": {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")


if __name__ == "__main__":
    main()
