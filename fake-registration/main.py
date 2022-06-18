import telebot

import random

import fake_useragent
from fake_useragent import UserAgent
ua = UserAgent()

from faker import Faker
fake = Faker('ru_RU')
import faker

import requests

fake_user = fake_useragent.UserAgent().random

fake_name = fake.name()
fake_password = fake.password()
fake_email = fake.email()

symbols = ['a','b''d','c','e','f','g','q','z','r','u','y','p']
fake_username = random.choice(symbols) + str(fake.random.randint(10000000,100000000)) + random.choice(symbols)

print(f'{fake_name} {fake_password} {fake_email} {fake_username}')

url = 'https://knigavuhe.org/register/'

user_agent_val = fake_user

session = requests.Session()
r = session.get(url, headers = {
    'User-Agent': user_agent_val
})

session.headers.update({'Referer':url})

session.headers.update({'User-Agent':user_agent_val})

_xsrf = session.cookies.get('_xsrf', domain=".org")

post_request = session.post(url, {
     'backUrl': 'https://knigavuhe.org/',
     'name': fake_name,
     'surname': fake_name,
     'username': fake_username,
     'email': fake_email,
     'password': fake_password,
     '_xsrf':_xsrf,
     'remember':'yes',
})

