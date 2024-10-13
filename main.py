import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from serv_func import *
from data import *
from request import get_weather

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    updater = Updater('8178715505:AAFNrAev-jktNbq-LC9KG7oFTzlleyEYjKI', use_context=True)

    dp = updater.dispatcher
    # Основной хендлер

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            WEATHER: [MessageHandler(filters=Filters.text, callback=get_weather)],
        },
        fallbacks=[CommandHandler('end_game', callback=end_game)])
    dp.add_handler(CommandHandler("help", hep))
    dp.add_handler(conv_handler)
    '''
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN, webhook_url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
    '''
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()