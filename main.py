import smtplib

my_email = 'mike.test.2424@gmail.com'
my_password = 'pxrt sqnz mqjq kaxc'

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='miketest2424@yahoo.com',
        msg='Subject:Hello Again\n\nTesting Testing 123...')
