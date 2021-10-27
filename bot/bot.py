from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json

token = '20745c8wCFFKY1WbeQrYs7ls'

def weather(update: Update, context: CallbackContext) -> None:
    url = 'https://api.weatherbit.io/v2.0/current?key=3715b60672f544ad&city=Tallinn&country=Estonia'
    result = requests.get(url)
    data = json.loads(result.text)
    update.message.reply_text("Temprature in Tallinn " + str(data['data'][0]['temp'])+"")


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('weather', weather))

updater.start_polling()
updater.idle()