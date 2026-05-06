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
    worst = -1

    for j in range(m):
        if blocks[j] >= process[i]:
            if worst == -1 or blocks[j] > blocks[worst]:
                worst = j

    if worst != -1:
        allocation[i] = worst
        blocks[worst] -= process[i]

print("\nProcess\tSize\tBlock")

for i in range(n):
    if allocation[i] != -1:
        print("P"+str(i+1), "\t", process[i], "\tB"+str(allocation[i]+1))
    else:
        print("P"+str(i+1), "\t", process[i], "\tNot Allocated")