n = int(input("Enter number of processes: "))

p = []
at = []
bt = []

for i in range(n):
    p.append(input("Process name: "))
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))

rt = bt.copy()   # Remaining time
ct = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
completed = 0
gantt = []

while completed < n:
    idx = -1
    min_bt = 9999

    # Find process with shortest remaining time
    for i in range(n):
        if at[i] <= time and rt[i] > 0:
            if rt[i] < min_bt:
                min_bt = rt[i]
                idx = i

    # If no process has arrived
    if idx == -1:
        time += 1
        continue

    # Execute for 1 unit time
    gantt.append(p[idx])
    rt[idx] -= 1
    time += 1

    # Process completed
    if rt[idx] == 0:
        completed += 1
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]

# Gantt Chart
print("\nGantt Chart")
for process in gantt:
    print("|", process, end=" ")
print("|")

# Table
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(p[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAverage Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)