import threading

NUM_THREADS = 4
N = 1000000
results = [0] * NUM_THREADS

def sum_range(index, start, end):
    total = sum(range(start, end))
    results[index] = total
    print(f"Thread {index + 1}: sum[{start}..{end}) = {total}")

threads = []
chunk = N // NUM_THREADS

for i in range(NUM_THREADS):
    start = i * chunk
    end = N if i == NUM_THREADS - 1 else (i + 1) * chunk
    thread = threading.Thread(target=sum_range, args=(i, start, end))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Total sum (0 to {N - 1}) computed using {NUM_THREADS} threads = {sum(results)}")
