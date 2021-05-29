import sqlite3

conn = sqlite3.connect('database.sqlite', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''create table if not exists users
(
	telegram_id integer,
	telegram_username string,
	language string
)''')


def update_lang(telegram_id, lang):
    cursor.execute('''update users set language = ? where telegram_id = ?''', (lang,telegram_id,))
    conn.commit()


def get_user(telegram_id):
    cursor.execute('''select * from users where telegram_id = ?''', (telegram_id,))
    return cursor.fetchone()


def insert(telegram_id, telegram_name):
    cursor.execute('''insert into users(telegram_id, telegram_username) values(?, ?)''', (telegram_id,telegram_name,))
    conn.commit()
