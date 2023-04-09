
import smtplib
import random as rd
import datetime as dt
import pandas as pd

MY_EMAIL ="your_mail@gmail.com"
PASSWORD = "your_password"

today = dt.datetime.now() # get current date and time
today_tuple = (today.month, today.day) # Створює в форматі tuple місяць і день

data = pd.read_csv("birthdays.csv") # Читаємо з файлу birthdays.csv
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()} # Дістаємо данні з файлу birthdays.csv

if today_tuple in birthday_dict: # Перевіряємо чи відповідні дати
    birthday_person = birthday_dict[today_tuple] 
    file_path = f"letter_{rd.randint(1, 3)}.txt" # Рандомно вибираємо файл
    with open(file_path) as letter_file:
        contents = letter_file.read() 
        contents = contents.replace("[NAME]", birthday_person["name"]) # Замінюємо відповідні дані
# ВИсилаємо листа на email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Шифруємо повідомлення
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday\n\n{contents}".encode('utf-8') # Усуває помилку з кодуванням
                )





    










