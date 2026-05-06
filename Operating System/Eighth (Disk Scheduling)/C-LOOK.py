n = int(input("Enter number of requests: "))
req = list(map(int, input("Enter request queue: ").split()))

head = int(input("Enter initial head position: "))

left = sorted([x for x in req if x < head])
right = sorted([x for x in req if x >= head])

sequence = [head] + right + left

seek = 0

for i in range(len(sequence)-1):
    seek += abs(sequence[i] - sequence[i+1])

print("\nSeek Sequence =", sequence)
print("Total Seek Time =", seek)