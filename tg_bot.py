from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token
from backend import generate_response

bot = Bot(token=token)
dp = Dispatcher(bot)

history = []
prompt = ''

# Create a custom keyboard layout
reset_button = ["Reset"]
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*reset_button)

@dp.message_handler(commands=['start'])
async def start_cmd_handler(message: types.Message):
    global history
    # Reset the chat history and context
    history = []
    await message.reply('Hi! Send me a message to start chatting.', reply_markup=keyboard)

@dp.message_handler(commands=['reset'])
async def reset_cmd_handler(message: types.Message):
    global history
    # Reset the chat history and context
    history = []
    await message.reply('Chat history and context reset.', reply_markup=keyboard)

@dp.message_handler(Text(equals="Reset"))
async def reset_button_handler(message: types.Message):

    global history
    # Reset the chat history and context
    history = []
    await message.reply('Chat history and context reset.', reply_markup=keyboard)

@dp.message_handler()
async def chat_handler(message: types.Message):
    global history, prompt
    # Update the chat history with the current message
    if message.text:
        history.append(f"Me: {message.text}")

    if len(history) > 8:
        history = history[-7:]
        prompt = ' '.join(history)
    else:
        prompt = ' '.join(history)

    # Generate a response based on the chat history
    response = generate_response(prompt)

    # Update the chat context with any relevant information from the response
    history.append(f"- {response}")

    # Send the response to the user
    if response:
        await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
