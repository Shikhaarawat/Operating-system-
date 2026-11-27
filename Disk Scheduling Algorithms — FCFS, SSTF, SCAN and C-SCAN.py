def fcfs(requests, head):
    order = requests[:]
    movement = 0
    current = head

    for track in order:
        movement += abs(track - current)
        current = track

    return order, movement

def sstf(requests, head):
    pending = requests[:]
    order = []
    movement = 0
    current = head

    while pending:
        track = min(pending, key=lambda x: abs(x - current))

        movement += abs(track - current)
        current = track
        order.append(track)
        pending.remove(track)

    return order, movement

def scan(requests, head, disk_size, direction):
    lower = sorted(x for x in requests if x < head)
    upper = sorted(x for x in requests if x >= head)

    if direction == "left":
        sequence = list(reversed(lower)) + [0] + upper
    else:
        sequence = upper + [disk_size - 1] + list(reversed(lower))

    order = []
    movement = 0
    current = head

    for track in sequence:
        movement += abs(track - current)
        current = track

        if track in requests and track not in order:
            order.append(track)

    return order, movement

def cscan(requests, head, disk_size, direction):
    lower = sorted(x for x in requests if x < head)
    upper = sorted(x for x in requests if x >= head)

    if direction == "right":
        sequence = upper + [disk_size - 1, 0] + lower
    else:
        sequence = list(reversed(lower)) + [0, disk_size - 1] + list(reversed(upper))

    order = []
    movement = 0
    current = head

    for track in sequence:
        movement += abs(track - current)
        current = track

        if track in requests and track not in order:
            order.append(track)

    return order, movement

requests = list(map(int, input("Enter disk requests: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))
direction = input("Enter direction (left/right): ").strip().lower()

print("1. FCFS")
print("2. SSTF")
print("3. SCAN")
print("4. C-SCAN")

choice = int(input("Enter choice: "))

if choice == 1:
    order, movement = fcfs(requests, head)
elif choice == 2:
    order, movement = sstf(requests, head)
elif choice == 3:
    order, movement = scan(requests, head, disk_size, direction)
elif choice == 4:
    order, movement = cscan(requests, head, disk_size, direction)
else:
    order = None
    movement = None
    print("Invalid choice")

if order is not None:
    print("Seek sequence:", order)
    print("Total head movement:", movement)
