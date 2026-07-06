import sys


def main():
    binary = input("Binary: ")

    if "," in binary:
        decimal = binary_to_decimal(binary.split(", "))
    else:
        decimal = binary_to_decimal([binary])

    for c, d in enumerate(decimal):
        if c >= len(decimal) - 1:
            print(d)
        else:
            print(d, end=", ")


def binary_to_decimal(binary):
    decimal = []

    for b in binary:
        if len(b) > 8:
            sys.exit("Max of 8 digits")

        try:
            decimal.append(int(b, 2))
        except ValueError:
            sys.exit("Please, type only 1 and 0 numbers")

    return decimal


if __name__ == "__main__":
    main()
