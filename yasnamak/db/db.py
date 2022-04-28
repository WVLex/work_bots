import psycopg2
from psycopg2 import Error
import random
import datetime
import codecs
from yasnamak.config import config
from yasnamak.config.config import host, user, password, database, port


def randomizer_for_datetime():
    hour = random.choice([0, 3, 6, 9, 12, 15, 18, 21])
    return hour


def check_user(key):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM yasnamak_users WHERE tg_id = %s'''
                cur.execute(check_user_query, (key,))
                data = cur.fetchall()
                if data:
                    data = {'id': data[0][0],
                            'tg_id': data[0][1],
                            'pay': data[0][2],
                            'time_to_send_message': data[0][3],
                            'message_id_to_edit': data[0][4],
                            'label': data[0][5],
                            'date_deactivate_subscribe': data[0][6],
                            'everyday_newsletter_time': data[0][7]}
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
                append_field_query = '''INSERT INTO yasnamak_users (tg_id) VALUES (%s)'''
                cur.execute(append_field_query, (tg_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def change_pay_value(tg_id, boolean):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_pay_query = 'UPDATE yasnamak_users SET pay = %s WHERE tg_id = %s'
                cur.execute(change_pay_query, (boolean, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения pay", error)


def update_message_id_to_edit(tg_id, message_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_pay_query = 'UPDATE yasnamak_users SET message_id_to_edit = %s WHERE tg_id = %s'
                cur.execute(change_pay_query, (message_id, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения message_id_to_edit", error)


def update_time_to_send_message(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'UPDATE yasnamak_users SET time_to_send_message = %s WHERE tg_id = %s'
                days_count = 7
                now = datetime.date.today()
                date_of_sending = now + datetime.timedelta(days=days_count)
                cur.execute(query, (date_of_sending, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения time_to_send_message", error)


def updates_time_to_send_message(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'UPDATE yasnamak_users SET time_to_send_message = %s WHERE tg_id = %s'
                now = datetime.date.today()
                for i in tg_id:
                    days_count = random.randint(1, 7)
                    date_of_sending = now + datetime.timedelta(days=days_count)
                    cur.execute(query, (date_of_sending, i))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при каскадном изменении значения time_to_send_message", error)


def set_none_in_time_to_send_message(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'UPDATE yasnamak_users SET time_to_send_message = NULL WHERE tg_id = %s'
                cur.execute(query, (tg_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения time_to_send_message на NULL", error)


def update_date_deactivate_subscribe(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                date = datetime.date.today() + datetime.timedelta(days=30)
                query = 'UPDATE yasnamak_users SET date_deactivate_subscribe = %s WHERE tg_id = %s'
                cur.execute(query, (date, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения date_deactivate_subscribe", error)


def update_everyday_newsletter_time(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                hour = randomizer_for_datetime()
                date = datetime.datetime.now() + datetime.timedelta(days=3)
                time = datetime.datetime(date.year, date.month, date.day, hour=hour, minute=2)
                query = 'UPDATE yasnamak_users SET everyday_newsletter_time = %s WHERE tg_id = %s'
                cur.execute(query, (time, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения date_deactivate_subscribe", error)


def deletes_date_deactivate_subscribe(ids):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'UPDATE yasnamak_users SET date_deactivate_subscribe = NULL WHERE tg_id = %s'
                for i in ids:
                    cur.execute(query, (i,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения date_deactivate_subscribe", error)


def delete_everyday_newsletter_time(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'UPDATE yasnamak_users SET everyday_newsletter_time = NULL WHERE tg_id = %s'
                cur.execute(query, (tg_id, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения date_deactivate_subscribe", error)


def get_all_tg_id():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                get_all_query = 'SELECT tg_id FROM yasnamak_users'
                cur.execute(get_all_query)
                data = cur.fetchall()
                return [i[0] for i in data]
            except (Exception, Error) as error:
                print("Ошибка при получении значения tg_id", error)


def get_today_subscribers_list():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_subscribe_query = 'SELECT tg_id, time_to_send_message FROM users'
                cur.execute(change_subscribe_query)
                raw_data = cur.fetchall()
                data = {}
                for i in raw_data:
                    if i[1] is not None:
                        data[i[0]] = i[1]

                now = datetime.datetime.now()
                today = []
                for i in data:
                    if data[i] <= now:
                        today.append(i)
                return today
            except (Exception, Error) as error:
                print("Ошибка при получении значений time_to_send_message", error)


def get_current_everyday_newsletter_time():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_subscribe_query = 'SELECT tg_id, everyday_newsletter_time FROM yasnamak_users'
                cur.execute(change_subscribe_query)
                raw_data = cur.fetchall()
                data = {}
                for i in raw_data:
                    if i[1] is not None:
                        data[i[0]] = i[1].date().strftime('{}/{}/{} {}'.format(i[1].month, i[1].day, i[1].year,
                                                                               i[1].hour))

                    now = datetime.datetime.now()
                    now = '{}/{}/{} {}'.format(now.month, now.day, now.year, now.hour)
                ids = []
                for i in data:
                    if data[i] == now:
                        ids.append(i)
                return ids
            except (Exception, Error) as error:
                print("Ошибка при получении значений time_to_send_message", error)


def update_label(tg_id, label):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_label_query = 'UPDATE yasnamak_users SET label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (label, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения label", error)


def get_list_to_deactivate():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_subscribe_query = 'SELECT tg_id, date_deactivate_subscribe FROM yasnamak_users'
                cur.execute(change_subscribe_query)
                raw_data = cur.fetchall()
                subscribe_list = []
                for i in raw_data:
                    if i[1] is not None and i[1].strftime("%m/%d/%Y") == datetime.date.today().strftime("%m/%d/%Y"):
                        subscribe_list.append(i[0])
                return subscribe_list
            except (Exception, Error) as error:
                print("Ошибка при изменении значения label", error)


def get_tg_id_from_label(label):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'SELECT tg_id FROM yasnamak_users WHERE label = %s'
                cur.execute(query, (label, ))
                data = cur.fetchall()[0][0]
                return data
            except (Exception, Error) as error:
                print("Ошибка при извдечении значения tg_id по label", error)


# def get_pay_url_and_label(tg_id):
#     label = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
#     quickpay = yoomoney.Quickpay(receiver='4100116717487131',
#                                  quickpay_form='shop',
#                                  targets='Подсказки Вселенной - подписка на месяц',
#                                  paymentType='SB',
#                                  sum=config.price,
#                                  label=label)
#     update_label(tg_id, label)
#     return quickpay.redirected_url, label


def get_photo(photo_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = 'SELECT photo_id FROM yasnamak_photo WHERE id = %s'
                cur.execute(query, (photo_id, ))
                data = cur.fetchall()[0][0]
                return data
            except (Exception, Error) as error:
                print("Ошибка при извлечении значения photo_id", error)


# --- Support functions ---
def randomizer_for_cards_and_poems():
    random_number = str(random.randint(1, 50))

    with codecs.open('texts.txt', 'r', 'utf_8_sig') as f:  # Выбор рандомного стиха
        poems_list = f.read().split(';\r\n')
        poems_dict = {}
        for i in poems_list:
            poem = i.split('~')
            poems_dict[poem[0]] = poem[1] + '\n\n©️ Ясна Токарик'

    return {'poem': poems_dict[random_number],
            'card_number': random_number}


# def check_transaction(label):
#     client = yoomoney.Client(config.yoo_token)
#     history = client.operation_history(label=label)
#     a = history.operations
#     return bool(a)


