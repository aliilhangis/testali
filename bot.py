import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler

# Oyun listesi
games = [
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

# Rastgele 5 oyun seçip oran atayan fonksiyon
def generate_random_games_and_rates():
    selected_games = random.sample(games, 5)  # Rastgele 5 oyun seç
    result = [f"{game}: {random.uniform(85, 98):.2f}" for game in selected_games]  # Her birine 85-98 arası oran ata
    return "\n".join(result)

# /start komutu için yanıt
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Merhaba! Bu bot saat başı rastgele oyunlar ve oranlar paylaşır.")

# Saatlik mesaj gönderme
def send_hourly_message(context: CallbackContext) -> None:
    chat_id = context.job.context
    random_games_and_rates = generate_random_games_and_rates()
    context.bot.send_message(chat_id=chat_id, text=f"Rastgele oyunlar ve oranlar:\n\n{random_games_and_rates}")

# /başlat komutu ile zamanlayıcı başlatma
def schedule_job(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(send_hourly_message, interval=3600, first=0, context=chat_id)
    update.message.reply_text("Saatlik gönderim başladı!")

def main():
    # Telegram Bot Token
    TOKEN = "7528327308:AAG5VxRb9QqArCLeP3gDxtJSE-m_jOV11Ho"
    
    # Botun çalıştırılması
    application = Application.builder().token(TOKEN).build()
dispatcher = application.dispatcher

    # Komutları tanımlama
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("başlat", schedule_job))

    # Zamanlayıcıyı başlat
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
