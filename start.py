import telebot
from telebot import types

TO_CHAT_ID = -1001502742121
bot = telebot.TeleBot('5606673802:AAFthndb5-degs1rFsTCUgSjbHbVKz50HA4')
photo_list = []
chat_id = None
send_photo_or_not = None
wait_photo = None
first_input = None


@bot.message_handler(commands=['start'])
def start(message):
    global send_photo_or_not, wait_photo
    if wait_photo:
        bot.send_message(message.chat.id, text="Отправьте пожалуйста фото!")
    else:
        if send_photo_or_not is None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Принять участие 📸")
            markup.add(btn1)
            bot.send_message(message.chat.id,
                             text="Хей, студент!👩🏼‍🎓 Готов участвовать в розыгрыше призов?",reply_markup=markup)
        else:
            bot.send_message(message.chat.id, text="Ждите результов конкурса!!")


@bot.message_handler(content_types=['text'])
def func(message):
    global send_photo_or_not, wait_photo
    if wait_photo:
        bot.send_message(message.chat.id, text="Отправьте пожалуйста фото!")
    else:
        if send_photo_or_not is None:
            if message.text == "Принять участие 📸":
                send = bot.send_message(message.chat.id,"Круто! Тогда объявляем сезон фотоохоты открытым! 📸",
                                        reply_markup=types.ReplyKeyboardRemove(),
                                        parse_mode='Markdown')
                bot.send_message(message.chat.id, "Чтобы участвовать в розыгрыше, тебе нужно выполнить несколько заданий.",
                                         reply_markup=types.ReplyKeyboardRemove(),
                                         parse_mode='Markdown'
                                         )
                bot.send_message(message.chat.id, "✅ А вот и первое задание. Сделай селфи с участником команды STUDBIT. "
                                                          "Ты найдешь их по чёрным футболкам с надписью STUDBIT.",
                                         reply_markup=types.ReplyKeyboardRemove(),
                                         parse_mode='Markdown'
                                         )
                bot.send_photo(message.chat.id, open('first.jpg', 'rb'))
                wait_photo = True
                bot.register_next_step_handler(send, photo_id)
            else:
                bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")
        else:
            bot.send_message(message.chat.id, text="Ждите результов конкурса!!")


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    global chat_id, send_photo_or_not, wait_photo
    if message.photo is None:
        bot.send_message(message.chat.id, text="Отправьте пожалуйста фото!")
    else:
        wait_photo = None
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup4.add()
        if message.photo[-1].file_id not in photo_list:
            photo_list.append(message.photo[-1].file_id)
            if len(photo_list) == 1:
                bot.send_message(TO_CHAT_ID, "{0.first_name} {0.last_name}".format(message.from_user))
                bot.send_message(message.from_user.id, "Хей-хей-хей. Кто эти красавчики? Клёвое селфи! Идём дальше? 😏",
                                 reply_markup=markup4)
                bot.send_message(message.from_user.id, "Следующее задание!"
                                                       "\nТебе нужно найти на территории рядом с университетом надпись "
                                                       "«Я люблю БашГУ» и сделать с ним ОРИГИНАЛЬНОЕ фото. 🔥",
                                 reply_markup=markup4)
                bot.send_photo(message.chat.id, open('second.jpg', 'rb'))
                fileID = message.photo[-1].file_id
                file_info = bot.get_file(fileID)
                bot.download_file(file_info.file_path)
                bot.send_photo(TO_CHAT_ID, message.photo[0].file_id)
                chat_id = message.chat.id
                send_photo_or_not = True
                return
            if len(photo_list)==2:
                bot.send_message(TO_CHAT_ID, "{0.first_name} {0.last_name}".format(message.from_user))
                bot.send_message(message.from_user.id, "Потрясающе!😍 Фотографы STUDBIT одобряют. "
                                                       "Тебе ещё одно задание. Наш куратор фотографов очень любит пародии. "
                                                       "Изобрази с друзьями эту картинку и пришли нам фото. 😂",
                                 reply_markup=markup4)
                bot.send_photo(message.chat.id, open('third.jpg', 'rb'))
                fileID = message.photo[-1].file_id
                file_info = bot.get_file(fileID)
                bot.download_file(file_info.file_path)
                bot.send_photo(TO_CHAT_ID, message.photo[0].file_id)
                chat_id = message.chat.id
                send_photo_or_not = True
                return
            if len(photo_list)==3:
                bot.send_message(TO_CHAT_ID, "{0.first_name} {0.last_name}".format(message.from_user))
                bot.send_message(message.from_user.id, "Супер! Мы в восторге! Давай соберёмся с силами. "
                                                       "Чуть-чуть осталось! 😉"
                                                       "Сфоткайся на любом интерактиве, который тебе понравился.",
                                 reply_markup=markup4)
                bot.send_photo(message.chat.id, open('fourth.jpg', 'rb'))
                fileID = message.photo[-1].file_id
                file_info = bot.get_file(fileID)
                bot.download_file(file_info.file_path)
                bot.send_photo(TO_CHAT_ID, message.photo[0].file_id)
                chat_id = message.chat.id
                send_photo_or_not = True
                return
            if len(photo_list)==4:
                bot.send_message(TO_CHAT_ID, "{0.first_name} {0.last_name}".format(message.from_user))
                bot.send_message(message.from_user.id, "Теперь мы видим, тебе было весело. "
                                                       "А вот и последнее задание.😱"
                                                       "Отправь самое удачное фото за этот день.",
                                 reply_markup=markup4)
                bot.send_photo(message.chat.id, open('final.jpg', 'rb'))
                fileID = message.photo[-1].file_id
                file_info = bot.get_file(fileID)
                bot.download_file(file_info.file_path)
                bot.send_photo(TO_CHAT_ID, message.photo[0].file_id)
                chat_id = message.chat.id
                send_photo_or_not = True
                return
            if len(photo_list)==5:
                bot.send_message(TO_CHAT_ID, "{0.first_name} {0.last_name}".format(message.from_user))
                bot.send_message(message.from_user.id, "Вааау! Да ты самый настоящий профи.😎Отличное фото.",
                                 reply_markup=markup4)
                bot.send_message(message.from_user.id, "📸 Фотоохота удалась! Жди результатов розыгрыша. "
                                                       "В конце дня мы объявим победителя. "
                                                       "Им станет человек, приславший лучшие фото.🔥",
                                 reply_markup=markup4)
                bot.send_message(message.from_user.id, "А если, выполняя эти задания ты понял, "
                                                       "что фотография - твоё призвание, то приходи к нам в команду. "
                                                       "Следи за новостями в нашей группе. "
                                                       "Скоро мы сделаем объявление о новом наборе в команду медиацентра.❤",
                                 reply_markup=markup4)
                fileID = message.photo[-1].file_id
                file_info = bot.get_file(fileID)
                bot.download_file(file_info.file_path)
                bot.send_photo(TO_CHAT_ID, message.photo[0].file_id)
                chat_id = message.chat.id
                send_photo_or_not = True
                return

            if len(photo_list) > 5:
                bot.send_message(message.chat.id, text="{0.first_name}, ты уже отправил фото! Больше нельзя :(".format(
                    message.from_user))


while True:
    try:
        bot.polling()
    except Exception:
        bot.send_message(chat_id, text="Больше фото загружать нельзя, жди результатов!")


