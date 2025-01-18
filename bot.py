import random
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# Bot Token
TOKEN = '7528327308:AAG5VxRb9QqArCLeP3gDxtJSE-m_jOV11Ho'

# Oyun listesi
games = [
    "Gates of Olympus", "The Dog House", "Sweet Bonanza", "John Hunter and the Tomb of the Scarab Queen", 
    "Wolf Gold", "Great Rhino Megaways", "Big Bass Bonanza", "Fruit Party", "Release the Kraken", 
    "Madame Destiny Megaways", "Buffalo King Megaways", "Peking Luck", "Chilli Heat", "Dragon Tiger", 
    "The Dog House Megaways"
]

# Rastgele yüzde seçme fonksiyonu
def random_percentage():
    return random.uniform(85, 98)

# Start komutu işleyicisi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot çalışıyor. /news komutunu kullanarak haber alabilirsiniz.")

# Haber gönderme fonksiyonu
async def send_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_games = random.sample(games, 5)
    news_message = "Saat Başına Seçilen Oyunlar ve Oranlar:\n\n"
    
    for game in selected_games:
        news_message += f"{game}: {random_percentage():.2f}%\n"
    
    await update.message.reply_text(news_message)

# Ana fonksiyon
async def main():
    # Uygulamayı başlat
    application = Application.builder().token(TOKEN).build()
    
    # Komut işleyicilerini ekle
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("news", send_news))
    
    # Botu başlat
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
