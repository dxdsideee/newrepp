# -*- coding: utf-8 -*-

import telebot
from telebot import types
import sqlite3
import keyboards as nav
from keyboards import *
import random
from pyqiwip2p import QiwiP2P
import requests

bot = telebot.TeleBot('5532266264:AAFCnvNY4TZZXqcH_4HZL-4Kf5dJii9vDQM')

PUBLIC_KEY = "48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP47hpr2x7anxY5aZABou2QQzyrpErdsASoktzPSBgg7hxWYKE9EVH5EjFDwNSXpW6b5hF2YfaEWKvoVWPumsSNfjG4L6dCtaQeiopnPYzt"
crystalpay = "9a6f675e03edc2ed882abe4a636f925982aea2f5"
kassaname = 'Uoldem'



src = 'secret.txt'
file = open(src, 'rb')
reading = file.read()
print(reading)


db = sqlite3.connect('base.db', check_same_thread=False)
sql = db.cursor()

name = 'Staff Cartel'

input_password = input('Введите пароль: ')
if input_password == '855429':
    try:
        print('Бот запущен')
        @bot.message_handler(commands=['start'])
        def start_command(message):
            img = open('photo/asd.jpg', 'rb')
            sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,))
            if sql.fetchone() == None:
                sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)', (message.from_user.id, 0, 0, 0, 0, 0, 'Начальная'))
                db.commit()
                keyboard = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton(text=f'Баланс(0 руб)', callback_data='balance')
                keyboard.row(btn1)
                keyboard2 = types.ReplyKeyboardMarkup()
                btn1_m = types.KeyboardButton(text='Локации')
                btn3_m = types.KeyboardButton(text='Профиль')
                btn4_m = types.KeyboardButton(text='Баланс')
                btn5_m = types.KeyboardButton(text=f'Отзывы')
                btn6_m = types.KeyboardButton(text='Поддержка')
                btn7_m = types.KeyboardButton(text='Заработать')
                btn8_m = types.KeyboardButton(text='Работа от 1000Р ')
                btn9_m = types.KeyboardButton(text='Рефералка')
                btn10_m = types.KeyboardButton(text='Розыгрыш')
                keyboard2.row(btn1_m, btn3_m)
                keyboard2.row(btn4_m, btn5_m, btn6_m)
                keyboard2.row(btn7_m, btn8_m, btn9_m)
                keyboard2.row(btn10_m)
                bot.send_photo(message.from_user.id, 'photo/asd.jpg')
                bot.send_message(message.from_user.id, f'Добро пожаловать в {name}!\n Вы можете пополнить баланс нажав на кнопку "Баланс"!', reply_markup=keyboard)
                bot.send_message(message.from_user.id, f'Удачных покупок!', reply_markup=keyboard2)
            else:
                keyboard = types.InlineKeyboardMarkup()
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[1]
                btn1 = types.InlineKeyboardButton(text=f'Баланс({balance} руб)', callback_data='balance')
                keyboard.row(btn1)
                keyboard2 = types.ReplyKeyboardMarkup()
                btn1_m = types.KeyboardButton(text='Локации')
                btn3_m = types.KeyboardButton(text='Профиль')
                btn4_m = types.KeyboardButton(text='Баланс')
                btn5_m = types.KeyboardButton(text=f'Отзывы')
                btn6_m = types.KeyboardButton(text='Поддержка')
                btn7_m = types.KeyboardButton(text='Заработать')
                btn8_m = types.KeyboardButton(text='Работа от 1000Р ')
                btn9_m = types.KeyboardButton(text='Рефералка')
                btn10_m = types.KeyboardButton(text='Розыгрыш')
                keyboard2.row(btn1_m, btn3_m)
                keyboard2.row(btn4_m, btn5_m, btn6_m)
                keyboard2.row(btn7_m, btn8_m, btn9_m)
                keyboard2.row(btn10_m)
                bot.send_photo(message.from_user.id, img)
                bot.send_message(message.from_user.id, f'Добро пожаловать в {name}!\n Вы можете пополнить баланс нажав на кнопку "Баланс"!', reply_markup=keyboard)
                bot.send_message(message.from_user.id, f'Удачных покупок!', reply_markup=keyboard2)


        def input_summa(message):
            bot.send_message(message.from_user.id, f'Скоро...')

        asgasgkawmkgmawkmawkmawkgmakgwmkwmawkmg = 855429
        global awmkgawgnawgnawjgwangw
        awmkgawgnawgnawjgwangw = asgasgkawmkgmawkmawkmawkgmakgwmkwmawkmg

        @bot.callback_query_handler(func = lambda call: True)
        def call_handler(call):
            if call.data == 'balance':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                keyboard = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton(text='Отменить', callback_data='cancel')
                asd = bot.send_message(call.from_user.id, f'*Пополнение балансa*\n\nВаш баланс: {balance} руб\n\nВведите на сколько вы хотите пополнить баланс (в руб)', parse_mode='Markdown', reply_markup=keyboard)
                bot.register_next_step_handler(asd, input_summa)

            tovar_zero = ['perm', 'samara', 'voronej', 'krasnoyarsk', 'saratov', 'omsk', 'novgorod', 'vladimir', 'vologda', 'tver', 'ryazan', 'volgograd', 'kostroma']

            if call.data == 'moscow':
                bot.send_message(call.from_user.id, f'Выберите товар:', reply_markup=nav.perm)

            #if call.data == 'perm' or 'samara' or 'voronej' or 'krasnoyarsk' or 'saratov' or 'omsk' or 'novgorod' or 'vladimir' or 'vologda' or 'tver' or 'ryazan' or 'volgograd' or 'kostroma':
                #bot.send_message(call.from_user.id, f'К сожалению в этой локации нет товара.')



            if call.data == 'perm':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)


            if call.data == 'samara':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'voronej':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'krasnoyarsk':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'saratov':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'omsk':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'novgorod':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'vladimir':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'vologda':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'tver':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'ryazan':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'volgograd':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'kostroma':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'chelyaba':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'rostov':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'yaroslavl':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'ekb':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'spb':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'novosib':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'tula':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'krasnodarskiy':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'ivanovo':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'krasnodar':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message_id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'voljskiy':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'krasnoturinsk':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'orenburg':
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text='Выберите товар:', reply_markup=nav.perm)

            if call.data == 'deposit':
                bot.send_message(call.from_user.id, f'В наличии: ', reply_markup=nav.deposit)

            if call.data == 'amf':
                bot.send_message(call.from_user.id, f'В наличии:', reply_markup=nav.amf)

            if call.data == 'mef_cristall':
                bot.send_message(call.from_user.id, f'В наличии:', reply_markup=nav.mefcristall)

            if call.data == 'mef_myka':
                bot.send_message(call.from_user.id, f'В наличии: ', reply_markup=nav.mefmyka)

            if call.data == 'alfapvp':
                bot.send_message(call.from_user.id, f'В наличии: ', reply_markup=nav.alfapvp)

            if call.data == 'boshki':
                bot.send_message(call.from_user.id, f'В наличии:', reply_markup=nav.boshki)

            if call.data == 'gashish':
                bot.send_message(call.from_user.id, f'В наличи:', reply_markup=nav.gashish)

            if call.data == 'podrobnee_referal':
                bot.send_message(call.from_user.id, f'Кол-во ваших рефералов: *0*\nПокупки рефералов: *0*\nСумма покупок рефералов:*0 руб*\nВаш заработок: *0 руб*', parse_mode="Markdown")

            if call.data == 'report':
                asd = bot.send_message(call.from_user.id, f'Введите текст обращения')
                bot.register_next_step_handler(asd, report_input)

            if call.data == 'gashish_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 1600:
                    new_balance = int(balance) - int(1600)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'gashish_2':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 3200:
                    new_balance = int(balance) - int(3200)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'deposit_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 1000:
                    new_balance = int(balance) - int(1000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'deposit_2':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 2000:
                    new_balance = int(balance) - int(2000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')
            if call.data == 'deposit_3':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 3000:
                    new_balance = int(balance) - int(3000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'deposit_5':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 5000:
                    new_balance = int(balance) - int(5000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'amf_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 1700:
                    new_balance = int(balance) - int(1700)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'amf_2':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 2450:
                    new_balance = int(balance) - int(2450)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'mef_cristall_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 2300:
                    new_balance = int(balance) - int(2300)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'mef_cristall_2':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 4600:
                    new_balance = int(balance) - int(4600)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'mef_cristall_3':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 6900:
                    new_balance = int(balance) - int(6900)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'mef_cristall_5':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 11500:
                    new_balance = int(balance) - int(11500)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'amf_myka_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 2000:
                    new_balance = int(balance) - int(4000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'amf_myka_3':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 6000:
                    new_balance = int(balance) - int(6000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'amf_myka_5':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 10000:
                    new_balance = int(balance) - int(10000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'alfapvp_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 1000:
                    new_balance = int(balance) - int(1000)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if 'ot' in call.data:
                ot_id = call.data.split('_')
                name = sql.execute('SELECT * FROM ot WHERE id = ?', (ot_id[1],)).fetchone()[1]
                text = sql.execute('SELECT * FROM ot WHERE id = ?', (ot_id[1],)).fetchone()[2]
                amount = sql.execute('SELECT * FROM ot WHERE id = ?', (ot_id[1],)).fetchone()[3]
                bot.send_message(call.from_user.id, f'Отзыв\n<b>Пользователь:</b> {name}\n<b>Текст:</b> {text}\n<b>Оценка:</b> {amount}', parse_mode='HTML')

            if call.data == 'boshki_1':
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (call.from_user.id,)).fetchone()[1]
                if balance >= 1800:
                    new_balance = int(balance) - int(1800)
                    sql.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {call.from_user.id}')
                    db.commit()
                    bot.send_message(call.from_user.id, f'Вы сделали покупку.\nСкоро с вами свяжется оператор, для уточнения места')
                else:
                    bot.send_message(call.from_user.id, f'Пополните баланс аккаунта.')

            if call.data == 'page_2_ot':
                sql.execute('SELECT * FROM ot OFFSET 10')
                data = sql.fetchall()
                bot.edit_message_text(chat_id=call.message.from_user.id, message_id=call.message_id - 1, text='2 страница', reply_markup=nav.markup2)


        def report_input(message):
            bot.send_message(1112411513, f'Обращение\nID: *{message.from_user.id}*\nTEXT: *{message.text}*')
            bot.send_message(message.from_user.id, f'Вы отправили обращение к администрации.')

        def is_number(_str):
            try:
                int(_str)
                return True
            except ValueError:
                return False


        def crystal_input(message):
            try:
                if is_number(message.text):
                    price = int(message.text)
                    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999))
                    bill = requests.get(
                        url=f'https://api.crystalpay.ru/v1/?s={crystalpay}&n={kassaname}&o=invoice-create&amount={price}&lifetime=60&extra={comment}').json()
                    bill_id = bill['id']
                    bill_url = bill['url']
                    sql.execute('INSERT INTO bills VALUES (?, ?, ?, ?, ?)', (message.from_user.id, bill_id, price, comment, 0))
                    db.commit()
                    keyboard = types.InlineKeyboardMarkup()
                    btn = types.InlineKeyboardButton(text='Оплатить', url=bill_url)
                    keyboard.row(btn)
                    bot.send_message(message.from_user.id,
                                     f'Счет на оплату создан!\n\n<b>Сумма</b>: {price} руб.\n<b>Комментарий</b>: {comment}',
                                     parse_mode='HTML', reply_markup=keyboard)
                    while True:
                        if requests.get(
                                url=f'https://api.crystalpay.ru/v1/?s={crystalpay}]&n={kassaname}&o=invoice-check&i={bill_id}').json()['state'] == 'payed':
                            bot.send_message(message.from_user.id, f'Новое пополнение на {price} руб.')
                            sql.execute(f'UPDATE bills SET status = {1} WHERE bill_id = "{bill_id}"')
                            db.commit()
                            balance = \
                            sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[1]
                            sql.execute(
                                f'UPDATE users SET balance = {int(balance) + int(price)} WHERE user_id = {message.from_user.id}')
                            db.commit()

                else:
                    bot.send_message(message.from_user.id, f'Введите целое число!')

            except Exception as er:
                print(er)


        def ot_input(message):
            global namesd
            namesd = message.text
            sql.execute('INSERT INTO ot VALUES (NULL, ?, ?, ?, ?)', (f'{message.text}', 'None', random.randint(4, 5), f'14.06.2022'))
            db.commit()
            asd = bot.send_message(message.from_user.id, f'Введите текст: ')
            bot.register_next_step_handler(asd, ot_text_input)

        def ot_text_input(message):
            sql.execute(f'UPDATE ot SET text = "{message.text}" WHERE name = "{namesd}"')
            db.commit()
            asd = bot.send_message(message.from_user.id, f'Введите оценку')
            bot.register_next_step_handler(asd, ot_amount)

        def ot_amount(message):
            sql.execute(f'UPDATE ot SET amount = {message.text} WHERE name = "{namesd}"')
            db.commit()
            bot.send_message(message.from_user.id, f'Отзыв создан')

        @bot.message_handler(content_types=['text'])
        def txt_message(message):
            if message.text == 'Локации':
                bot.send_message(message.from_user.id, f'Выберите локацию', reply_markup=nav.location)

            if message.text == 'Рефералка':
                bot.send_message(message.from_user.id, f'1. Приглашайте покупателей и получайте 5% с каждой сделки на свой баланс. Вывести деньги можно в любой момент, либо в криптовалюте, либо на банковскую карту. Так же на них можно преобрести у нас товар.\n\nЧтобы приступить, нажмите кнопку "Заработать" в боте. Вы получите ссылку, перейдя по которой, человек становится вашем рефералом.\n\n2. Если у вас есть знакомые, которые работают (или хотели бы поработать) курьерами, то приглашайте их к нам и получите 25к + 10% с каждого клада.\n\nЧтобы привести курьера, пишите в поддержку.')

            if message.text == 'Поддержка':
                keyboard = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton(text='Обратиться к администрации', callback_data='report')
                keyboard.row(btn1)
                bot.send_message(message.from_user.id, f'- Выберите пункт на клавиатуре.', reply_markup=keyboard)

            if message.text == 'ot':
                asd = bot.send_message(message.from_user.id, f'Имя:')
                bot.register_next_step_handler(asd, ot_input)

            if message.text == 'Работа от 1000Р':
                bot.send_message(message.from_user.id, f'В нашу команду срочно требуются курьеры во всех городах РФ!\n\nОплата:\n1г - 1000₽,\n2г - 1050₽,\n3г - 1100₽,\n5г - 1200₽\n\n- Выплаты производятся в любое время, по запросу. Получать деньги можно в криптовалюте, либо сразу на банковскую карту;\n- Для сотрудников действует высокая скидка на ассортимент магазина;\n- Все мастер-клады расфасованы и укомплектованы, расположены в черте города, в безопасных и удобных локациях;\n- Для людей без опыта, а также для желающих повысить кфалификацию, имеются авторские мануалы по качественной работе;\n- Кураторы всегда на связи и никогда не оставят один на один с любого рода трудностями;\n- Предусмотрен быстрый карьерный рост до склада, химика, а также онлайн-должностей;\n\nПо всем вопросам, пишите в поддержку')

            if 'Отзывы' in message.text:
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Отзывы", url='https://t.me/+jWBP--Va5vs5YWIy')
                markup.add(button1)
                data = 'https://t.me/+jWBP--Va5vs5YWIy'
                bot.send_message(message.from_user.id, text='Канал с отзывами', reply_markup=markup)

            if message.text == '#lottery':
                bot.send_message(message.from_user.id, f'Вы уже приняли участие в лоттереи.')

            if message.text == 'Розыгрыш':
                bot.send_message(message.from_user.id, f'Ежедневно, в течение месяца, мы будем разыгрывать 15 тысяч рублей среди своих постоянных покупателей! \nПризы:\n1 место - 5000₽\n\n2 место - 4000₽\n\n3 место - 3000₽\n\n4 место - 2000₽\n\n5 место - 1000₽\n\n\nУсловия розыгрыша:\n\n1. Одна покупка - один билетик. То есть, совершив в течение дня несколько покупок, Вы получаете несколько билетиков, тем самым увеличивая свои шансы на выигрыш.\n\n2. В 00:00 часов каждого дня происходит подведение итогов. Все неиспользованные билетики аннулируются. Призовые билетики выбираются случайным образом из всех участвующих.\n\n3.  Выигрыш зачисляется на баланс победителя, после чего его можно вывести, либо потратить на покупки.\n\nДля участия в розыгрыше, пишите #lottery')

            if message.text == 'Профиль':
                img = open('photo/asd.jpg', 'rb')
                balance = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[1]
                offerets = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[2]
                summa_offerets = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[3]
                mid_check = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[4]
                skidka = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[5]
                group = sql.execute('SELECT * FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()[6]
                bot.send_photo(message.from_user.id, img)
                bot.send_message(message.from_user.id, f'*Профиль*\n\n*Ваш ID*: {message.from_user.id}\n*Ваш баланс*: {balance}\n*Заказов*: {offerets}\n*На сумму:* {summa_offerets}\n*Средний чек*: {mid_check}\n*Ваша скидка*: {skidka}%\n\nВаша группа покупателя: *{group}*', parse_mode="Markdown") #reply_markup=nav.menu

            if message.text == 'Заработать':
                sql.execute('SELECT * FROM referal WHERE user_id = ?', (message.from_user.id,))
                if sql.fetchone() == None:
                    for n in range(1):
                        password =''
                        for i in range(7):
                            chars = 'QAWSEDRFTGYHUJIKOLPZXCVBNM'
                            password += random.choice(chars)
                    sql.execute('INSERT INTO referal VALUES (?, ?)', (message.from_user.id, f'{password}'))
                    db.commit()
                    bot.send_message(message.from_user.id, f'Ваш код реферала: *{password}*\nРаспостроняйте ваш реферальный код. Когда получатель зарегестрируется с вашим кодом, он получит награду. Если он сделает покупку, вы получите вознаграждение.', parse_mode='Markdown')
                    keyboard = types.InlineKeyboardMarkup()
                    btn1 = types.InlineKeyboardButton(text='Подробнее', callback_data='podrobnee_referal')
                    keyboard.row(btn1)
                    bot.send_message(message.from_user.id, f'Вы можете заработать приглашая покупателей.\n\nС каждой покупки приглашенного вами покупателя, вам полагается награда в размере 0.5% от суммы его покупки.', reply_markup=keyboard)
                else:
                    password = sql.execute('SELECT * FROM referal WHERE user_id = ?', (message.from_user.id,)).fetchone()[1]
                    bot.send_message(message.from_user.id, f'Ваш код реферала: *{password}*\nРаспостроняйте ваш реферальный код. Когда получатель зарегестрируется с вашим кодом, он получит награду. Если он сделает покупку, вы получите вознаграждение.', parse_mode='Markdown')
                    keyboard = types.InlineKeyboardMarkup()
                    btn1 = types.InlineKeyboardButton(text='Подробнее', callback_data='podrobnee_referal')
                    keyboard.row(btn1)
                    bot.send_message(message.from_user.id, f'Вы можете заработать приглашая покупателей.\n\nС каждой покупки приглашенного вами покупателя, вам полагается награда в размере 0.5% от суммы его покупки.', reply_markup=keyboard)

            if message.text == 'Баланс':
                asd = bot.send_message(message.from_user.id, f'Введите сумму для пополнения баланс')
                bot.register_next_step_handler(asd, crystal_input)








    except Exception as er:
        print(er)

else:
    print('Пароль неверный!')


bot.polling(none_stop=True)

