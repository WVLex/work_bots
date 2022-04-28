import psycopg2
from psycopg2 import Error
from audio_bot.config.config import host, user, password, database, port


def check_user(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM audiobot_users WHERE tg_id = %s'''

                get_column_names = "SELECT column_name " \
                                   "FROM information_schema.columns " \
                                   "WHERE " \
                                   "table_name = 'audiobot_users' " \
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
                append_field_query = '''INSERT INTO audiobot_users (tg_id, counter, pay) VALUES (%s, %s, %s)'''
                cur.execute(append_field_query, (tg_id, 3, False))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def update_value(tg_id, column: str, value):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''UPDATE audiobot_users SET {} = %s WHERE tg_id = %s'''.format(column)
                cur.execute(query, (value, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения pay", error)


def get_audio_id(counter):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = '''SELECT id FROM audio_bot_files_id WHERE counter = %s'''
                cur.execute(query, (counter, ))
                data = cur.fetchone()
                return data[0]
            except (Exception, Error) as error:
                print("Ошибка при изменении получении id аудио", error)


def add_audio(aid):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''INSERT INTO audio_bot_files_id (id) VALUES (%s)'''
                cur.execute(append_field_query, (aid, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_users_with_pay_vlaue():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''SELECT tg_id FROM audiobot_users WHERE pay = (%s)'''
                cur.execute(append_field_query, (True, ))
                data = cur.fetchall()
                return data
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)

print(get_users_with_pay_vlaue())