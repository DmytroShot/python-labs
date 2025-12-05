import socket
import threading
import json
import sys

HOST = "127.0.0.1"
PORT = 5000


def listen(sock):
    """Listen to server and print everything."""
    while True:
        try:
            raw = sock.recv(1024).decode("utf-8")
            if not raw:
                print("З’єднання розірвано сервером.")
                sys.exit(0)

            for line in raw.splitlines():
                data = json.loads(line)

                t = data["type"]

                if t == "positions":
                    print("\n--- Поточні позиції ---")
                    for u, pos in data["data"].items():
                        print(f"{u}: {pos}")
                    print("-----------------------")

                elif t == "position":
                    print(f"[POS] {data['user']} → ({data['x']}, {data['y']})")

                elif t == "message":
                    print(f"[CHAT] {data['user']}: {data['text']}")

                elif t == "join":
                    print(f"[JOIN] {data['user']} підключився.")

                elif t == "disconnect":
                    print(f"[LEFT] {data['user']} вийшов.")

        except Exception as e:
            print("Помилка:", e)
            sys.exit(0)


def main():
    username = input("Введіть своє ім'я: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    # Надсилаємо ім'я при підключенні
    sock.sendall((json.dumps({"user": username}) + "\n").encode("utf-8"))

    threading.Thread(target=listen, args=(sock,), daemon=True).start()

    print("Команди:")
    print("  /move x y — відправити координати")
    print("  будь-що інше — повідомлення в чат")

    while True:
        txt = input()

        if txt.startswith("/move"):
            try:
                _, x, y = txt.split()
                msg = {
                    "type": "position",
                    "user": username,
                    "x": float(x),
                    "y": float(y)
                }
            except:
                print("Формат: /move 12.5 33.8")
                continue

        else:
            msg = {
                "type": "message",
                "user": username,
                "text": txt
            }

        sock.sendall((json.dumps(msg) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
