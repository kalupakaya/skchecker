from pyrogram import Client, filters
from pyrogram.types import Message
from ipgen import thread, valid, genip

# Replace with your API ID and API hash
API_ID = 4730697
API_HASH = '5b451ec5950aae4b8e914359c7975dca'
BOT_TOKEN = '6467875273:AAHxShcMmP1NEJTQI9MakV9LmGUhlK7O6y0'

# Create a Pyrogram client instance
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define a command handler for the /start command
@app.on_message(filters.command("start"))
def start_command_handler(client: Client, message: Message):
    # Reply to the user with a welcome message
    message.reply_text("Welcome to MyBot! Type /help for more options.")

@app.on_message(filters.command("gen"))
def gen_command_handler(client, message):
    # Extract the number from the command
    command_parts = message.text.split()
    if len(command_parts) == 2:
        try:
            number = int(command_parts[1])
            msg = message.reply_text("~ Generating..")
            genip(msg, number)
        except ValueError:
            client.send_message(message.chat.id, "Invalid number format")
    else:
        client.send_message(message.chat.id, "Invalid command format")

@app.on_message(filters.command("run"))
def validator(client, message):
    message.reply_text("~ Checking..")
    thread(message)

# Run the bot
if __name__ == "__main__":
    app.run()
