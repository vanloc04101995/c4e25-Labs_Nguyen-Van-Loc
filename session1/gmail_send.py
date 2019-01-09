import random
from gmail import *
import datetime
sickness_list = ["ốm","đau răng","cảm cúm"]
while True:
    now = datetime.datetime.now()
    if now.hour == 7 and now.minute == 0 and now.second == 0:
        gmail = GMail('Nguyen Loc <nguyenlocxtnd@gmail.com>','nguyenvanloc1995')
        html_template ='''
        <h>Chào thầy!</h>
        <p>Hôm nay em bị <strong>{{sickness}}</strong> nên xin phép thầy cho em nghỉ hôm nay ạ.</p>
        <a href="https://mail.google.com/mail/u/0/#inbox/FMfcgxwBTsjpCzSqfksKmxTKVVhDXBSD"> Click to me </a>'''
        html_content = html_template.replace("{{sickness}}",random.choice(sickness_list))
        msg = Message('Test Message',to='nguyenlocxtnd@gmail.com>',html = html_content)
        gmail.send(msg)