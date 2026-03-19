import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Токен из переменных окружения
TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

PHRASES = [
    "Здарова, мудак!",
    "Иди нахуй!",
    "Сам такой, блять!",
    "Отвали, гандон!",
    "Чё надо, долбоёб?",
    "Не беси меня, сука!",
    "Пошёл нахуй со своими вопросами!"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name or "чувак"
    await update.message.reply_text(f"🤬 Бурмалдина в облаке! Здарова, {user_name}!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(PHRASES))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🚀 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()