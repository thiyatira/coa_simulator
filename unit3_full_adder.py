# full adder truth table

print("A B Cin | Sum Cout")
for a in (0, 1):
    for b in (0, 1):
        for carry_in in (0, 1):
            total = a ^ b ^ carry_in
            carry_out = (a & b) | (carry_in & (a ^ b))
            print(f"{a} {b}  {carry_in}  |  {total}    {carry_out}")
