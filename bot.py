import random
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Bot Token'ınızı buraya girin
TOKEN = '7528327308:AAG5VxRb9QqArCLeP3gDxtJSE-m_jOV11Ho'

# İsim listesi
games = [
    "Gates of Olympus", "The Dog House", "Sweet Bonanza", "John Hunter and the Tomb of the Scarab Queen", 
    "Wolf Gold", "Great Rhino Megaways", "Big Bass Bonanza", "Fruit Party", "Release the Kraken", 
    "Madame Destiny Megaways", "Buffalo King Megaways", "Peking Luck", "Chilli Heat", "Dragon Tiger", 
    "The Dog House Megaways"
]

# 85 ile 98 arasında rastgele oran seçme fonksiyonu
def random_percentage():
    return random.uniform(85, 98)

# Haber gönderme fonksiyonu
def send_news(update: Update, context: CallbackContext):
    # Saat başı 5 rastgele oyun ve oran seçme
    selected_games = random.sample(games, 5)
    news_message = "Saat Başına Seçilen Oyunlar ve Oranlar:\n\n"
    
    for game in selected_games:
        news_message += f"{game}: {random_percentage():.2f}%\n"
    
    update.message.reply_text(news_message)

# Start komutunun işlevi
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot çalışıyor. /news komutunu kullanarak haber alabilirsiniz.")

# Main fonksiyonu
def main():
    # Updater ve Dispatcher'ı başlatma
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Komutları ekleyelim
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("news", send_news))

    # Botu çalıştırma
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
