# Токен бота
token = '5332858863:AAFa_B0Sm4I63igPecySGt3-0McBhv16Stk'

# Константы базы данных
host = 'pg2.sweb.ru'
user = 'v4tograpru_lex'
password = 'AlexCoolBoy22'
database = 'v4tograpru_lex'
port = 5432

# Админы
admins = [126668370, 244607176]


receiver = None
targets = None
sum = None

url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
      'receiver={receiver}&' \
      'quickpay-form=shop&' \
      'label={label}&' \
      'targets={targets}&' \
      'paymentType=SB&' \
      'sum={sum}'.format(receiver=None, targets=None, sum=None, label=None)
