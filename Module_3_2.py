def send_email(message, recipient, sender='university.help@gmail.com'):
    variants = ('.com', '.ru', '.net')
    if ('@' in recipient and '@' in sender and recipient.endswith(variants)
            and sender.endswith(variants)) and recipient != sender\
            and sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)


send_email(message=input('Введите сообщение: '),
           recipient=input('Введите E-mail получателя: '),
           sender=input('Введите E-mail отправителя: '))