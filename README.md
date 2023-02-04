# OpenAI ChatGPT Chatbot Demo
A simple CLI chatbot using the leaked model of OpenAI's ChatGPT.

# Project Setup
Create a virtual environment using the following command in the project directory:

```bash
python -m venv venv
```

And activate the virtual environment:

```bash
source venv/bin/activate # for linux
./venv/Scripts/Activate  # for Windows
```

Finally, install the required packages using:

```bash
pip install -e .
```

# Environment Variables
You will need to set the environment variable **OPENAI_API_KEY** to your OpenAI API key.

# Configuration
You can configure your bot's name and the initial prompt to sent to your bot in the data/bot_name.txt and data/initial_prompt.txt file, respectively.
By default, the maximum number of latest messages that will be kept during the conversation is 5. You can increase this limit by providing a value for the max_message_count in the User class's \_\_init\_\_. But of course, it will deplete your tokens faster with higher limit as you chat for longer.

# Caveat
Note that the initial prompt in the data/initial_prompt.txt file is inserted to your message each time you send along with chat history.

# Demo
You can run the direct conversation demo using the following command:

```bash
python demo/direct_chat.py
```
