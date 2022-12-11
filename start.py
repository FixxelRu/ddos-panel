import os
os.system("pip3 install requests")
import requests
import random
import time

os.system("clear")
print("Загрузка файлов...")
os.system("rm main.py")
pr = open('main.py', 'a+', encoding='utf-8')
px = requests.get("https://fixxel.tk/main.py").text
pr.write(px)
os.system("clear")
print("Загрузка панели...")
os.system("rm panel.py")
ua = open('panel.py', 'a+', encoding='utf-8')
uas = requests.get("https://fixxel.tk/panel.py").text
ua.write(uas)
os.system("clear")
print("Все файлы загружены!")
print("Чтобы начать пользоваться панелью введите команду которая будет ниже")
print("python main.py")