# LFU Page Replacement

ref = list(map(int, input("Reference string: ").split()))
frames = int(input("Frames: "))

memory = [-1] * frames
history = []

freq = {}      # Frequency count
age = {}       # For tie breaking (older page removed)

page_faults = 0
time = 0

for page in ref:

    time += 1

    # Update frequency
    if page not in freq:
        freq[page] = 1
        age[page] = time
    else:
        freq[page] += 1

    # If page already exists
    if page in memory:
        history.append(memory.copy())
        continue

    # Page fault
    page_faults += 1

    # Empty frame available
    if -1 in memory:
        idx = memory.index(-1)
        memory[idx] = page

    else:
        # Find LFU page
        victim = memory[0]

        for p in memory:
            if freq[p] < freq[victim]:
                victim = p
            elif freq[p] == freq[victim]:
                if age[p] < age[victim]:
                    victim = p

        idx = memory.index(victim)
        memory[idx] = page

    history.append(memory.copy())

# Print reference string
print("\n ", end=" ")
for x in ref:
    print(x, end=" ")
print("\n")

# Print table like your image
for i in range(frames - 1, -1, -1):

    print("F" + str(i), "|", end=" ")

    for j in range(len(ref)):

        if history[j][i] == -1:
            print("-", end=" ")
        else:
            print(history[j][i], end=" ")

    print()

# Output
ratio = page_faults / len(ref)

print("\nPage Fault Ratio =", round(ratio, 2))
print("Total Page Faults =", page_faults)