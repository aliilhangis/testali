import os
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
import random

# Bot Token
TOKEN = '7528327308:AAG5VxRb9QqArCLeP3gDxtJSE-m_jOV11Ho'

# Oyun listesi
games = [
    "Gates of Olympus", "The Dog House", "Sweet Bonanza", "John Hunter and the Tomb of the Scarab Queen", 
    "Wolf Gold", "Great Rhino Megaways", "Big Bass Bonanza", "Fruit Party", "Release the Kraken", 
    "Madame Destiny Megaways", "Buffalo King Megaways", "Peking Luck", "Chilli Heat", "Dragon Tiger", 
    "The Dog House Megaways"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot çalışıyor. /news komutunu kullanarak haber alabilirsiniz.")

async def send_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_games = random.sample(games, 5)
    news_message = "Saat Başına Seçilen Oyunlar ve Oranlar:\n\n"
    
    for game in selected_games:
        percentage = random.uniform(85, 98)
        news_message += f"{game}: {percentage:.2f}%\n"
    
    await update.message.reply_text(news_message)

def main():
    # Bot uygulamasını oluştur
    app = Application.builder().token(TOKEN).build()
    
    # Komut işleyicilerini ekle
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", send_news))
    
    # Botu başlat
    print("Bot başlatılıyor...")
    app.run_polling(poll_interval=3.0, timeout=30)

if __name__ == '__main__':
    main()
