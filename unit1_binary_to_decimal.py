# binary to decimal

binary = input("Enter a binary number: ").strip()

if not binary or any(digit not in "01" for digit in binary):
    print("Invalid input: enter binary digits 0 and 1 only.")
else:
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    print("Decimal:", decimal)
