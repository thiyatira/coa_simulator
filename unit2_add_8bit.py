# add two 8-bit numbers

try:
    first = int(input("Enter first unsigned 8-bit number: "))
    second = int(input("Enter second unsigned 8-bit number: "))
    if not (0 <= first <= 255 and 0 <= second <= 255):
        raise ValueError
except ValueError:
    print("Invalid input: enter whole numbers from 0 to 255.")
else:
    total = first + second
    print("Full sum:", total)
    print("8-bit result:", total % 256)
    print("Carry:", total // 256)
