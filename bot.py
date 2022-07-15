import telebot
import time

bot = telebot.TeleBot('5325582360:AAHduY0Sw0SWrCEUhMNdqus4dOK-qFEm95k', parse_mode=None)
each_user_queries = dict()
info_commands = ["/lowprice", "/highprice", "/bestdeal"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    each_user_queries[str(message.text)] = time.ctime()
    if message.text.lower() == "/help":
        bot.send_message(message.from_user.id,
                         "Ниже приведен список команд бота:\n"
                         "/help — помощь по командам бота,\n"
                         "/lowprice — вывод самых дешёвых отелей в городе,\n"
                         "/highprice — вывод самых дорогих отелей в городе,\n"
                         "/bestdeal — вывод отелей, наиболее подходящих по цене и расположению от центра,\n"
                         "/history — вывод истории поиска отелей.\n\n"
                         "Выберете одну из команд списка, можете просто нажать на неё, "
                         "или впишите ее в текстовую строку, "
                         "или нажмите на одну из кнопок с командой.")
    elif message.text.lower() == "/history":
        bot.send_message(message.from_user.id, 'Ниже выведена история введенных Вами команд:')
        for i_user_query in each_user_queries.keys():
            bot.send_message(message.from_user.id, f'{i_user_query}, {each_user_queries[i_user_query]}')
    elif message.text.lower() in info_commands:
        bot.send_message(message.from_user.id, 'В каком городе хотели бы выбрать гостиницу/отель?')
    else:
        bot.send_message(message.from_user.id, "Эта часть кода пока не доработана... Извините.")


bot.polling(none_stop=True, interval=0)
