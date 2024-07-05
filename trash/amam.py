from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests


# # Укажите путь к драйверу Chrome
# driver_path = '/путь/к/chromedriver'

# Инициализируйте веб-драйвер
driver = webdriver.Firefox()

url = 'https://soundcloud.com/koffeika_let/likes'  # Замените на нужный URL
driver.get(url)

def scroll_to_end():
    # Прокрутите страницу вниз до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Прокручивайте страницу, пока не достигнете конца
while True:
    prev_height = driver.execute_script("return document.body.scrollHeight")
    scroll_to_end()
    time.sleep(0.9)  # Пауза между прокрутками

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:
        
        break  # Достигли конца страницы


# Получение всего кода страницы
page_source = driver.page_source

# Сохранение кода в файл
with open('page_code.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

driver.quit()

with open('page_code.html', 'r', encoding='utf-8') as file:
    page_source = file.read()

soup = BeautifulSoup(page_source, "lxml")

h2_tags = soup.find_all('h2')
a_tags = soup.find_all('a')

for tag in h2_tags + a_tags:
    if 'href' in tag.attrs:
        print(f"Тег: {tag.name}, Строка: {tag.text.strip()}, Ссылка: {tag['href']}")



# from bs4 import BeautifulSoup

# # Получите HTML-код страницы
# page_source = driver.page_source

# # Создайте объект BeautifulSoup
# soup = BeautifulSoup(page_source, 'html.parser')

# # Извлеките данные, которые вас интересуют
# # Например:
# # data = soup.find_all('div', class_='your-data-class')

