from aiogram.utils.markdown import bold


def msg_text(sneba_users, astro_users, yasna_users, audio_users, bagriy_users, new_makbot_users, meditation_users):
    msg_text = 'Колличетво пользователей\n' \
               'Подсказки вселенной: ' + bold('{}\n'.format(sneba_users)) + \
               'Вспомнить себя: ' + bold('{}\n'.format(yasna_users)) + \
               'Твоя поддержка: ' + bold('{}\n'.format(bagriy_users)) + \
               'Метафорические карты психолога: ' + bold('{}\n'.format(new_makbot_users)) + \
               'Осознанные медитации: ' + bold('{}\n'.format(meditation_users)) + \
               'Астробот: ' + bold('{}\n'.format(astro_users)) + \
               'Аудиокнига "Мама, я... Кто Я?: ' + bold('{}\n'.format(audio_users))
    return msg_text
