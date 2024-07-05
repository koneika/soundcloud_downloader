from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import requests
from sclib import SoundcloudAPI, Track, Playlist # pip install soundcloud-lib
import random

# # Инициализируйте веб-драйвер
# driver = webdriver.Firefox()

# url = 'https://soundcloud.com/koffeika_let/likes'  # Замените на нужный URL
# driver.get(url)

# def scroll_to_end():
#     # Прокрутите страницу вниз до конца
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # Прокручивайте страницу, пока не достигнете конца
# while True:
#     prev_height = driver.execute_script("return document.body.scrollHeight")
#     scroll_to_end()
#     time.sleep(0.9)  # Пауза между прокрутками

#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == prev_height:
        
#         break  # Достигли конца страницы


# # Получение всего кода страницы
# page_source = driver.page_source

# # Сохранение кода в файл
# with open('page_code.html', 'w', encoding='utf-8') as file:
#     file.write(page_source)

# driver.quit()

import os
import selenium


# Вариант 1: Изменить рабочую директорию
os.chdir(r'C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices')  # Замените на ваш путь


with open('page_code.html', 'r', encoding='utf-8') as file:
    page_source = file.read()

# with open('new_page_code.html', 'w', encoding='utf-8') as file:
#     file.write(page_source)

i = 0
counter = 0



with open('data.txt', 'w', encoding='utf-8') as file:
    if f'<a class="sound__coverArt" href="' in page_source:

        print(-1)
        # Ваша строка с текстом
        # text = "Ваш текст до символа ?"

        # Ищем индекс символа "?"
        word_for_find = f'<a class="sound__coverArt" href="'
        index = page_source.find(word_for_find)
        # Если символ найден, выводим текст до него
        while index != -1:
            # if page_source[index+len(word_for_find) : index+len(word_for_find)+i] != '"':
            #     result = page_source[index+len(word_for_find) : index+len(word_for_find)+128]
            #     index = page_source.find(word_for_find, index + len(word_for_find))
            #     print(result)
            if page_source[index+len(word_for_find) : index+len(word_for_find)+i] != '"':
                # time.sleep(0.5)
                result = page_source[index+len(word_for_find) : index+len(word_for_find)+i] # 9999 : 9999 + 32
                
                i += 1
                if '"' in page_source[index+len(word_for_find) : index+len(word_for_find)+i]:
                    i -= i
                    counter += 1
                    # index = page_source.find(word_for_find, index + len(word_for_find))
                    # print(str(counter) + ". " + "https://soundcloud.com" + result)
                    # filename2[i] = file.read()
                    index = page_source.find(word_for_find, index + len(word_for_find))
                    print(str(counter) + ". " + "https://soundcloud.com" + result)
                    file.write("https://soundcloud.com" + result + '\n')
            #     else if 
        
            
    else:
        print("Символ не найден в тексте.")



filename = [] # создаю пустой массив с размером столько сколько найдено музыки

# эта штука нужна, создать за ранее названия музыки, сколько нашло ссылок на музыку, столько и будет в массиве рандомных названий для музыки
# если музыки будет 361, то и ранд. названий будет 361 заложено в массивах
# for i in range(0, counter): # РАБОТАЙ теперь от 0 - сколько музыки
#     filename.append(str(random.random()) + ".mp3")
#     print(filename[i])


# тоже самое что и filename только другой массив, заче если можно было использовать такой же массив что и прошлый, ответ - я не знаю
# но пусть будет пока так, до выхода релиза
filename2 = []

counter -= counter
# открываем файл с заранее уже имеющимися ссылками от sc, чтобы заюзать логику по скачиванию музыки
with open("data.txt", 'r') as file:

    # каждая строчка с data.txt будет теперь отрабатывать for line in file кек
    for line in file:
        # print(line)
        # input()
        # time.sleep(1)
        # filename2.append(line.strip())
        # time.sleep(1)
        # print(filename2[counter])# выведет каждую строчку с data.txt
        filename2.append(line.strip())

        
        print(filename2[counter])
        counter += 1
        




for i in range(88, counter):
    api = SoundcloudAPI()
    track = api.resolve(filename2[i])
    print(track)
    with open(filename, 'wb+') as file:
        print(track.write_mp3_to(file))
    #assert type(track) is Track
    
    filename = str(random.random()) + ".mp3"
    print(i, filename2[i])
    # time.sleep(15)
    if len(filename2[i]) < 120:
        with open(filename, 'wb+') as file: #old code
            track.write_mp3_to(file)        #old code
    # else:
    #     print("к сожалению, как бы я не старался, но его ссылка настолько огромная, что саунд клауд отказывает скачивать с неё музыку, без обид, вот ваша потерянная ссылка:" + filename2[i])
 

    # api = SoundcloudAPI()  
    # track = api.resolve('https://soundcloud.com/hyzrit/weird')

    # assert type(track) is Track

    # filename = f'./{track.artist} - {track.title}.mp3'

    # with open(filename, 'wb+') as file:
    #     track.write_mp3_to(file)

# soup = BeautifulSoup(page_source, "lxml")

# h2_tags = soup.find_all('h2')
# a_tags = soup.find_all('a')

# for tag in h2_tags + a_tags:
#     if 'href' in tag.attrs:
#         print(f"Тег: {tag.name}, Строка: {tag.text.strip()}, Ссылка: {tag['href']}")

        # line2[line] = line.strip()
        # print(line2) 

