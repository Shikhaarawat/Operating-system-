import threading
import time

N = 5

forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)

def philosopher(pid):
    left = pid
    right = (pid + 1) % N

    for _ in range(2):
        print(f"Philosopher {pid} is thinking")
        time.sleep(0.1)

        room.acquire()
        forks[left].acquire()
        forks[right].acquire()

        print(f"Philosopher {pid} is eating")
        time.sleep(0.15)

        forks[right].release()
        forks[left].release()
        room.release()

        print(f"Philosopher {pid} finished eating")

threads = [
    threading.Thread(target=philosopher, args=(i,))
    for i in range(N)
]

for t in threads:
    t.start()

for t in threads:
    t.join()
