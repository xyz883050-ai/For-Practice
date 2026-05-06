# File Allocation Strategies

print("1. Sequential Allocation")
print("2. Linked Allocation")
print("3. Indexed Allocation")

choice = int(input("Enter your choice: "))

file_name = input("Enter file name: ")
start = int(input("Enter starting block: "))
length = int(input("Enter file length: "))


# Sequential Allocation
if choice == 1:

    print("\nFile Name:", file_name)
    print("Sequential Allocation Blocks:")

    for i in range(length):
        print(start + i, end=" ")

    print()


# Linked Allocation
elif choice == 2:

    print("\nFile Name:", file_name)
    print("Linked Allocation:")

    for i in range(length):

        block = start + i

        if i == length - 1:
            print(block, "-> NULL")

        else:
            print(block, "->", start + i + 1)


# Indexed Allocation
elif choice == 3:

    print("\nFile Name:", file_name)
    print("Index Block =", start)

    print("Allocated Blocks:")

    for i in range(1, length + 1):
        print(start + i, end=" ")

    print()


else:
    print("Invalid Choice")