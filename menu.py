from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import constants


def languages():
    keyboard = [
        [
            InlineKeyboardButton("Русский", callback_data='lang_ru'),
            InlineKeyboardButton("English", callback_data='lang_en'),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def zodiac_signs(lang):
    buttons = []
    group = []
    i = 0
    while i < len(constants.ZODIAC):
        if i % 4 == 0:
            buttons.append(group)
            group = []
        group.append(KeyboardButton(constants.ZODIAC[i][lang]['name']))
        i += 1

    buttons.append(group)
    buttons.append([KeyboardButton(constants.CHANGE_LANG[lang])])

    return ReplyKeyboardMarkup(buttons)



