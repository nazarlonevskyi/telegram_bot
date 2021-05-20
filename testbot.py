import telebot
import re
import requests
import baza
import conf as config
from conf import offensive_messages, love_messages
from datetime import datetime

bot = telebot.TeleBot(config.token)


# При введенні команди '/start' привітаємося з користувачем.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    if (baza.get_data(str(message.chat.id) + 'name')):
        bot.send_message(message.chat.id, f" Привіт, {baza.get_data(str(message.chat.id) + 'name')},"
                                          f"\nЯкщо ти не знаєш що далі, пиши /help!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUO9gphfpZQlB3jFnUPHwirSSQz-0JwACHwADnP4yMCBW8jz3ttrRHwQ')
    else:
        bot.send_message(message.chat.id, "   Привіт!"
                                          "\nЯ, бот, який любить собак🤫, класно правда?"
                                          "\nЯ можу багато чого, тож,"
                                          "\nЯк я можу до тебе звертатись? ")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUO9gphfpZQlB3jFnUPHwirSSQz-0JwACHwADnP4yMCBW8jz3ttrRHwQ')
        baza.set_data(message.chat.id, config.States.S_ENTER_NAME.value)


# При введенні команди '/set_name' змінимо ім'я користувача.
@bot.message_handler(commands=['set_name'])
def set_name(message):
    bot.send_message(message.chat.id, "Тож, як тебе звати?")
    baza.set_data(message.chat.id, config.States.S_ENTER_NAME.value)


# Записуємо ім'я користувача
@bot.message_handler(func=lambda message: baza.get_data(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    # В випадку з іменем не будемо нічого перевіряти
    bot.send_message(message.chat.id, "Чудове ім'я, запам'ятаю!")
    bot.send_message(message.chat.id, f"Що ж далі? Пиши: /help")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUPVgphgbJwqWZHpnNSbooLkUw-Uq0QACEgADnP4yMOA1S0Oue2vUHwQ')
    baza.set_data(str(message.chat.id) + 'name', message.text)
    baza.set_data(message.chat.id, config.States.S_START.value)


# При введенні команди '/help' виведемо команди для роботи з ботом.
@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Command list: '
                                      '\n/help, '
                                      '\n/start, '
                                      '\n/price'
                                      '\n/set_name, '
                                      '\n/random_dog'
                                      '\n/random_stats_dog')


# При введенні користувачем образливих слів саме до бота з масиву 'offensive_messages' з 'config'
# будемо відповідати до нього
@bot.message_handler(func=lambda message: message.text \
                                          and re.sub(r'\s+', ' ', message.text.lower()) \
                                          in map(lambda x: x, offensive_messages))
def offensive_message(message):
    words = re.sub(r'\s+', ' ', message.text.lower()).split()
    bot.reply_to(message, f"Сам {words[0]}")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUPtgphnA3-a9qSU6w7FqpUXVtx00cAACGwADnP4yMByL0TjtFNWIHwQ')


# При введенні користувачем приэмних слів саме до бота з масиву 'love_messages' з 'config'
# будемо відповідати до нього
@bot.message_handler(func=lambda message: message.text \
                                          and re.sub(r'\s+', ' ', message.text.lower()) \
                                          in map(lambda x: x, love_messages))
def love_message(message):
    words = re.sub(r'\s+', ' ', message.text.lower()).split()
    bot.send_message(message.chat.id, 'WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOW ')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUQpgphth27f3rL6LkuwQmdhF6CtDDAACGQADnP4yMGtnBiuSyxWjHwQ')


# При введенні команди '/random_dog' виведемо випадкове фото чи відео собаки.
@bot.message_handler(commands=['random_dog'])
def random_dog(message):
    try:
        r = requests.get(url=config.random_dog_api)
        response = r.json()
    except:
        bot.send_message(message.chat.id, 'Нажаль не вдалось отримати відповідь 😔')
        return

    extension = response["url"].split('.')[-1]
    # Якщо відео
    if ('mp4' in extension):
        bot.send_video(message.chat.id, response["url"])
    # gif
    elif ('gif' in extension):
        bot.send_video_note(message.chat.id, response["url"])
    # Фото
    else:
        bot.send_photo(message.chat.id, response["url"])


# При введенні команди '/random_stats_dog' виведемо випадкове фото чи відео собаки.
@bot.message_handler(commands=['random_stats_dog'])
def random_stats_dog_help(message):
    bot.send_message(message.chat.id, '🤗 Це моя основна можливість'
                                      '\n🤫 Я знаю все про собак'
                                      '\n❔ Хочеш перевірити? '
                                      '\n✔ Ти можеш сказати "name", і я тобі назву рандомне ім`я '
                                      '\n✔ Я скажу породу та вік собаки, його можливості,пиши"breed"'
                                      '\n✔ Темперамент і походження - пиши "temp"')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUPhgphiW3lLddusR1Qn2oRCodDHELQACEAADnP4yMIzJFdBdAnGcHwQ')

@bot.message_handler(commands=['price'])
def random_stats_dog_help(message):
    bot.send_message(message.chat.id, '🤗 Ти знав, що в честь собаки назвали криптовалюту?'
                                      '\n🤫 Я знаю про неї все'
                                      '\n❔ Хочеш перевірити? '
                                      '\n✔ Напиши "show me a doge crupto price" ')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBUVZgpnrGmreMkOzg1hSL37ot8hNZUgACIwADnP4yMGLSFbgqnabRHwQ')


@bot.message_handler(content_types=["text"])
def random_stats(message):
    if message.text.lower() == "show me a doge crupto price":
        req = requests.get("https://yobit.net/api/2/doge_usd/ticker")
        response = req.json()
        high_price = response["ticker"]["high"]
        sell_price = response["ticker"]["sell"]
        buy_price = response["ticker"]["buy"]
        bot.send_message( message.chat.id,f"⏺ Now: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
                                          f"\n\n\n⬆️ High DOGE price: {high_price,}"
                                          f"\n\n➡️ Sell DOGE price: {sell_price},"
                                          f"\n\n⬅️ Buy DOGE price: {buy_price}"
                         )

    if message.text.lower() == "name":
        response = requests.get(url=config.random_stats_api)
        response.headers.get("Content-Type")
        'application/json; charset=utf-8'
        category_name = response.json()['name']
        bot.send_message(message.chat.id,
                         f"Name: {category_name}"
                         )

    if message.text.lower() == "breed":
        req = requests.get(url=config.random_stats_api_1)
        req.headers.get("Content-Type")
        'application/json; charset=utf-8'
        breedgroup = req.json()["breed_group"]
        life = req.json()["life_span"]
        bred = req.json()['bred_for']
        bot.send_message(message.chat.id, f"Breed:  {breedgroup},"
                                          f"\nLife span:  {life},"
                                          f"\nBred for:  {bred}"
                         )

    if message.text.lower() == "temp":
        requ = requests.get(url=config.random_stats_api)
        requ.headers.get("Content-Type")
        'application/json; charset=utf-8'
        temperament = requ.json()['temperament']
        origin = requ.json()['origin']
        bot.send_message(message.chat.id, f"Temperament: {temperament}"
                                          f"\nOrigin: {origin}"
                         )

bot.polling()

if __name__ == '__testbot__':
    bot.polling()