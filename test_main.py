# основной - ******
# тестовый - ******

token = ''
test = ''
adminka = ""

import telebot, re
from telebot import types

import time
from time import sleep

import datetime

import random
from random import choice


from threading import Thread

# my ID - *******

# Создаем бота
bot = telebot.TeleBot(test)

# старт бота, на эту функцию  можно привязать оповещения
def main():
    print('! bot running !')

def alerts():
    print("alerts")

    file1 = open("balance.txt", "r")

    start = True

    while start:

        try:
            time.sleep(0.1)
            today = datetime.datetime.today()
            if today.strftime("%H:%M") == "20:00":
                line = file1.readline()
                print(line)
                if not line:
                    print("not line")
                    time.sleep(61)
                    start = False
                    file1.close()
                    alerts()

                user = line.split("##")
                user[2] = user[2].rstrip('\n')
                if int(user[2]) < 300:
                    print(user[2] + " malo")
                    userid = user[0]

                    bot.send_message(userid, 'Ваш баланс менее 300 рублей!')

        except:
            print("alerts is dead")
            start = False
            file1.close()
            alerts()
	
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Добро пожаловать!')
    add_main_menu(m)

@bot.message_handler(commands=['button'])
def add_main_menu(message):
    # Добавляем кнопки
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Баланс')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Что сделаем?', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(m):
    if m.text.strip() == 'Баланс':
        bot.send_message(m.chat.id, 'Ваш баланс равен:')

        file1 = open("balance.txt", "r")

        while True:

            line = file1.readline()

            if not line:
                break

            if str(line[:9]) == str(m.chat.id):
                print("yes")
                user = line.split("##")
                user_all = str(user[1] + " - " + user[2].rstrip("\n") + " рублей")
                bot.send_message(m.chat.id, user_all)
                print(user[1])
            

            elif str(line[:10]) == str(m.chat.id):
                user = line.split("##")
                user_all = str(user[1] + " - " + user[2].rstrip("\n") + " рублей")
                bot.send_message(m.chat.id, user_all)
                print(user[1])
                
            #elif str(line[:4]) == str("date"):
              #  date_file = line.split("##")
             #   date_file_message = ("Последняя дата изменения: " + date_file[1])
            #    bot.send_message(m.chat.id, date_file_message)
           #     print("date")

				
        
        file1.close()
    
        file_date = open('date.txt', 'r')
        date_read = file_date.read()
        bot.send_message(m.chat.id, "Последняя дата изменения: " + date_read)
        print("date")
        
    
    elif m.text.strip() == adminka:
        print("admin")
        def opened(m):
            file = open('balance.txt','r')
            all_file = file.read()
            bot.send_message(m.chat.id, all_file)
            bot.send_message(m.chat.id, "Пожалуйста, обновите данные")
            file.close()
            
            def deleter(m):
                with open("balance.txt", "w",encoding='utf-8') as f:
                    f.write(m.text.strip())
                bot.send_message(m.chat.id, "Спасибо, изменено")
                print("deleter")
                
                with open("date.txt", "w",encoding='utf-8') as f:
                    today = datetime.datetime.today()
                    f.write(today.strftime("%d.%m.%y"))
            
            bot.register_next_step_handler(m, deleter)
        
        opened(m)




# Запускаем бота
while True:

    try:
        Thread(target=main and alerts).start()
        bot.polling(none_stop=True, interval=1)
    except:
        print("polling is dead")
        time.sleep(0.3)
