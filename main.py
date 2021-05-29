from telegram import Update
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, CallbackContext
import menu
import database
import constants
from datetime import datetime


def start_handler(update: Update, _: CallbackContext) -> None:
    user = database.get_user(update.effective_user.id)
    if user is None:
        database.insert(update.effective_user.id, update.effective_user.name)

    lang_buttons = menu.languages()

    update.message.reply_text(
        fr'Привет {update.effective_user.name}! Выбери язык',
        reply_markup=lang_buttons
    )


def lang_handler(update: Update, _: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == 'lang_ru':
        database.update_lang(update.effective_user.id, 'ru')
        markup = menu.zodiac_signs('ru')
        query.message.reply_markdown_v2(text='Знаки зодиака', reply_markup=markup)
    elif query.data == 'lang_en':
        database.update_lang(update.effective_user.id, 'en')
        markup = menu.zodiac_signs('en')
        query.message.reply_markdown_v2(text='Zodiac signs', reply_markup=markup)


def text_handler(update: Update, _: CallbackContext) -> None:
    database.update_last_usage(update.effective_user.id, datetime.now())

    if update.message.text == 'Сменить язык':
        lang_buttons = menu.languages()
        update.message.reply_text(
            'Выбери язык',
            reply_markup=lang_buttons
        )
    elif update.message.text == 'Change language':
        lang_buttons = menu.languages()
        update.message.reply_text(
            'Choose language',
            reply_markup=lang_buttons
        )
    else:
        selected_zodiac = update.message.text
        user = database.get_user(update.effective_user.id)
        lang = user[2]
        for zodiac in constants.ZODIAC:
            if zodiac[lang]['name'] == selected_zodiac:
                update.message.reply_text(text=zodiac[lang]['descr'])
                return

        update.message.reply_text(text=constants.UNKNOWN_COMMAND[lang])



def main() -> None:
    updater = Updater(constants.API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))

    dispatcher.add_handler((CallbackQueryHandler(callback=lang_handler, pattern='lang_*')))

    dispatcher.add_handler(MessageHandler(Filters.text, text_handler))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
