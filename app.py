import logging
from queue import Queue
from threading import Thread
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, MessageHandler, Updater, CommandHandler, CallbackQueryHandler, InlineQueryHandler
import finder

TOKEN = '288492738:AAGOQMuftxYWspRqnWvcqfwUC8As_GTQrgA'

status="zero"
background="NO"
name="NO"
phone="NO"
desc="NO"

def start(bot, update):	

    update.message.reply_text('سلام {} عزیز! به ربات دیکشنری خوش آمدید. برای شروع کار /start را بزنید و برای هر معنای واژه کافیست واژه ی مورد نظر را در یک پیام بفرستید'.format(update.message.from_user.first_name))


def example_handler(bot, update):

    nametext = update.message.text
    name=nametext
    bot.send_message(
        update.message.chat_id,
            text=finder.find(nametext)
            )  


# Write your handlers here


def setup(webhook_url=None):
    """If webhook_url is not passed, run with long-polling."""
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:
        updater = Updater(TOKEN)
        bot = updater.bot
        dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler([], example_handler))
 


    if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:
        bot.set_webhook()  # Delete webhook
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    setup()
