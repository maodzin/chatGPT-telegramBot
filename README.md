#ChatGPT Telegram Bot
This is a Telegram bot built using the aiogram library in Python. The bot uses the GPT-3.5 architecture to generate responses to user messages based on the chat history.

##Setup
To use this bot, you will need to obtain a Telegram bot API token and a GPT-3.5 API key. These values should be stored in a config.py file in the following format:

python
Copy code
token = "YOUR_TELEGRAM_BOT_API_TOKEN"
api_key = "YOUR_GPT_3.5_API_KEY"
Once you have obtained these keys, you can run the bot by executing the main.py file.

##Usage
The bot responds to two commands:

/start - This command resets the chat history and prompts the user to send a message to start chatting.
/reset - This command resets the chat history and context.
The bot also includes a custom keyboard layout with a "Reset" button that can be used to reset the chat history and context.

To chat with the bot, simply send a message and wait for a response. The bot will generate a response based on the chat history and send it back to the user.

The chat history is stored in a list called history, and the current prompt is stored in a string called prompt. The generate_response() function in the backend.py file is responsible for generating responses based on the chat history.

##Contributors
Maksym Pokrovskyi - maxxox@gmail.com - [YOUR WEBSITE HERE]
