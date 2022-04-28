import sys
import psycopg2
import string
import random
from psycopg2 import Error
sys.path.append('/home/v/v4tograpru/public_html/meditation')
from meditation.config.config import host, user, password, database, port


def check_user(key):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                check_user_query = '''SELECT * FROM meditation_users WHERE tg_id = %s'''
                cur.execute(check_user_query, (key,))
                data = cur.fetchall()
                if data:
                    data = {
                        'tg_id': data[0][0],
                        'pay': data[0][1],
                        'id': data[0][2],
                        'relax_label': data[0][3],
                        'anxiety_label': data[0][4],
                        'full_label': data[0][5],
                        'doit_label': data[0][6],
                        'relax_url': data[0][7],
                        'anxiety_url': data[0][8],
                        'full_url': data[0][9],
                        'doit_url': data[0][10],
                        'twelve_meditation_label': data[0][11],
                        'six_meditation_label': data[0][12],
                        'twelve_meditation_url': data[0][13],
                        'six_meditation_url': data[0][14],
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
                append_field_query = '''INSERT INTO meditation_users (tg_id) VALUES (%s)'''
                cur.execute(append_field_query, (tg_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def get_all_data(table):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "SELECT * FROM {}".format(table)
                cur.execute(query)
                data = cur.fetchall()
                return data
            except (Exception, Error) as error:
                print("Ошибка вывода всех значений из таблицы " + table, error)


def delete_from_massmailing(mail_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                query = "DELETE FROM massmailing WHERE name = 'meditation_bot' AND id = (%s)"
                cur.execute(query, (mail_id,))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при удалении прогноза из таблицы massmailing", error)


def append_massmail_text(text):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                append_field_query = '''INSERT INTO massmailing (name, text) VALUES ('meditation_bot', %s)'''
                cur.execute(append_field_query, (text, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при добавлении значения в таблицу", error)


def update_labels(tg_id, relax_label, anxiety_label, full_label, doit_label,
                  quickpay_relax_url, quickpay_anxiety_url, quickpay_full_url, quickpay_doit_url,
                  twelve_meditation_label, six_meditation_label, twelve_meditation_url, six_meditation_url):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_label_query = 'UPDATE meditation_users SET relax_label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (relax_label, tg_id))
                change_label_query = 'UPDATE meditation_users SET anxiety_label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (anxiety_label, tg_id))
                change_label_query = 'UPDATE meditation_users SET full_label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (full_label, tg_id))
                change_label_query = 'UPDATE meditation_users SET doit_label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (doit_label, tg_id))
                change_label_query = 'UPDATE meditation_users SET relax_url = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (quickpay_relax_url, tg_id))
                change_label_query = 'UPDATE meditation_users SET anxiety_url = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (quickpay_anxiety_url, tg_id))
                change_label_query = 'UPDATE meditation_users SET full_url = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (quickpay_full_url, tg_id))
                change_label_query = 'UPDATE meditation_users SET doit_url = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (quickpay_doit_url, tg_id))
                change_label_query = 'UPDATE meditation_users SET twelve_meditation_label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (twelve_meditation_label, tg_id))
                change_label_query = 'UPDATE meditation_users SET six_meditation_label = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (six_meditation_label, tg_id))
                change_label_query = 'UPDATE meditation_users SET twelve_meditation_url = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (twelve_meditation_url, tg_id))
                change_label_query = 'UPDATE meditation_users SET six_meditation_url = %s WHERE tg_id = %s'
                cur.execute(change_label_query, (six_meditation_url, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения label", error)


def change_pay_value(tg_id, boolean):
    with psycopg2.connect(host='pg2.sweb.ru',
                          user='v4tograpru_lex',
                          password='AlexCoolBoy22',
                          database='v4tograpru_lex',
                          port=5432) as conn:
        with conn.cursor() as cur:
            try:
                change_pay_query = 'UPDATE meditation_users SET pay = %s WHERE tg_id = %s'
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
                change_pay_query = 'UPDATE meditation_users SET message_id = %s WHERE tg_id = %s'
                cur.execute(change_pay_query, (message_id, tg_id))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения message_id_to_edit", error)


def delete_all_pay_values(tg_id):
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                change_pay_query = 'UPDATE meditation_users SET relax_url = NULL WHERE tg_id = %s'
                cur.execute(change_pay_query, (tg_id, ))
                change_pay_query = 'UPDATE meditation_users SET anxiety_url = NULL WHERE tg_id = %s'
                cur.execute(change_pay_query, (tg_id, ))
                change_pay_query = 'UPDATE meditation_users SET full_url = NULL WHERE tg_id = %s'
                cur.execute(change_pay_query, (tg_id, ))
                change_pay_query = 'UPDATE meditation_users SET doit_url = NULL WHERE tg_id = %s'
                cur.execute(change_pay_query, (tg_id, ))
                change_pay_query = 'UPDATE meditation_users SET twelve_meditation_url = NULL WHERE tg_id = %s'
                cur.execute(change_pay_query, (tg_id, ))
                change_pay_query = 'UPDATE meditation_users SET six_meditation_url = NULL WHERE tg_id = %s'
                cur.execute(change_pay_query, (tg_id, ))
                conn.commit()
            except (Exception, Error) as error:
                print("Ошибка при изменении значения message_id_to_edit", error)


def get_all_tg_id():
    with psycopg2.connect(host=host,
                          user=user,
                          password=password,
                          database=database,
                          port=port) as conn:
        with conn.cursor() as cur:
            try:
                get_all_query = 'SELECT tg_id FROM meditation_users'
                cur.execute(get_all_query)
                data = cur.fetchall()
                return [i[0] for i in data]
            except (Exception, Error) as error:
                print("Ошибка при получении значения tg_id", error)


def get_tg_id_from_label(label):
    with psycopg2.connect(host='pg2.sweb.ru',
                          user='v4tograpru_lex',
                          password='AlexCoolBoy22',
                          database='v4tograpru_lex',
                          port=5432) as conn:
        with conn.cursor() as cur:
            try:
                query = 'SELECT tg_id FROM meditation_users WHERE relax_label = %s'
                cur.execute(query, (label,))
                data1 = cur.fetchall()
                query = 'SELECT tg_id FROM meditation_users WHERE anxiety_label = %s'
                cur.execute(query, (label,))
                data2 = cur.fetchall()
                query = 'SELECT tg_id FROM meditation_users WHERE full_label = %s'
                cur.execute(query, (label,))
                data3 = cur.fetchall()
                query = 'SELECT tg_id FROM meditation_users WHERE doit_label = %s'
                cur.execute(query, (label,))
                data4 = cur.fetchall()
                query = 'SELECT tg_id FROM meditation_users WHERE twelve_meditation_label = %s'
                cur.execute(query, (label,))
                data5 = cur.fetchall()
                query = 'SELECT tg_id FROM meditation_users WHERE six_meditation_label = %s'
                cur.execute(query, (label,))
                data6 = cur.fetchall()
                new = data1 + data2 + data3 + data4 + data5 + data6
                return new[0][0]
            except (Exception, Error) as error:
                print("Ошибка при извдечении значения tg_id по label", error)


# --------- Support funcs ---------
def get_pay_urls(tg_id):
    relax_label = 'relx' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    quickpay_relax_url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
                         'receiver=4100117596986931&' \
                         'label={}&' \
                         'quickpay-form=shop&' \
                         'targets=Осознанные+медитации+-+Расслабиться&' \
                         'paymentType=SB&' \
                         'sum=3500'.format(relax_label)

    anxiety_label = 'anxi' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    quickpay_anxiety_url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
                           'receiver=4100117596986931&' \
                           'label={}&' \
                           'quickpay-form=shop&' \
                           'targets=Осознанные+медитации+-+Снять+тревогу&' \
                           'paymentType=SB&' \
                           'sum=3500'.format(anxiety_label)

    full_label = 'full' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    quickpay_full_url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
                        'receiver=4100117596986931&' \
                        'label={}&' \
                        'quickpay-form=shop&' \
                        'targets=Осознанные+медитации+-+Наполниться&' \
                        'paymentType=SB&' \
                        'sum=3500'.format(full_label)
    doit_label = 'doit' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    quickpay_doit_url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
                        'receiver=4100117596986931&' \
                        'label={}&' \
                        'quickpay-form=shop&' \
                        'targets=Осознанные+медитации+-+Действовать&' \
                        'paymentType=SB&' \
                        'sum=3500'.format(doit_label)

    twelve_meditation_label = 'twlv' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    quickpay_twelve_url = 'https://snebaupal.ru/meditation/twelve/{}'.format(twelve_meditation_label)

    six_meditation_label = 'sixx' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    quickpay_six_url = 'https://snebaupal.ru/meditation/half/{}'.format(six_meditation_label)

    update_labels(tg_id, relax_label, anxiety_label, full_label, doit_label,
                  quickpay_relax_url, quickpay_anxiety_url, quickpay_full_url, quickpay_doit_url,
                  twelve_meditation_label, six_meditation_label, quickpay_twelve_url, quickpay_six_url)


def make_dict(data):
    data = data.split('&')
    new_dict = {i.split('=')[0]: i.split('=')[1] for i in data}
    return new_dict