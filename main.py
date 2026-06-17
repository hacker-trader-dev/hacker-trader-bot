import sys
import subprocess

# Render par sahi version force karne ke liye
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot==20.8", "Flask==3.0.2"])

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import threading
from flask import Flask

BOT_TOKEN = "8721463485:AAER6rDSuaoMRbMZJs508qyc32aDldxRyfA"
REFERRAL_LINK = "https://broker-qx.pro/sign-up/?lid=2155703"
WHATSAPP_LINK = "https://wa.me/923412579993?text=Hi%20Hacker%20Trader,%20I%20need%20the%20bot%20license%20Key."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"⚡ <b>WELCOME TO THE HACKER TRADER PREMIUM BOT</b> ⚡\n\n"
        f"Hello {user.first_name}! This is an advanced AI Binary Options analysis bot.\n\n"
        f"🏆 <b>To Access the Bot, choose one option below:</b>\n"
        f"1️⃣ <b>FREE ACCESS:</b> Create a new account via our Referral Link and send your Trader ID to Admin.\n"
        f"2️⃣ <b>PREMIUM KEY:</b> If you already have an account, enter your Secret License Key using /key command."
    )
    
    keyboard = [
        [InlineKeyboardButton("👉 Create Quotex Account 👈", url=REFERRAL_LINK)],
        [InlineKeyboardButton("💬 Get Secret Key via WhatsApp", url=WHATSAPP_LINK)]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")

async def verify_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide the key. Example: <code>/key YOUR_SECRET_KEY</code>", parse_mode="HTML")
        return
        
    user_key = context.args[0]
    if user_key == "HACKER2026":
        success_text = (
            "🚀 <b>ACCESS GRANTED!</b> 🚀\n\n"
            "Welcome to the Inner Circle. Use commands below to generate signals:\n"
            "🔹 /signals - Get Live Signals (5s, 1m, 5m, etc.)\n"
            "🔹 /future - Get Future Signals List\n"
            "🔹 /pairs - View All Active Pairs"
        )
        await update.message.reply_text(success_text, parse_mode="HTML")
    else:
        await update.message.reply_text("❌ <b>Invalid License Key!</b>\nClick the WhatsApp button or join via Referral Link.", parse_mode="HTML")

def main():
    # Hosting par bot ko active rakhne ke liye chhota sa web server
    app_web = Flask('')
    
    @app_web.route('/')
    def home():
        return "Bot is Alive!"
        
    def run():
        app_web.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
        
    threading.Thread(target=run).start()

    # Telegram Bot Setup
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("key", verify_key))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
