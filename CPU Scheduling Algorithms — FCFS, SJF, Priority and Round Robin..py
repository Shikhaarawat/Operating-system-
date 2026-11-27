def display(processes):
    total_wt = sum(p["wt"] for p in processes)
    total_tat = sum(p["tat"] for p in processes)

    print("\nPID\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        print(f'{p["pid"]}\t{p["at"]}\t{p["bt"]}\t{p["ct"]}\t{p["tat"]}\t{p["wt"]}')

    print(f"Average Waiting Time = {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f}")

def fcfs(data):
    ps = [p.copy() for p in data]
    ps.sort(key=lambda p: p["at"])
    time = 0

    for p in ps:
        time = max(time, p["at"]) + p["bt"]
        p["ct"] = time
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]

    display(ps)

def sjf(data):
    ps = [p.copy() for p in data]
    done = set()
    time = 0
    completed = 0

    while completed < len(ps):
        ready = [i for i, p in enumerate(ps) if i not in done and p["at"] <= time]

        if not ready:
            time += 1
            continue

        idx = min(ready, key=lambda i: ps[i]["bt"])
        p = ps[idx]

        time += p["bt"]
        p["ct"] = time
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]

        done.add(idx)
        completed += 1

    display(ps)

def priority(data):
    ps = [p.copy() for p in data]
    done = set()
    time = 0
    completed = 0

    while completed < len(ps):
        ready = [i for i, p in enumerate(ps) if i not in done and p["at"] <= time]

        if not ready:
            time += 1
            continue

        idx = min(ready, key=lambda i: ps[i]["pr"])
        p = ps[idx]

        time += p["bt"]
        p["ct"] = time
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]

        done.add(idx)
        completed += 1

    display(ps)

def round_robin(data, quantum):
    ps = [p.copy() for p in data]

    for p in ps:
        p["rem"] = p["bt"]

    queue = []
    time = 0
    completed = 0
    added = set()

    while completed < len(ps):
        for i, p in enumerate(ps):
            if i not in added and p["at"] <= time:
                queue.append(i)
                added.add(i)

        if not queue:
            time += 1
            continue

        idx = queue.pop(0)
        p = ps[idx]

        run = min(p["rem"], quantum)
        time += run
        p["rem"] -= run

        for i, other in enumerate(ps):
            if i not in added and other["at"] <= time:
                queue.append(i)
                added.add(i)

        if p["rem"] > 0:
            queue.append(idx)
        else:
            p["ct"] = time
            p["tat"] = p["ct"] - p["at"]
            p["wt"] = p["tat"] - p["bt"]
            completed += 1

    display(ps)

n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at, bt, pr = map(int, input(f"Process {i + 1} - AT BT Priority: ").split())
    processes.append({"pid": i + 1, "at": at, "bt": bt, "pr": pr})

print("1. FCFS")
print("2. SJF")
print("3. Priority")
print("4. Round Robin")

choice = int(input("Enter choice: "))

if choice == 1:
    fcfs(processes)
elif choice == 2:
    sjf(processes)
elif choice == 3:
    priority(processes)
elif choice == 4:
    quantum = int(input("Enter time quantum: "))
    round_robin(processes, quantum)
else:
    print("Invalid choice")
