n = int(input("Enter number of processes: "))
process = []

print("Enter process sizes:")
for i in range(n):
    process.append(int(input()))

m = int(input("Enter number of blocks: "))
blocks = []

print("Enter block sizes:")
for i in range(m):
    blocks.append(int(input()))

allocation = [-1] * n

for i in range(n):
    best = -1

    for j in range(m):
        if blocks[j] >= process[i]:
            if best == -1 or blocks[j] < blocks[best]:
                best = j

    if best != -1:
        allocation[i] = best
        blocks[best] -= process[i]

print("\nProcess\tSize\tBlock")

for i in range(n):
    if allocation[i] != -1:
        print("P"+str(i+1), "\t", process[i], "\tB"+str(allocation[i]+1))
    else:
        print("P"+str(i+1), "\t", process[i], "\tNot Allocated")