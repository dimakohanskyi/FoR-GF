import requests
from bs4 import BeautifulSoup
import smtplib
import random
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL_SEC")
TO_EMAIL = os.getenv("TO_EMAIL_SEC")
MY_PASSWORD = os.getenv("MY_PASSWORD_SEC")
URL = "https://www.stylecraze.com/articles/compliments-for-girls/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
res = soup.find("ol")

with open("data.txt", "w") as data_file:
     # Iterate through each tag and write it to a new line in the file
     for tag in res.find_all():
         tag_str = str(tag)
         data_file.write(tag_str + "\n")

with open("data.txt", "r") as data_file:
    compliments = data_file.read().splitlines()

random_compliment = random.choice(compliments)

cleaned_compliment = BeautifulSoup(random_compliment, "html.parser").get_text()


emoji_heart = "❤️"
message = f"{emoji_heart}LOVE YOU {emoji_heart}"
message_text = f"Yea maybe I can't say this for you every day, but I can write a script which makes this instead of me\n\n" \
               f"{message}{cleaned_compliment}{message}"
# Convert the message to bytes using the 'utf-8' codec
message_bytes = message_text.encode('utf-8')


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
         from_addr=MY_EMAIL,
         to_addrs=TO_EMAIL,
         msg=message_bytes
     )




