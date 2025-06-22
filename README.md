# Distributed Task Executor using Python Sockets

A lightweight distributed task execution system using plain TCP sockets in Python. This project simulates a coordinator-worker architecture, where a central coordinator delegates categorized instructions to specialized worker nodes (`a`, `b`, and `c`) and maintains order of execution.

---

## 🚀 Features

- **Task Categorization**: Instructions are grouped by their initial character (e.g., `a1`, `b3`, etc.)
- **Simple TCP Communication**: Uses Python’s built-in `socket` library
- **Instruction Distribution**: Coordinator sends grouped instructions to appropriate worker nodes
- **Graceful Shutdown**: Workers shutdown gracefully upon receiving `SHUTDOWN` signal

---

## 🛠 Architecture Overview

### Coordinator (`coordinator.py`)

- Reads tasks from `input.txt`
- Categorizes instructions by type (`a`, `b`, `c`)
- Sends instructions to the corresponding worker (host: `localhost`, port: 8001–8003)
- Waits for task completion acknowledgment
- Sends shutdown signal

### Worker Node (`worker_node.py`)

- Listens on its designated port for tasks
- Executes each received instruction (simulated delay)
- Acknowledges completion
- Waits for `SHUTDOWN` command and exits gracefully

---

## 📄 Input Format

Instructions must be placed in `input.txt`, space-separated.

### Example:
```
a1 a2 c1 b1 c2 b3 b2 b4 a3
```

These will be distributed as:
- `a`: a1, a2, a3
- `b`: b1, b3, b2, b4
- `c`: c1, c2

---

## 📦 How to Run

### 1. Start Worker Nodes (in separate terminals)
```
python worker_node.py --type a --port 8001
python worker_node.py --type b --port 8002
python worker_node.py --type c --port 8003
```

### 2. Start Coordinator
```
python coordinator.py
```

---

## 🔧 File Structure

```
.
├── coordinator.py       # Main controller that delegates tasks
├── worker_node.py       # Worker logic for executing instructions
├── input.txt            # Input file containing space-separated tasks
└── README.md            # Project documentation
```

---

## 💡 Sample Output

```
[Worker a] Listening on port 8001...
[Worker b] Listening on port 8002...
[Worker c] Listening on port 8003...

[Coordinator] Starting task distribution
[Coordinator] Sent to a: a1 a2 a3
[Coordinator] a says: a1 a2 a3 completed
[Coordinator] a shutdown: Goodbye from a

[Coordinator] Sent to b: b1 b3 b2 b4
[Coordinator] b says: b1 b3 b2 b4 completed
[Coordinator] b shutdown: Goodbye from b

[Coordinator] Sent to c: c1 c2
[Coordinator] c says: c1 c2 completed
[Coordinator] c shutdown: Goodbye from c
```

---

## 🔮 Future Improvements

- Add dynamic node discovery
- Real-time execution tracking
- Upgrade to asynchronous sockets or `asyncio`
- Implement global task sequencing across workers
- Add retry logic and fault tolerance

---

## 📜 License

This project is for academic and demonstration purposes. Use it freely under MIT license.

---

## 👨‍💻 Author

Built with ❤️ by [Your Name] as part of a distributed systems challenge.
