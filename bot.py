from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
import random
import logging
from datetime import datetime
import pytz

# Loglama ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Bot Token
TOKEN = 'BURAYA_BOT_TOKENINIZI_YAZIN'

# Oyun listesi
GAMES = [
    "Gates of Olympus",
    "The Dog House",
    "Sweet Bonanza",
    "John Hunter and the Tomb of the Scarab Queen",
    "Wolf Gold",
    "Great Rhino Megaways",
    "Big Bass Bonanza",
    "Fruit Party",
    "Release the Kraken",
    "Madame Destiny Megaways",
    "Buffalo King Megaways",
    "Peking Luck",
    "Chilli Heat",
    "Dragon Tiger",
    "The Dog House Megaways"
]

# Komut işleyicileri
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = """
🎰 Hoş Geldiniz! 

Komutlar:
/slots - Güncel slot oranlarını gösterir
    """
    await update.message.reply_text(welcome_message)

async def get_slots(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Türkiye saat dilimini ayarla
    tz = pytz.timezone('Europe/Istanbul')
    current_time = datetime.now(tz).strftime('%H:%M')
    
    # 5 rastgele oyun seç
    selected_games = random.sample(GAMES, 5)
    
    # Mesajı oluştur
    message = f"🎰 {current_time} Slot Oranları 🎰\n\n"
    
    for game in selected_games:
        # 85-98 arası random oran
        rate = random.uniform(85, 98)
        message += f"🎮 {game}\n"
        message += f"📊 Oran: %{rate:.2f}\n\n"
    
    await update.message.reply_text(message)

def main():
    # Uygulama oluştur
    application = Application.builder().token(TOKEN).build()
    
    # Komutları ekle
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("slots", get_slots))
    
    # Botu başlat
    print("Bot başlatıldı...")
    application.run_polling(poll_interval=1.0)

if __name__ == '__main__':
    main()
