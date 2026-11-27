import os
import sys

print(f"Parent process: PID = {os.getpid()}", flush=True)

pid = os.fork()

if pid < 0:
    print("Fork failed")
    sys.exit(1)

elif pid == 0:
    print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}", flush=True)
    print("Child is about to exec 'ls -l'", flush=True)
    os.execlp("ls", "ls", "-l")

else:
    print(f"Parent waiting for child (PID = {pid}) to finish...", flush=True)
    child_pid, status = os.waitpid(pid, 0)
    exit_status = os.waitstatus_to_exitcode(status)
    print(f"Child exited with status {exit_status}")
    print("Parent process resumes and exits.")
