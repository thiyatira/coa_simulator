# find data hazards

# operation, output register, input registers
instructions = [
    ("ADD", "R1", "R2", "R3"),
    ("SUB", "R4", "R1", "R5"),
    ("AND", "R6", "R4", "R1"),
]

print("Instructions:")
for index, (operation, destination, left, right) in enumerate(instructions, 1):
    print(f"{index}: {operation} {destination},{left},{right}")

print("\nRAW timing hazards (producer -> consumer):")
for consumer in range(len(instructions)):
    sources = instructions[consumer][2:]
    for producer in range(max(0, consumer - 2), consumer):
        register = instructions[producer][1]
        # check if the register was written again
        overwritten = any(instructions[i][1] == register
                          for i in range(producer + 1, consumer))
        if register in sources and not overwritten:
            print(f"{producer + 1} -> {consumer + 1}: {register}")

print("\nAssumes consecutive issue, no forwarding, and WB before ID.")
