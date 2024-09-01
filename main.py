konec = ('.com','.ru','.net')
def send_email(message, recipient,*,sender = "university.help@gmail.com"):
    konec = ('.com','.net','.ru')
    if '@'not in recipient or not recipient.endswith(konec):
        print('Не возможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif '@'not in sender or not sender.endswith(konec):
        print('Не возможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'не стандартный отправитель! письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')