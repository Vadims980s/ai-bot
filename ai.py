import datetime
import random

print("Hello, I am your virtual assistant.")
bot_name = input("What will be the bot's name? ")
print(bot_name, "will be your bot's name!")
print("Great! Now before we begin, I shall ask you one more question.")
name = input("What's your name? ")
print("Greetings", name + "!")
def functions():
    print("What would you like to do? ")
    print("0 - Check the time")
    print("1 - Check the date")
    print("2 - Play Rock, Paper, Scissors")
    print("3 - Guess my number")
    print("4 - Learn fun facts")
    print("5 - Exit")
functions()
answer = int(input("What would you like to do? "))
if answer == 0:
    date_time = datetime.datetime.now()
    print("The time is", date_time.time())
if answer == 1:
    date_time = datetime.datetime.now()
    print("Today is", date_time.date())
if answer == 2:
    gamelist = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    print("To get started, what will you choose?")
    print(f"\n 1 - {gamelist[0]} \n 2 - {gamelist[1]} \n 3 - {gamelist[2]}")
    user = int(input("Pick a number from 1-3: "))
    user = gamelist[user - 1]
    print("Your choice:", user)
    bot = random.randint(1, 3)
    bot = gamelist[bot - 1]
    print("Your bot:", bot)
    if user == bot:
        print("It's a tie")
    elif (user == "rock" and bot == "scissors") or\
        (user == "scissors" and bot == "paper") or\
        (user == "paper" and bot == "rock") :
        print("You won!")
    else:
        print("You lost...")
if answer == 3:
    number = random.randint(1, 100)
    while True:
        guess = int(input("Guess the number from 1-100! "))
        if guess == number - 1 or guess == number + 1:
            print("Close enough. Good job!")
            break
        elif guess > number:
            print("Number is too big. Try again.")
        elif guess < number:
            print("Number is too small. Try again.")
        else:
            print("Well done! You just guessed the number!")
            break
if answer == 4:
    facts = {
    'A': 'I am invincible',
    'B': 'You can be anything!',
    'C': 'I can talk in any language, including beep-boop!',
    'D': 'Robots are going to replace humans in 2050.',
    'E': 'Tip: If anything, contact anyone in need of help!'
    }
    letter_facts = ['A', 'B', 'C', 'D', 'E']
    facts_items = ['I am invincible', 'You can be anything!', 'I can talk in any language, including beep-boop!', 'Robots are going to replace humans in 2050.', 'Tip: If anything, contact anyone in need of help!']
    for ran_fact in range(5):
        print(letter_facts)
        facts_ask = input(
            "I have 5 facts, which kind of facts would you like to hear about? ")
        if facts_ask in letter_facts:
            print(f"{facts[facts_ask]}")
if answer == 5:
    import sys
    sys.exit()
