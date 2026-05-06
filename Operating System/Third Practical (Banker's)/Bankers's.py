# Banker's Algorithm

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

processes = []
allocation = []
max_matrix = []

# Input Allocation Matrix
print("\nEnter process names and Allocation Matrix:")
for i in range(n):
    pname = input("Process name: ")
    processes.append(pname)

    print("Enter allocation for", pname)
    row = list(map(int, input().split()))
    allocation.append(row)

# Input Max Matrix
print("\nEnter Max Matrix:")
for i in range(n):
    print("Enter max for", processes[i])
    row = list(map(int, input().split()))
    max_matrix.append(row)

# Choice
print("\nChoose Input Method:")
print("1. Enter Available Resources")
print("2. Enter Total Resource Instances")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Enter Available Resources:")
    available = list(map(int, input().split()))

elif choice == 2:
    print("Enter Total Resource Instances:")
    total = list(map(int, input().split()))

    allocated_sum = [0] * m

    for i in range(n):
        for j in range(m):
            allocated_sum[j] += allocation[i][j]

    available = []

    for j in range(m):
        available.append(total[j] - allocated_sum[j])

else:
    print("Invalid Choice")
    exit()

# Calculate Need Matrix
need = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(max_matrix[i][j] - allocation[i][j])
    need.append(row)

# Output Need Matrix
print("\nNeed Matrix")
for i in range(n):
    print(processes[i], ":", need[i])

# Safety Algorithm
finish = [False] * n
work = available.copy()
safe_sequence = []

count = 0

while count < n:
    found = False

    for i in range(n):
        if not finish[i]:

            possible = True

            for j in range(m):
                if need[i][j] > work[j]:
                    possible = False
                    break

            if possible:
                for j in range(m):
                    work[j] += allocation[i][j]

                safe_sequence.append(processes[i])
                finish[i] = True
                count += 1
                found = True

    if not found:
        break

print("\nAvailable Resources =", available)

if count == n:
    print("System is in Safe State")
    print("Safe Sequence =", " -> ".join(safe_sequence))
else:
    print("System is NOT in Safe State")