buffer = []
item_count = 1

while True:
    print("\n1. Producer")
    print("2. Consumer")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = "Item" + str(item_count)
        buffer.append(item)

        print("Producer produced:", item)
        item_count += 1

    elif choice == 2:
        if len(buffer) == 0:
            print("Buffer is empty")
        else:
            item = buffer.pop(0)
            print("Consumer consumed:", item)

    elif choice == 3:
        print("Program exited")
        break

    else:
        print("Invalid choice")