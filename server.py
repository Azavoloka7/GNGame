
import socket
import threading
import random

# Функція для обробки клієнтів
def handle_client(client_socket, secret_number):
    while True:
        try:
            guess = client_socket.recv(1024).decode()
            if not guess:
                break
            guess = int(guess)

            if guess == secret_number:
                client_socket.send("Вітаємо! Ви вгадали число!\n".encode())
                break
            elif guess < secret_number:
                client_socket.send("Число більше.\n".encode())
            else:
                client_socket.send("Число менше.\n".encode())
        except:
            break

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Сервер запущено. Очікування підключень...")

    secret_number = random.randint(0, 100)
    print(f"Загадане число: {secret_number}")

    while True:
        client_socket, addr = server.accept()
        print(f"Новий гравець підключився: {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, secret_number))
        client_thread.start()
if __name__ == "__main__":
    main()
