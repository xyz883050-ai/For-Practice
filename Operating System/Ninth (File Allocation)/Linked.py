file_name = input("Enter file name: ")
start = int(input("Enter starting block: "))
length = int(input("Enter file length: "))

print("\nFile Name:", file_name)
print("Linked Allocation:")

for i in range(length):
    block = start + i

    if i == length - 1:
        print(block, "-> NULL")
    else:
        print(block, "->", start + i + 1)