from data import *


def start(update, context):
    update.message.reply_text("""В каком городе Вы хотите узнать погоду?""")
    return WEATHER

def hep(update, context):
    update.message.reply_text("""Ведите название населенного пункта, где вы хотите узнать погоду.""")



from telegram.ext import ConversationHandler

def end_game(update, context):
    update.message.reply_text('Работа завершена. Узнать ещё погоду - /start')
    return ConversationHandler.END