
import smtplib
import datetime as dt
import random

now= dt.datetime.now()
weekday= now.weekday()
if weekday == 0:                            
    quote_file= open("./Day_32_/quotes.txt")
    all_quotes= quote_file.readlines()
    quote= random.choice(all_quotes)
    print(quote)  #quote will be generated in the console

MY_ID= "your ID"
MY_PASSWORD= "Your password"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_ID, MY_PASSWORD)

    connection.sendmail(
        from_addr= MY_ID,
        to_addrs= "sender's address",
        msg= f"Subject:Monday Motivation \n\n {quote}"
    )
