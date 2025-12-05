import socket
import threading
import json

HOST = "0.0.0.0"
PORT = 5000

clients = {}        # socket → username
positions = {}      # username → (x, y)
lock = threading.Lock()


def broadcast(message, exclude_sock=None):
    """Send message (dict) to all connected clients except exclude_sock."""
    data = (json.dumps(message) + "\n").encode("utf-8")
    with lock:
        for sock in list(clients.keys()):
            if sock is not exclude_sock:
                try:
                    sock.sendall(data)
                except:
                    remove_client(sock)


def remove_client(sock):
    """Remove a disconnected client and notify others."""
    with lock:
        if sock in clients:
            username = clients[sock]
            print(f"[DISCONNECT] {username}")
            del clients[sock]
            if username in positions:
                del positions[username]

            # Broadcast that the user left
            broadcast({"type": "disconnect", "user": username})

        try:
            sock.close()
        except:
            pass


def handle_client(sock, addr):
    print(f"[CONNECT] {addr}")

    try:
        # Перше повідомлення — ім'я
        raw = sock.recv(1024).decode("utf-8").strip()
        info = json.loads(raw)
        username = info["user"]

        with lock:
            clients[sock] = username
            positions[username] = (0, 0)

        # Надсилаємо усім, що новий клієнт підключився
        broadcast({"type": "join", "user": username})

        # Надсилаємо новому клієнту поточні позиції
        sock.sendall((json.dumps({
            "type": "positions",
            "data": positions
        }) + "\n").encode("utf-8"))

        # Основний цикл
        while True:
            raw = sock.recv(1024).decode("utf-8")
            if not raw:
                break

            for line in raw.splitlines():
                data = json.loads(line)

                if data["type"] == "position":
                    x, y = float(data["x"]), float(data["y"])
                    with lock:
                        positions[username] = (x, y)

                    broadcast(data, exclude_sock=None)

                elif data["type"] == "message":
                    broadcast(data, exclude_sock=None)

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        remove_client(sock)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        sock, addr = server.accept()
        threading.Thread(target=handle_client, args=(sock, addr), daemon=True).start()


if __name__ == "__main__":
    main()
