n = int(input("Enter number of processes: "))

p = []
at = []
bt = []
pr = []

for i in range(n):
    p.append(input("Process name: "))
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))
    pr.append(int(input("Priority: ")))

completed = [False] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
count = 0
gantt = []

while count < n:
    idx = -1
    highest_priority = 9999   # Smaller number = Higher priority

    # Find highest priority among arrived processes
    for i in range(n):
        if at[i] <= time and not completed[i]:
            if pr[i] < highest_priority:
                highest_priority = pr[i]
                idx = i

    # If no process has arrived
    if idx == -1:
        time += 1
        continue

    # Execute process
    gantt.append(p[idx])

    time += bt[idx]
    ct[idx] = time

    tat[idx] = ct[idx] - at[idx]
    wt[idx] = tat[idx] - bt[idx]

    completed[idx] = True
    count += 1

# Gantt Chart
print("\nGantt Chart")
for process in gantt:
    print("|", process, end=" ")
print("|")

# Process table
print("\nProcess\tAT\tBT\tPriority\tCT\tTAT\tWT")
for i in range(n):
    print(p[i], "\t", at[i], "\t", bt[i], "\t", pr[i], "\t\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAverage Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)