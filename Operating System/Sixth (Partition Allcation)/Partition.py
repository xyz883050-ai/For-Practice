# Partition Allocation

n = int(input("Enter number of processes: "))
process = []

print("Enter process sizes:")
for i in range(n):
    process.append(int(input(f"P{i+1}: ")))

m = int(input("Enter number of memory blocks: "))
blocks = []

print("Enter block sizes:")
for i in range(m):
    blocks.append(int(input(f"B{i+1}: ")))

print("\nChoose Allocation Method")
print("1. First Fit")
print("2. Best Fit")
print("3. Worst Fit")

choice = int(input("Enter choice: "))

allocation = [-1] * n
temp_blocks = blocks.copy()

# First Fit
if choice == 1:
    for i in range(n):
        for j in range(m):
            if temp_blocks[j] >= process[i]:
                allocation[i] = j
                temp_blocks[j] -= process[i]
                break

# Best Fit
elif choice == 2:
    for i in range(n):
        best = -1

        for j in range(m):
            if temp_blocks[j] >= process[i]:
                if best == -1 or temp_blocks[j] < temp_blocks[best]:
                    best = j

        if best != -1:
            allocation[i] = best
            temp_blocks[best] -= process[i]

# Worst Fit
elif choice == 3:
    for i in range(n):
        worst = -1

        for j in range(m):
            if temp_blocks[j] >= process[i]:
                if worst == -1 or temp_blocks[j] > temp_blocks[worst]:
                    worst = j

        if worst != -1:
            allocation[i] = worst
            temp_blocks[worst] -= process[i]

else:
    print("Invalid choice")
    exit()

# Output
print("\nProcess\tSize\tBlock")

for i in range(n):
    if allocation[i] != -1:
        print("P", i+1, "\t", process[i], "\tB", allocation[i]+1)
    else:
        print("P", i+1, "\t", process[i], "\tNot Allocated")