n = int(input("Enter number of processes: "))

p = []
at = []
bt = []

for i in range(n):
    p.append(input("Process name: "))
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))

completed = [False] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
count = 0
gantt = []

while count < n:
    idx = -1
    min_bt = 9999

    # Find shortest job among arrived processes
    for i in range(n):
        if at[i] <= time and completed[i] == False:
            if bt[i] < min_bt:
                min_bt = bt[i]
                idx = i

    # If no process arrived yet
    if idx == -1:
        time += 1
        continue

    # Execute selected process
    gantt.append(p[idx])

    time += bt[idx]
    ct[idx] = time

    tat[idx] = ct[idx] - at[idx]
    wt[idx] = tat[idx] - bt[idx]

    completed[idx] = True
    count += 1

# Correct Gantt Chart
print("\nGantt Chart")
for process in gantt:
    print("|", process, end=" ")
print("|")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(p[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAverage Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)