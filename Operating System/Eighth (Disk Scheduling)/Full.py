def show_output(sequence, total_seek):
    print("\nSeek Sequence:", sequence)
    print("Total Seek Time:", total_seek)


# FCFS
def fcfs(requests, head):
    sequence = [head]
    seek = 0

    for req in requests:
        seek += abs(head - req)
        head = req
        sequence.append(head)

    show_output(sequence, seek)


# SSTF
def sstf(requests, head):
    requests = requests.copy()

    sequence = [head]
    seek = 0

    while requests:
        nearest = min(requests, key=lambda x: abs(x - head))

        seek += abs(head - nearest)
        head = nearest

        sequence.append(head)
        requests.remove(nearest)

    show_output(sequence, seek)


# SCAN
def scan(requests, head, disk_size):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = [head]

    sequence += right
    sequence.append(disk_size - 1)
    sequence += left[::-1]

    seek = 0

    for i in range(len(sequence) - 1):
        seek += abs(sequence[i] - sequence[i+1])

    show_output(sequence, seek)


# C-SCAN
def cscan(requests, head, disk_size):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = [head]

    sequence += right
    sequence.append(disk_size - 1)
    sequence.append(0)
    sequence += left

    seek = 0

    for i in range(len(sequence) - 1):
        seek += abs(sequence[i] - sequence[i+1])

    show_output(sequence, seek)


# LOOK
def look(requests, head):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = [head]

    sequence += right
    sequence += left[::-1]

    seek = 0

    for i in range(len(sequence) - 1):
        seek += abs(sequence[i] - sequence[i+1])

    show_output(sequence, seek)


# C-LOOK
def clook(requests, head):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = [head]

    sequence += right
    sequence += left

    seek = 0

    for i in range(len(sequence) - 1):
        seek += abs(sequence[i] - sequence[i+1])

    show_output(sequence, seek)


# Main Program
n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter request queue: ").split()))

head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

print("\n1. FCFS")
print("2. SSTF")
print("3. SCAN")
print("4. C-SCAN")
print("5. LOOK")
print("6. C-LOOK")

choice = int(input("Enter choice: "))

if choice == 1:
    fcfs(requests, head)

elif choice == 2:
    sstf(requests, head)

elif choice == 3:
    scan(requests, head, disk_size)

elif choice == 4:
    cscan(requests, head, disk_size)

elif choice == 5:
    look(requests, head)

elif choice == 6:
    clook(requests, head)

else:
    print("Invalid Choice")