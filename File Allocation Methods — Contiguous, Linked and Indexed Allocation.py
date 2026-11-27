def contiguous():
    start = int(input("Enter starting block: "))
    length = int(input("Enter file length: "))

    blocks = list(range(start, start + length))

    print("Allocated blocks:", blocks)

def linked():
    blocks = list(map(int, input("Enter available block numbers: ").split()))
    length = int(input("Enter file length: "))

    if length > len(blocks):
        print("Not enough blocks available")
        return

    allocated = blocks[:length]

    print("Block\tNext")

    for i, block in enumerate(allocated):
        next_block = allocated[i + 1] if i + 1 < len(allocated) else -1
        print(f"{block}\t{next_block}")

def indexed():
    index_block = int(input("Enter index block number: "))
    blocks = list(map(int, input("Enter file data block numbers: ").split()))

    print("Index block:", index_block)
    print("Index entries:", blocks)

print("1. Contiguous Allocation")
print("2. Linked Allocation")
print("3. Indexed Allocation")

choice = int(input("Enter choice: "))

if choice == 1:
    contiguous()
elif choice == 2:
    linked()
elif choice == 3:
    indexed()
else:
    print("Invalid choice")
