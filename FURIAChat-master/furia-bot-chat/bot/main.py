import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
from . import messages


load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", messages.start))
    app.add_handler(CommandHandler("ajuda", messages.ajuda))
    app.add_handler(CommandHandler("noticias", messages.noticias))
    app.add_handler(CommandHandler("elenco", messages.elenco))

    print("🤖 Bot da FURIA rodando! Aguardando comandos...")
    app.run_polling()