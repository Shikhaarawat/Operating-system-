def allocate(blocks, processes, method):
    free_blocks = blocks[:]
    result = [-1] * len(processes)

    for i, size in enumerate(processes):
        candidates = [
            j for j, block in enumerate(free_blocks)
            if block >= size
        ]

        if not candidates:
            continue

        if method == "first":
            index = candidates[0]
        elif method == "best":
            index = min(candidates, key=lambda j: free_blocks[j])
        else:
            index = max(candidates, key=lambda j: free_blocks[j])

        result[i] = index
        free_blocks[index] -= size

    print("\nProcess Size\tBlock")

    for i, size in enumerate(processes):
        block = result[i] + 1 if result[i] != -1 else "Not allocated"
        print(f"{size}\t\t{block}")

blocks = list(map(int, input("Enter block sizes: ").split()))
processes = list(map(int, input("Enter process sizes: ").split()))

print("1. First Fit")
print("2. Best Fit")
print("3. Worst Fit")

choice = int(input("Enter choice: "))

if choice == 1:
    allocate(blocks, processes, "first")
elif choice == 2:
    allocate(blocks, processes, "best")
elif choice == 3:
    allocate(blocks, processes, "worst")
else:
    print("Invalid choice")
