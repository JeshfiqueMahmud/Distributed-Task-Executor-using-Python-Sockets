
import socket
import time

INSTRUCTION_FILE = "input.txt"
WORKERS = {
    "a": ("localhost", 8001),
    "b": ("localhost", 8002),
    "c": ("localhost", 8003)
}

def send_tasks(worker_type, tasks):
    host, port = WORKERS[worker_type]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        task_data = " ".join(tasks)
        s.sendall(task_data.encode())
        print(f"[Coordinator] Sent to {worker_type}: {task_data}")
        response = s.recv(1024).decode()
        print(f"[Coordinator] {worker_type} says: {response}")

        # Send shutdown message
        s.sendall(b"SHUTDOWN")
        shutdown_ack = s.recv(1024).decode()
        print(f"[Coordinator] {worker_type} shutdown: {shutdown_ack}")

def main():
    print("[Coordinator] Starting task distribution")
    with open(INSTRUCTION_FILE) as f:
        instructions = f.read().split()

    grouped = {"a": [], "b": [], "c": []}
    for instr in instructions:
        t = instr[0]
        if t in grouped:
            grouped[t].append(instr)

    for task_type, tasks in grouped.items():
        if tasks:
            send_tasks(task_type, tasks)
            time.sleep(0.5)

if __name__ == "__main__":
    main()
