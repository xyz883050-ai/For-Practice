n = int(input("Enter number of requests: "))
req = list(map(int, input("Enter request queue: ").split()))

head = int(input("Enter initial head position: "))

sequence = [head]
seek = 0

requests = req.copy()

while requests:
    nearest = min(requests, key=lambda x: abs(x - head))

    seek += abs(head - nearest)
    head = nearest

    sequence.append(head)
    requests.remove(nearest)

print("\nSeek Sequence =", sequence)
print("Total Seek Time =", seek)