import sqlite3

conn = sqlite3.connect('database.sqlite', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''create table if not exists users
(
	telegram_id integer,
	telegram_username string,
	language string,
	last_usage string,
	latitude string,
	longitude string
)''')


cursor.execute('''create table if not exists zodiacs
(
    name string,
    description string,
    language string
)''')


def update_location(telegram_id, lat, long):
    cursor.execute('''update users set latitude = ?, longitude = ? where telegram_id = ?''', (lat,long,telegram_id,))
    conn.commit()


def update_last_usage(telegram_id, date):
    cursor.execute('''update users set last_usage = ? where telegram_id = ?''', (date,telegram_id,))
    conn.commit()


def update_lang(telegram_id, lang):
    cursor.execute('''update users set language = ? where telegram_id = ?''', (lang,telegram_id,))
    conn.commit()


def get_user(telegram_id):
    cursor.execute('''select * from users where telegram_id = ?''', (telegram_id,))
    return cursor.fetchone()


def get_user_language(telegram_id):
    cursor.execute('''select language from users where telegram_id = ?''', (telegram_id,))
    lang = cursor.fetchone()
    if lang is None:
        return None
    return lang[0]


def insert_user(telegram_id, telegram_name):
    cursor.execute('''insert into users(telegram_id, telegram_username) values(?, ?)''', (telegram_id,telegram_name,))
    conn.commit()


def get_zodiac_description(zodiac):
    cursor.execute('''select description from zodiacs where name = ?''', (zodiac,))
    descr = cursor.fetchone()
    if descr is None:
        return None
    return descr[0]

def get_zodiac_names(lang):
    cursor.execute('''select name from zodiacs where language = ?''', (lang,))
    zodiacs = cursor.fetchall()

    names = []
    for zod in zodiacs:
        names.append(zod[0])

    return names
