from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)

gender_m = KeyboardButton("Мужчина")
gender_f = KeyboardButton("Женщина")
gender_u = KeyboardButton("Незнаю")

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(gender_m, gender_f, gender_u, cancel_button)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))