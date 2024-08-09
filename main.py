import random
import smtplib
import datetime as dt
import pandas as pd

my_email = 'mike.test.2424@gmail.com'
my_password = 'pxrt sqnz mqjq kaxc'
now = dt.datetime.now()

data = pd.read_csv('birthdays.csv').to_dict('records')
with open(f'./letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as letter_templates:
    letter = letter_templates.read()

for item in data:
    if item['month'] == now.month and item['day'] == now.day:
        new_letter = letter.replace('[NAME]', item['name'])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=item['email'],
                msg=f'Subject:Happy Birthday\n\n{new_letter}')




