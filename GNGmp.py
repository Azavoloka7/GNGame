import random

def guess_number_game(num_players):
    # Генеруємо випадкове число від 0 до 100
    secret_number = random.randint(0, 100)
    players = []

    # Запитуємо імена гравців
    for i in range(num_players):
        name = input(f"Введіть ім'я гравця {i+1}: ")
        players.append({'name': name, 'score': 0})

    guessed = False

    while not guessed:
        for player in players:
            guess = int(input(f"{player['name']}, введіть ваше припущення (0-100): "))
            if guess == secret_number:
                print(f"Вітаємо, {player['name']}! Ви вгадали число!")
                player['score'] += 1
                guessed = True
                break
            elif guess < secret_number:
                print("Число більше.")
            else:
                print("Число менше.")
    
    # Виводимо результати гри
    print("\nРезультати гри:")
    for player in players:
        print(f"{player['name']}: {player['score']} бал(ів)")

if __name__ == "__main__":
    num_players = int(input("Введіть кількість гравців: "))
    guess_number_game(num_players)
