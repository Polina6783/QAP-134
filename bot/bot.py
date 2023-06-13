import telebot
from config import user_keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username or message.chat.first_name or 'Друг'}!\n"
                                      f"Я - конвертер валют!\n"
                                      f"Я помогу тебе быстро сделать перевод из одной валюты в другую.\n"
                                      f"\n"
                                      f"Введи команду /values, чтобы узнать информацию обо всех доступных валютах, которые я могу конвертировать.\n"
                                      f"\n"
                                      f"Чтобы начать работу введи данные в следующем формате:\n <имя валюты, цену которой хочешь узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>\n"
                                      f"Например: Рубли доллары 50 или евро доллар 100"
                                      f"\n"
                                      f"\n"
                                      f"Введи команду /start или /help, чтобы повторно прочитать инструкцию.")

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in user_keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise ConvertionException('Некорректное количество параметров')

        quote, base, amount = values
        total = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {float(total) * float(amount)}'
        bot.reply_to(message, text)

bot.polling(none_stop=True)