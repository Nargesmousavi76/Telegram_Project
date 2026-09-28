import telebot
import base1
import bot_api

bot = telebot.TeleBot(base1.TOKEN)

print("bot created...")

###############################################################

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, text='Welcome to Movie Bot')


    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)

    btn1 = telebot.types.KeyboardButton(text="Search")
    btn2 = telebot.types.KeyboardButton(text="Random")
    btn3 = telebot.types.KeyboardButton(text="Help")

    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id, text='Choose an option:',
                     reply_markup=markup)

###############################################################

def show_movie_info_name(message):

    movie_name = message.text

    results = bot_api.get_movie_info_by_name(movie_name)

    if results == 'ERROR':

        bot.send_message(
            message.chat.id,
            text='Error getting movie info.'
        )

    elif len(results) == 0:

        bot.send_message(
            message.chat.id,
            text='No movies found.'
        )

    else:

        markup = telebot.types.InlineKeyboardMarkup(row_width=1)

        for movie in results:

            movie_id = movie['id']
            movie_title = movie['title']

            btn = telebot.types.InlineKeyboardButton(
                text=movie_title,
                callback_data=str(movie_id)
            )

            markup.add(btn)

        bot.send_message(
            message.chat.id,
            text='Choose a movie:',
            reply_markup=markup
        )

# def show_movie_info_name(message):
#     movie_name = message.text

#     results = bot_api.get_movie_info_by_name(movie_name)

#     if results == 'ERROR':
#         bot.send_message(message.chat.id,
#                           text='Error getting movie info.')

#     elif len(results) == 0:
#         bot.send_message( message.chat.id,
#                         text='No movies found.' )
        
#     else:    
#         markup = telebot.types.InlineKeyboardMarkup(row_width=1)

#         for movie in results:
#             movie_id = movie['id'] 
#             movie_title = movie['title']

#             print("Movie:", movie_title) 
#             print("ID:", movie_id)

#             btn = telebot.types.InlineKeyboardButton(text=movie_title,
#                                             callback_data=str(movie_id))
#             markup.add(btn)

#         print("BUTTON COUNT:", len(markup.keyboard))

#         bot.send_message(message.chat.id, text='Choose a movie:',
#                         reply_markup=markup)
            
###############################################################
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    movie_id = call.data

    result = bot_api.get_movie_info_by_id(movie_id)

    if result == "ERROR":
        bot.send_message(call.message.chat.id,
                        text='Error getting movie info.')

    else:
        genres = ",".join(result[5])
        text = f''' Title: {result[0]}
        Country: {result[1]}
        Director: {result[2]}
        Year: {result[3]} 
        IMDb: {result[4]} 
        Genre: {genres} '''

        bot.send_message( call.message.chat.id, text=text ) 
        if result[6]:
            bot.send_photo( call.message.chat.id, photo=result[6] )
    

###############################################################

@bot.message_handler(func=lambda message:True)
def handle_other_message(message):

    if message.text == "Search" :
        msg = bot.send_message(message.chat.id,
                            text='Enter movie name:')
        bot.register_next_step_handler(msg, show_movie_info_name)
            

    elif message.text == "Random" :
        result = bot_api.get_random_movie()

        if result == 'ERROR':

            bot.send_message(message.chat.id,
                            text='Error getting movie.')
        else:
            genres = ", ".join(result[5]) 
            text = f''' 
            Title: {result[0]} 
            Country: {result[1]} 
            Director: {result[2]} 
            Year: {result[3]} 
            IMDb: {result[4]} 
            Genre: {genres} '''

            bot.send_message( message.chat.id, text=text ) 
            if result[6]: 
                bot.send_photo( message.chat.id, photo=result[6] )



    elif message.text == "Help" :
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                        text='Use "Search" to find a movie.',
                          reply_markup=markup)

    else:
            bot.send_message(message.chat.id,
                            text="I don't understand.")
    


if __name__ == '__main__':
    bot.infinity_polling()


