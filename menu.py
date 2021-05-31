from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import constants
import database


def languages():
    keyboard = [
        [
            InlineKeyboardButton("Русский", callback_data='lang_ru'),
            InlineKeyboardButton("English", callback_data='lang_en'),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def zodiac_signs(lang):
    zodiac_names = database.get_zodiac_names(lang)

    buttons = []
    group = []
    i = 0

    while i < len(zodiac_names):
        if i % 4 == 0:
            buttons.append(group)
            group = []
        group.append(KeyboardButton(zodiac_names[i]))
        i += 1

    buttons.append(group)
    buttons.append([KeyboardButton(constants.CHANGE_LANG[lang])])
    buttons.append([KeyboardButton(constants.LOCATION[lang], request_location=True)])

    return ReplyKeyboardMarkup(buttons)



