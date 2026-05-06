# FIFO Page Replacement

ref = list(map(int, input("Reference string: ").split()))
frames = int(input("Frames: "))

memory = [-1] * frames
pointer = 0
page_faults = 0

# To store table history
history = []

for page in ref:

    if page not in memory:
        page_faults += 1

        memory[pointer] = page
        pointer = (pointer + 1) % frames

    # Store current frame state
    history.append(memory.copy())

# Print reference string
print("\n ", end=" ")
for x in ref:
    print(x, end=" ")
print("\n")

# Print frame table (reverse like your image)
for i in range(frames - 1, -1, -1):

    print("F" + str(i), "|", end=" ")

    for j in range(len(ref)):

        if history[j][i] == -1:
            print("-", end=" ")
        else:
            print(history[j][i], end=" ")

    print()

# Page Fault Ratio
ratio = page_faults / len(ref)

print("\nPage Fault Ratio =", round(ratio, 2))
print("Total Page Faults =", page_faults)