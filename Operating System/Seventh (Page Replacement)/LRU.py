# LRU Page Replacement

ref = list(map(int, input("Reference string: ").split()))
frames = int(input("Frames: "))

memory = [-1] * frames
history = []

page_faults = 0

for i in range(len(ref)):
    page = ref[i]

    # Page fault
    if page not in memory:
        page_faults += 1

        # Empty frame available
        if -1 in memory:
            index = memory.index(-1)
            memory[index] = page

        else:
            # Find least recently used page
            lru_index = -1
            least = i

            for j in range(frames):
                last_used = -1

                for k in range(i-1, -1, -1):
                    if ref[k] == memory[j]:
                        last_used = k
                        break

                if last_used < least:
                    least = last_used
                    lru_index = j

            memory[lru_index] = page

    # Save current state
    history.append(memory.copy())

# Print reference string
print("\n ", end=" ")
for x in ref:
    print(x, end=" ")
print("\n")

# Print frame table
for i in range(frames-1, -1, -1):
    print("F" + str(i), "|", end=" ")

    for j in range(len(ref)):
        if history[j][i] == -1:
            print("-", end=" ")
        else:
            print(history[j][i], end=" ")

    print()

# Page fault ratio
ratio = page_faults / len(ref)

print("\nPage Fault Ratio =", round(ratio, 2))
print("Total Page Faults =", page_faults)