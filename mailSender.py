import yagmail
import sched, time
import os

user = 'myEmail@gmail.com'
app_password = 'myAppPasword'
to = 'receiverEmail@gmail.com'

subject = 'The Subject of the Email'
content = """\
Hi, 
You can write your message here !

Thank you.
Bye bye.
"""

timer = '300' # exemple: send email every 300 seconds

clear = lambda: os.system('cls')
clear()

#timer
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Email Sent")
    with yagmail.SMTP(user, app_password) as yag:
    	yag.send(to, subject, content)
    s.enter(timer, 1, do_something, (sc,))

s.enter(timer, 1, do_something, (s,))
s.run()
