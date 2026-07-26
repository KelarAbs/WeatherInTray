from pystray import Icon,Menu,MenuItem
import PIL.Image
from pogodadata import get_weather,city
import  webbrowser
import os
import sys
from time import sleep
import threading

currect_weather = {
    'temp': 'Загрузка...',
    'nebo': 'Загрузка...',
    'veter': 'Загрузка...',
    'vlazhnost': 'Загрузка...'
}

def weather_updater():
    global currect_weather
    while True:
        try:
            currect_weather = get_weather()
            icon.update_menu()
        except Exception as e:
            print(f'Ошибка обновления: {e}')
        sleep(1500)

def image_path(path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath('.')
    return os.path.join(base_path,path)

image = PIL.Image.open(image_path('cloud.png'))

def stop():
    icon.stop()

def on_click():
    webbrowser.open(f"https://yandex.ru/pogoda/ru/{city}/")

icon = Icon('Погода', image,menu=Menu(
    MenuItem(text=lambda item:f"Температура: {currect_weather['temp']}",action=None),
    MenuItem(text=lambda item:f"Осадки: {currect_weather['nebo']}",action=None),
    MenuItem(text=lambda item:f"Ветер: {currect_weather['veter']}",action=None),
    MenuItem(text=lambda item:f"Влажность: {currect_weather['vlazhnost']}",action=None),
    MenuItem(f'Подробнее...',on_click),
    MenuItem('Выход',stop)
    )
)

if __name__=='__main__':
    try:
        current_weather = get_weather()
    except Exception as e:
        print(f"Не удалось загрузить погоду при старте: {e}")
    updater_thread=threading.Thread(target=weather_updater,daemon=True)
    updater_thread.start()
    icon.run()