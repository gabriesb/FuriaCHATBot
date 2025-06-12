from telegram.ext import CommandHandler
from . import messages

async def start(update, context):
    await update.message.reply_text(messages.start_msg)

async def grito(update, context):
    await update.message.reply_text(messages.grito_msg)

async def curiosidade(update, context):
    await update.message.reply_text(messages.curiosidade_msg)

async def elenco(update, context):
    await update.message.reply_text(messages.elenco_msg)

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("grito", grito))
    app.add_handler(CommandHandler("curiosidade", curiosidade))
    app.add_handler(CommandHandler("elenco", elenco))
