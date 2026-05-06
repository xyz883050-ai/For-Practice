n = int(input("Enter number of processes: "))

p = []
bt = []

for i in range(n):
    p.append(input("Process name: "))
    bt.append(int(input("Burst Time: ")))

tq = int(input("Enter Time Quantum: "))

rt = bt.copy()   # Remaining Time
ct = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
gantt = []

while True:
    done = True

    for i in range(n):
        if rt[i] > 0:
            done = False

            gantt.append(p[i])

            if rt[i] > tq:
                time += tq
                rt[i] -= tq
            else:
                time += rt[i]
                ct[i] = time
                rt[i] = 0

    if done:
        break

# Calculate TAT and WT
for i in range(n):
    tat[i] = ct[i]   # Assuming Arrival Time = 0
    wt[i] = tat[i] - bt[i]

# Gantt Chart
print("\nGantt Chart")
for process in gantt:
    print("|", process, end=" ")
print("|")

# Process Table
print("\nProcess\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(p[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAverage Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)