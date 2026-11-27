def fifo(pages, capacity):
    frames = []
    index = 0
    faults = 0

    for page in pages:
        if page not in frames:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1) % capacity

        print(f"Page {page}: {frames}")

    return faults

def lru(pages, capacity):
    frames = []
    last_used = {}
    faults = 0

    for time, page in enumerate(pages):
        if page not in frames:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)
            else:
                victim = min(frames, key=lambda p: last_used[p])
                frames[frames.index(victim)] = page

        last_used[page] = time
        print(f"Page {page}: {frames}")

    return faults

def optimal(pages, capacity):
    frames = []
    faults = 0

    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i + 1:]

                distances = [
                    future.index(p) if p in future else float("inf")
                    for p in frames
                ]

                victim = frames[distances.index(max(distances))]
                frames[frames.index(victim)] = page

        print(f"Page {page}: {frames}")

    return faults

pages = list(map(int, input("Enter page reference string: ").split()))
capacity = int(input("Enter number of frames: "))

if capacity <= 0:
    print("Number of frames must be positive")
else:
    print("1. FIFO")
    print("2. LRU")
    print("3. Optimal")

    choice = int(input("Enter choice: "))

    if choice == 1:
        faults = fifo(pages, capacity)
    elif choice == 2:
        faults = lru(pages, capacity)
    elif choice == 3:
        faults = optimal(pages, capacity)
    else:
        faults = None
        print("Invalid choice")

    if faults is not None:
        print("Total page faults =", faults)
