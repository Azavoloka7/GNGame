import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    print("Підключено до сервера. Починаємо гру!")
    while True:
        guess = input("Введіть ваше припущення (0-100): ")
        client.send(guess.encode())

        response = client.recv(1024).decode()
        print(response)
        
        if "Вітаємо" in response:
            break

    client.close()

if __name__ == "__main__":
    main()
