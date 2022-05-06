import psycopg2
from psycopg2 import Error
import datetime
from new_makbot.config.config import host, user, password, database, port
import random


def check_user(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM new_makbot_users WHERE tg_id = %s'''

                get_column_names = "SELECT column_name " \
                                   "FROM information_schema.columns " \
                                   "WHERE " \
                                   "table_name = 'new_makbot_users' " \
                                   "AND table_catalog = 'v4tograpru_lex' " \
                                   "AND table_schema = 'public'"

                cur.execute(get_column_names)
                column_names = cur.fetchall()

                cur.execute(check_user_query, (tg_id, ))
                data = cur.fetchall()
                if data:
                    data = {column_names[index][0]: data[0][index] for index, i in enumerate(data[0])}
                return data
            except (Exception, Error) as error:
                print("Ошибка при чтении из таблицы", error)


def append_user(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''INSERT INTO new_makbot_users (tg_id, counter) VALUES (%s, 0)'''
                cur.execute(append_field_query, (tg_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_user_counter(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''SELECT counter FROM new_makbot_users WHERE tg_id = %s'''
                cur.execute(query, (tg_id, ))
                data = cur.fetchone()
                return data[0]
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_card_id(card_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''SELECT card_id FROM new_makbot_photo WHERE id = %s'''
                cur.execute(query, (card_id, ))
                data = cur.fetchone()
                return data[0]
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def update_counter(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''UPDATE new_makbot_users SET counter = counter + 1 WHERE tg_id = %s'''
                cur.execute(query, (tg_id, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def zeroing_counter(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''UPDATE new_makbot_users SET counter = 0 WHERE tg_id = %s'''
                cur.execute(query, (tg_id, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def update_date(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''UPDATE new_makbot_users SET date = %s WHERE tg_id = %s'''
                cur.execute(query, (datetime.datetime.now(), tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def randomizer_for_cards():
    card_id = random.randint(1, 23)
    card_id = get_card_id(card_id)
    return card_id


def append_card(text):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''INSERT INTO new_makbot_photo (card_id) VALUES (%s)'''
                cur.execute(append_field_query, (text, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)