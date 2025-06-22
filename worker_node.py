
import socket
import argparse

BUFFER_SIZE = 1024

def start_worker(port, task_type):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('localhost', port))
        server.listen(1)
        print(f"[{task_type.upper()} Node] Listening on port {port}...")

        conn, addr = server.accept()
        with conn:
            print(f"[{task_type.upper()} Node] Connected by {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                message = data.decode().strip()

                if message == "SHUTDOWN":
                    conn.sendall(b"ACK_SHUTDOWN")
                    print(f"[{task_type.upper()} Node] Shutdown acknowledged.")
                    break

                print(f"[{task_type.upper()} Node] Received: {message}")
                tasks = message.split()
                for task in tasks:
                    print(f"[{task_type.upper()} Node] Executing task: {task}")

                conn.sendall(b"Tasks Completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, type=int, help="Port to listen on")
    parser.add_argument("--type", required=True, choices=["a", "b", "c"], help="Type of task this node handles")
    args = parser.parse_args()

    start_worker(args.port, args.type)
