n = int(input("Enter number of requests: "))
req = list(map(int, input("Enter request queue: ").split()))

head = int(input("Enter initial head position: "))

sequence = [head]
seek = 0

for r in req:
    seek += abs(head - r)
    head = r
    sequence.append(head)

print("\nSeek Sequence =", sequence)
print("Total Seek Time =", seek)