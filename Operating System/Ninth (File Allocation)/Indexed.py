file_name = input("Enter file name: ")
start = int(input("Enter starting block: "))
length = int(input("Enter file length: "))

print("\nFile Name:", file_name)
print("Index Block:", start)

print("Allocated Blocks:")

for i in range(1, length + 1):
    print(start + i, end=" ")

print()