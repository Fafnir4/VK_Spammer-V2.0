#!/usr/bin/python
# -*- coding cp1251 -*-
#-*- coding utf8 -*-
# Author: https://vk.com/fafnir_4

import vk, urllib.request, urllib.error, urllib.parse, json, random, time

print('╔═══╗─╔══╗╔══╗─╔═══╗─╔╗───╔══╗─╔══╗─╔══╗─╔══╗─╔╗─╔╗')
print('║╔══╝─╚═╗║║╔═╝─║╔═╗║─║║───║╔╗║─║╔═╝─╚╗╔╝─║╔╗║─║╚═╝║')
print('║╚══╗───║╚╝║───║╚═╝║─║║───║║║║─║╚═╗──║║──║║║║─║╔╗─║')
print('║╔══╝───║╔╗║───║╔══╝─║║───║║║║─╚═╗║──║║──║║║║─║║╚╗║')
print('║╚══╗─╔═╝║║╚═╗─║║────║╚═╗─║╚╝║─╔═╝║─╔╝╚╗─║╚╝║─║║─║║')
print('╚═══╝─╚══╝╚══╝─╚╝────╚══╝─╚══╝─╚══╝─╚══╝─╚══╝─╚╝─╚╝')
print('                      V 1.0                        ')
print('                     By Fafnir                     ')
config = {}

try:
	exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)
except IOError:
	print("Не удалось получить логин и пароль, Введите их снова с помощью авторизации")
	input('нажмите ENTER для выхода') 


url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("Неверный логин или пароль (Перезапишите c помошью авторизации)")
    input('нажмите ENTER для выхода')

r = r.read()
token = json.loads(r)["access_token"] 
session = vk.Session(access_token = token)
vk = vk.API(session)

try:
    cast = open('cast.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('foo.txt', 'w', encoding='utf-8')
    print("Словарь каста отсутствует. Был создан новый")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

if not cast:
    print("Словарь каста пуст. Добавьте в него слова.")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

try:
    expid = open('expid.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('expid.txt', 'w', encoding='utf-8')
    print("Словарь id отсутствует. Был создан новый")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

if not cast:
    print("Словарь id пуст. Добавьте в него слова.")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

print("Словарь каста:")
print()
print()
print (cast)
print()
print()
print("Словарь взрыва:")
print()
print()
print (expid)
print()
print()
victim = input("id группы: ")

r = vk.users.get(user_ids = victim, fields = "id", v = 5.73)
r = r[0]["id"]

victim = r
print("Взрыв запущен")
print()
print("Нажмите Ctrl+C для выхода")
r = vk.messages.send(peer_id =2000000000 + victim, message = random.choice(cast), v = 5.73)
time.sleep(6)
r = vk.messages.send(peer_id =2000000000 + victim, message = "ВЗРЫВ!!!", v = 5.73)
time.sleep(3)
r = vk.messages.send(peer_id =2000000000 + victim, message = expid, v = 5.73)
print()
time.sleep(3)
print("Каст...")
time.sleep(3)
print("Взорвано")
os.system("cls")
os.system("python spam.py")
