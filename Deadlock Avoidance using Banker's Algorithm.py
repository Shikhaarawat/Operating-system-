P = 5
R = 3

available = list(map(int, input("Enter available resources: ").split()))

maximum = []
allocation = []

print("Enter Max matrix:")

for i in range(P):
    maximum.append(list(map(int, input(f"P{i}: ").split())))

print("Enter Allocation matrix:")

for i in range(P):
    allocation.append(list(map(int, input(f"P{i}: ").split())))

need = [
    [maximum[i][j] - allocation[i][j] for j in range(R)]
    for i in range(P)
]

def safe_state(avail, alloc, needs):
    work = avail[:]
    finish = [False] * P
    sequence = []

    while len(sequence) < P:
        found = False

        for i in range(P):
            if not finish[i] and all(needs[i][j] <= work[j] for j in range(R)):
                for j in range(R):
                    work[j] += alloc[i][j]

                finish[i] = True
                sequence.append(i)
                found = True

        if not found:
            return False, []

    return True, sequence

safe, sequence = safe_state(available, allocation, need)

if safe:
    print("System is in a safe state.")
    print("Safe sequence:", " -> ".join(f"P{i}" for i in sequence))
else:
    print("System is not in a safe state.")

process = int(input("Enter process number (0-4): "))
request = list(map(int, input("Enter request vector: ").split()))

if all(request[j] <= need[process][j] for j in range(R)) and all(request[j] <= available[j] for j in range(R)):
    new_available = [available[j] - request[j] for j in range(R)]
    new_allocation = [row[:] for row in allocation]
    new_need = [row[:] for row in need]

    for j in range(R):
        new_allocation[process][j] += request[j]
        new_need[process][j] -= request[j]

    request_safe, request_sequence = safe_state(
        new_available,
        new_allocation,
        new_need
    )

    if request_safe:
        print("Request can be granted.")
        print("Safe sequence:", " -> ".join(f"P{i}" for i in request_sequence))
    else:
        print("Request cannot be granted.")
else:
    print("Invalid request or resources unavailable.")
