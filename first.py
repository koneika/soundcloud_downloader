from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import requests
#from sclib import SoundcloudAPI, Track, Playlist
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


with open(r'C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\page_code.html', 'r', encoding='utf-8') as file:
    page_source = file.read()

with open('new_page_code.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

i = 0
counter = 0



with open(r'C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\data.txt', 'w', encoding='utf-8') as file:
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
                    file.write(result + '\n')
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
        




# for i in range(0, counter):
#     api = SoundcloudAPI()
#     track = api.resolve(filename2[i])

#     assert type(track) is Track
    
#     filename = str(random.random()) + ".mp3"
#     print(filename2[i])
#     # time.sleep(15)
#     if len(filename2[i]) < 120:
#         with open(filename, 'wb+') as file:
#             track.write_mp3_to(file)
#     else:
#         print("к сожалению, как бы я не старался, но его ссылка настолько огромная, что саунд клауд отказывает скачивать с неё музыку, без обид, вот ваша потерянная ссылка:" + filename2[i])


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


# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service

# # Настройка Firefox в headless режиме
# firefox_options = Options()
# firefox_options.add_argument("--headless")  # Обеспечивает работу без графического интерфейса

# # Путь к драйверу geckodriver (убедитесь, что он у вас установлен и доступен)
# service = Service('C:/Users/slava/Desktop/py/soundcloud/github/pythons-main/list_of_prices/geckodriver.exe')  # Замените на актуальный путь

# # Инициализация драйвера
# driver = webdriver.Firefox(options=firefox_options, service=service)

# # Открываем нужный сайт
# url = 'https://soundcloud.com/koffeika_let/likes'  # Замените на нужный URL
# driver.get(url)

# # Прокрутка до конца страницы (несколько способов)
# # 1. С помощью JavaScript:
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # 2. Постепенная прокрутка (если важна имитация поведения пользователя)
# from selenium.webdriver.common.keys import Keys
# html = driver.find_element("tag name", "html")  # Находим элемент <html>
# html.send_keys(Keys.END)  # Прокручиваем до конца

# # Сохранение исходного кода страницы
# source_code = driver.page_source
# with open('sourcecode.html', 'w', encoding='utf-8') as f:
#     f.write(source_code)

# # Закрываем браузер
# driver.quit()
