import time

from helpers import read_file
from chatbot import User, Bot


def main() -> None:
    chatgpt_preamble = read_file("chatgpt-preamble.txt")
    chatgpt_preamble = f"{chatgpt_preamble}\nCurrent date: {time.strftime('%Y-%m-%d')}"
    initial_prompt = read_file("initial-prompt.txt")

    # Add the bot name and username to the initial prompt.
    # You can remove this if you alreacy have the bot name and username in the initial prompt.
    username = input("What is your name? ")
    bot_name = read_file("bot-name.txt")
    bot_initial_prompt = f"{chatgpt_preamble}\n\n{initial_prompt}\nI want you to act as if your name is {bot_name}.\n" \
        f"And pretend you are talking to a person called {username}."

    user = User(username)
    bot = Bot(bot_name, bot_initial_prompt)

    while True:
        prompt = input(f"{user.name}> ").strip()
        response = user.send_message(bot, prompt)
        print(f"{bot.name}: {response}")

        # Avoid hogging CPU too much by sleeping for one second.
        time.sleep(1)


if __name__ == "__main__":
    main()
