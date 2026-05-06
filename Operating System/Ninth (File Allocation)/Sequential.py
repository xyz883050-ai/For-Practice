file_name = input("Enter file name: ")
start = int(input("Enter starting block: "))
length = int(input("Enter file length: "))

print("\nFile Name:", file_name)
print("Allocated Blocks:")

for i in range(length):
    print(start + i, end=" ")

print()