n = int(input("Enter number of processes: "))

processes = []

# Input
for i in range(n):
    p = input("Process name: ")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    processes.append([p, at, bt])

# Sort by Arrival Time
processes.sort(key=lambda x: x[1])

ct, tat, wt = [], [], []
time = 0

# Calculate times
for i in range(n):
    p, at, bt = processes[i]

    if time < at:
        time = at

    time += bt
    ct.append(time)

    tat.append(time - at)
    wt.append(tat[i] - bt)

# Output
print("\nGantt Chart")
for process in processes:
    print("|", process[0], end=" ")
print("|")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(processes[i][0], "\t",
          processes[i][1], "\t",
          processes[i][2], "\t",
          ct[i], "\t",
          tat[i], "\t",
          wt[i])

print("\nAverage Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)