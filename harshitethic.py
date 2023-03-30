import telegram.ext
import openai

# Set up the Telegram bot
bot_token = "5794438845:AAGwYnguPlnRwH7gMSyjIUZSjkx8OF6fg9Y"
updater = telegram.ext.Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Set up the OpenAI API
openai.api_key = "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"

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the incoming message text and chat ID
    message_text = update.message.text
    chat_id = update.message.chat_id
    
    # Generate a response using GPT-3
    response = generate_response(message_text)
    
    # Send the response back to the user
    context.bot.send_message(chat_id=chat_id, text=response)

# Define a function to generate a response using GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Register the message handler function
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
