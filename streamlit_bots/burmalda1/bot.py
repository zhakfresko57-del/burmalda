import telebot
import random
import os
import time

# Токен из переменных окружения
TOKEN = os.environ.get("BOT_TOKEN")

# Создаём бота
bot = telebot.TeleBot(TOKEN)

PHRASES = [
    "Здарова, мудак!",
    "Иди нахуй!",
    "Сам такой, блять!",
    "Отвали, гандон!",
    "Чё надо, долбоёб?",
    "Не беси меня, сука!",
    "Пошёл нахуй со своими вопросами!"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name or "чувак"
    bot.reply_to(message, f"🤬 Бурмалдина в облаке! Здарова, {user_name}!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, random.choice(PHRASES))

print("🚀 Бот запущен!")
bot.infinity_polling()
