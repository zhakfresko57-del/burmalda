import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from urllib.parse import quote
import os

TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 **ГДЗ БОТ**\n\nНапиши задание, например:\n• 7 класс алгебра №234",
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    query = quote(user_message)
    
    keyboard = [
        [InlineKeyboardButton("📘 ГДЗ.РУ", url=f"https://gdz.ru/search/?q={query}")],
        [InlineKeyboardButton("📗 Мегарешеба", url=f"https://megaresheba.ru/index/0-?s={query}")],
        [InlineKeyboardButton("🔍 Google", url=f"https://www.google.com/search?q=гдз+{query}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🔍 **Результаты для:** {user_message}",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🚀 ГДЗ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()