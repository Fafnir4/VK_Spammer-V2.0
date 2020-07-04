#!/usr/bin/python
# -*- coding cp1251 -*-
#-*- coding utf8 -*-
# Author: https://vk.com/fafnir_4

import os, time
os.system("clear")
print()
print('╔╗──╔╗─╔╗╔═╗───╔═══╗╔═══╗╔═══╗╔═╗╔═╗╔═╗╔═╗╔═══╗╔═══╗')
print('║╚╗╔╝║─║║║╔╝───║╔═╗║║╔═╗║║╔═╗║║║╚╝║║║║╚╝║║║╔══╝║╔═╗║')
print('╚╗║║╔╝─║╚╝╝────║╚══╗║╚═╝║║║─║║║╔╗╔╗║║╔╗╔╗║║╚══╗║╚═╝║')
print('─║╚╝║──║╔╗║────╚══╗║║╔══╝║╚═╝║║║║║║║║║║║║║║╔══╝║╔╗╔╝')
print('─╚╗╔╝──║║║╚╗───║╚═╝║║║───║╔═╗║║║║║║║║║║║║║║╚══╗║║║╚╗')
print('──╚╝───╚╝╚═╝───╚═══╝╚╝───╚╝─╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚═══╝╚╝╚═╝')
print('                    V 2.0                           ')
print('                  By Fafnir                         ')
config = {}



print()
print('                  Действия:                  ')
print()
print("[0] Авторизация")
print("[1] Спам одного человека")
print("[2] Спам беседы")
print("[3] Спам рассылка")
print("[4] ВЗРЫВ!!!")
print()
doit = input("Выберете действие: ")

if doit == "0":
    print()
    print('Авторизация')
    print()
    username = input("Логин:")
    print()
    password = input("Пароль:")
    f = open("config.py", "w")
    f.write("username = '" + username + "'\n")
    f.write("password = '" + password + "'\n")
    f.close()
    print()
    print("Готово.")
    time.sleep(4)
    os.system("clear")
    os.system("python3 start.py")


if doit == "1":
    print("Выбран спам одного пользывателя.")
    time.sleep(1)
    os.system("clear")
    os.system("python3 1spam.py")

if doit == "2":
    print("Выбран спам беседы.")
    time.sleep(1)
    os.system("clear")
    os.system("python3 chat.py")

if doit == "3":
    print("Выбран спам рассылка.")
    time.sleep(1)
    os.system("clear")
    os.system("python3 invite.py")

if doit == "4":
    print("Выбран ВЗРЫВ!!!.")
    time.sleep(1)
    os.system("clear")
    os.system("python3 exp.py")

if doit <= "4":
    print("Не верное действие")
    time.sleep(1)
    os.system("clear")
    os.system("python3 start.py")

if doit >= "0":
    print("Не верное действие")
    time.sleep(1)
    os.system("clear")
    os.system("python3 start.py")
