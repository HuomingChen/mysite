import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自1',
        '欢迎访问',
        'gamefile6@163.com',
        ['gamefile1@163.com'],
    )