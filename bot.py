from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '8084491198:AAER87m72_f8OcD1YzSBG1l2BctGI0b-fTY'

# Replace 'YOUR_CHAT_ID' with your Telegram chat ID where you want to receive feedback
ADMIN_CHAT_ID = '5010103329'

# Define the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Welcome to the Feedback Bot. Please send your feedback anytime.')

# Define a function to handle feedback
async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    feedback = update.message.text
    user = update.message.from_user
    user_info = f"Feedback received from {user.first_name} ({user.username}):\n{feedback}"
    
    # Send feedback to admin (your chat ID)
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=user_info)
    await update.message.reply_text('Thank you for your feedback!')

# Main function to set up the bot
def main():
    # Set up the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
