import psycopg2
from psycopg2 import Error
import datetime
from astro_bot.config.config import host, user, password, database, port


def check_user(key):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM astrobot_users WHERE tg_id = %s'''
                cur.execute(check_user_query, (key,))
                data = cur.fetchall()
                if data:
                    data = {
                        'tg_id': data[0][0],
                        'subscribe': data[0][1],
                    }
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
                append_field_query = '''INSERT INTO astrobot_users (tg_id) VALUES (%s)'''
                cur.execute(append_field_query, (tg_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_all_data():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "SELECT * FROM astrobot_forecasts"
                cur.execute(query)
                data = cur.fetchall()
                return data
            except (Exception, Error) as error:
                print("Ошибка вывода всех значений из таблицы", error)


def update_subscribe(tg_id, boolean):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''UPDATE astrobot_users SET subscribe = %s WHERE tg_id = %s'''
                cur.execute(append_field_query, (boolean, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_all_tg_id():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                get_all_query = 'SELECT tg_id, subscribe FROM astrobot_users'
                cur.execute(get_all_query)
                data = cur.fetchall()
                return [i[0] for i in data if i[1] is True]
            except (Exception, Error) as error:
                print("Ошибка при получении значения tg_id", error)


def get_all_subscribers():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                get_all_query = 'SELECT tg_id, subscribe FROM astrobot_users'
                cur.execute(get_all_query)
                data = cur.fetchall()
                return [i[0] for i in data if i[1] is True], [i[0] for i in data if i[1] is not True]
            except (Exception, Error) as error:
                print("Ошибка при получении значения tg_id", error)


""" Forecasts"""


def append_forecast(forecast, date):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "INSERT INTO astrobot_forecasts (forecast, date) VALUES (%s, %s)"
                value = parse_date(date)
                cur.execute(query, (forecast, value))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_all_forecasts():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "SELECT * FROM astrobot_forecasts"
                cur.execute(query)
                data = cur.fetchall()
                return data
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_forecast(forecast_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "SELECT * FROM astrobot_forecasts WHERE id = %s"
                cur.execute(query, (forecast_id,))
                data = cur.fetchall()
                return data[0]
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def delete_from_forecasts(forecast_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "DELETE FROM astrobot_forecasts WHERE id = %s"
                cur.execute(query, (forecast_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


"""Admin func"""


def check_admin(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM astrobot_admin WHERE tg_id = %s'''
                cur.execute(check_user_query, (tg_id,))
                data = cur.fetchall()
                if data:
                    data = {
                        'tg_id': data[0][0],
                        'state': data[0][1],
                        'forecast': data[0][2],
                    }
                    return data
                else:
                    data = {'state': None}
                    return data

            except (Exception, Error) as error:
                print("Ошибка при чтении из таблицы", error)


def update_state(tg_id, state):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''UPDATE astrobot_admin SET state = %s WHERE tg_id = %s'''
                cur.execute(append_field_query, (state, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def update_forecast(tg_id, forecast):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''UPDATE astrobot_admin SET forecast = %s WHERE tg_id = %s'''
                cur.execute(append_field_query, (forecast, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def append_admin(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "INSERT INTO astrobot_admin (tg_id) VALUES (%s)"
                cur.execute(query, (tg_id, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


"""Support func"""

def parse_date(date):
    date_and_time = date.split(' ')
    date = date_and_time[0].split('.')
    time = date_and_time[1].split(':')
    value = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]))
    return value