#!/usr/bin/python
# -*- coding cp1251 -*-
#-*- coding utf8 -*-
# Author: https://vk.com/fafnir_4

import vk, urllib.request, urllib.error, urllib.parse, json, random, time

print('╔══╗─╔╗─╔╗─╔╗╔╗─╔══╗─╔════╗─╔═══╗')
print('╚╗╔╝─║╚═╝║─║║║║─╚╗╔╝─╚═╗╔═╝─║╔══╝')
print('─║║──║╔╗─║─║║║║──║║────║║───║╚══╗')
print('─║║──║║╚╗║─║╚╝║──║║────║║───║╔══╝')
print('╔╝╚╗─║║─║║─╚╗╔╝─╔╝╚╗───║║───║╚══╗')
print('╚══╝─╚╝─╚╝──╚╝──╚══╝───╚╝───╚═══╝')
print('             V 1.0               ')
print('           By Fafnir4            ')
config = {}

try:
	exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)
except IOError:
	print("Не удалось получить логин и пароль, Введите их снова с помощью: python auth.py")
	input('нажмите ENTER для выхода') 


url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("Неверный логин или пароль (Перезапишите c помошью python auth.py)")
    input('нажмите ENTER для выхода')

r = r.read()
token = json.loads(r)["access_token"] 
session = vk.Session(access_token = token)
vk = vk.API(session)

try:
    inv = open('inv.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('inv.txt', 'w', encoding='utf-8')
    print("Словарь рассылки отсутствует. Был создан новый inv.txt")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

if not inv:
    print("Словарь рассылки пуст. Добавьте в него слова.")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

try:
    ir = open('ID.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('ID.txt', 'w', encoding='utf-8')
    print("Словарь ID отсутствует. Был создан новый ID.txt")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

if not ir:
    print("Словарь ID пуст. Добавьте в него слова.")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)
print("Словарь рассылки:")
print()
print()
print (inv)
print()
print()

ll = (iter(ir))

while(0):

    victim = next(ll)
    r = vk.users.get(user_ids = victim, fields = "id", v = 5.73)
    r = r[0]["id"]
    victim = r

print("Рассылка запущена")
print()
print("Нажмите Ctrl+C для выхода")
def mainloop():
    while(1):
        try:
            time.sleep(7)
            victim = next(ll)
            r = vk.users.get(user_ids = victim, fields = "id", v = 5.73)
            r = r[0]["id"]
            victim = r
            r = vk.messages.send(peer_id = victim, message = random.choice(inv), v = 5.73)
            print("Жди...")
            print(victim)
            time.sleep(3)
            print("Отправлено:  ",random.choice(inv))
        except:
            print("Не отправлено")
            pass

mainloop()
