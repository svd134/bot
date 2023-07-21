import telebot
import config
bot = telebot.TeleBot(config.TOKEN)
#content_types=['text']
@bot.message_handler(content_types=['photo'])

def lalala(message):
    #bot.send_message(message.chat.id, 'hey')
    #bot.send_photo(message.chat.id, message.photo[0].file_id)
    #bot.send_photo(message.chat.id, message.photo[1].file_id)
    #bot.send_photo(message.chat.id, message.photo[2].file_id)
    bot.send_photo(message.chat.id, message.photo[3].file_id)
    bot.send_photo(message.chat.id, message.photo[3].file_id)
    bot.send_message(message.chat.id, "По всей видимости это")
    #bot.send_message(message.chat.id, str(message.photo[1]))
    #bot.send_message(message.chat.id, str(message.photo[2]))
    #bot.send_message(message.chat.id, str(message.photo[3]))

@bot.message_handler()

def lalala(message):
    #bot.send_message(message.chat.id, 'hey')
    #bot.send_photo(message.chat.id, message.photo[0].file_id)
    #bot.send_photo(message.chat.id, message.photo[1].file_id)
    #bot.send_photo(message.chat.id, message.photo[2].file_id)
    #x = 4
    #for i in range(40000000):
    #    x+=1
    check = message.from_user.is_bot
    if check:
        #bot.send_message(message.chat.id, "Попался, ёбаный бот!")
        bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, message.text)
    #if message.from_user.is_bot == False:
    #    s = str(bot.get_updates())
    #    bot.send_message(message.chat.id, s)
    #bot.send_message(message.chat.id, str(message.photo[1]))
    #bot.send_message(message.chat.id, str(message.photo[2]))
    #bot.send_message(message.chat.id, str(message.photo[3]))

#def al(message):
#    bot.send_Photo(message.chat.id, message.id)


# RUN
bot.polling(none_stop=True)
