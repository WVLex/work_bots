import psycopg2
from psycopg2 import Error
import datetime

from bagriy_bot.config.config import host, user, password, database, port


def check_user(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM bagriy_bot_users WHERE tg_id = %s'''

                get_column_names = "SELECT column_name " \
                                   "FROM information_schema.columns " \
                                   "WHERE " \
                                   "table_name = 'bagriy_bot_users' " \
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
                append_field_query = '''INSERT INTO bagriy_bot_users (tg_id, date_start) VALUES (%s, %s)'''
                cur.execute(append_field_query, (tg_id, datetime.datetime.now()))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_group_of_users():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''SELECT * FROM bagriy_bot_users'''
                cur.execute(append_field_query)
                data = cur.fetchall()
                send_text = [i for i in data if datetime.datetime.now() - i[2] < datetime.timedelta(days=7) or
                             i[1] is True]
                send_pay = [i for i in data if datetime.datetime.now() - i[2] >= datetime.timedelta(days=7) and
                            i[1] is None]
                send_monthly_msg = [i for i in data if datetime.datetime.now() - i[3] >= datetime.timedelta(days=30)]
                return send_text, send_pay, send_monthly_msg
            except (Exception, Error) as error:
                print("Ошибка при чтении из таблицы", error)


def get_texts():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''SELECT * FROM bagriy_bot_texts'''
                cur.execute(query)
                data = {a: b for a, b in cur.fetchall()}
                return data
            except (Exception, Error) as error:
                print("Ошибка при чтении из таблицы", error)


def update_value(tg_id, column, value):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''UPDATE bagriy_bot_users SET {} = %s WHERE tg_id = %s'''.format(column)
                cur.execute(query, (value, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при чтении из таблицы", error)
