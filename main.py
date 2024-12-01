import asyncio
import re
import os

from playwright.async_api import async_playwright
from yt_dlp import YoutubeDL

async def scrape_dynamic_page(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        # Начальное значение высоты страницы
        last_height = await page.evaluate("document.body.scrollHeight")

        while True:
            # Прокрутка до конца страницы
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

            # Ожидание загрузки потенциально нового контента
            await page.wait_for_timeout(1000)  # Можно адаптировать время ожидания

            # Проверка, увеличилась ли высота страницы после прокрутки
            new_height = await page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                # Если высота не изменилась, прокрутка останавливается
                break
            last_height = new_height

        # Получение HTML страницы после динамической загрузки
        html_content = await page.content()
        await browser.close()
        return html_content

# Запуск асинхронной функции
async def main():
    ###
    # короче тут можно сделать автоматически спрашивать человека continue with 
    # https://sound... если вдруг чё программа остановилась
    # автоматизация короче такая темка, позже сделаем
    ###

    # html = "https://soundcloud/username/likes"

    if not os.path.exists("config.txt"):
        print("write your url of likes musics from your web-browser, " +
        "should be looks like this: https://soundcloud/username/likes")
        url = input()
        with open("fully_loaded_page.html", 'r', encoding='utf-8') as file:
            html = file.read()

        html = await scrape_dynamic_page(url)

        with open("fully_loaded_page.html", 'w') as file:
            file.write(html)
    else:
        with open("config.txt", 'r', encoding='utf-8') as file:
            url = file.read()

        print("do you want to continue? with this url: " + url)
        print(1. yes)
        print(2. no)


    linkes = ""

    pattern = r'<a class="sound__coverArt" href="([^"]+)"'
    matches = re.findall(pattern, html)

    # if last_part
    directory_path = 'music'

    # Список всех файлов
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    print("Файлы в директории:", files)

    # # check
    # with open("new_file.txt", 'w', encoding='utf-8') as file:
    #     file.write("")
    # for i, url in enumerate(matches, start=1):
    #     with open("new_file.txt", 'a', encoding='utf-8') as file:
    #         file.write(url + "\n")

    # Вывод результатов
    for i, url in enumerate(matches, start=1):
        last_part = url.split("/")[-1]
        # with open("new_file.txt", 'r', encoding='utf-8') as file:
        #     linkes = file.read()
        # print(linkes)
        # if files[i] == last_part

        # # Проверяем, что список не пуст
        # if files[i]:
        # for i in range(len(files)):
        print(i-1)


        # else:
        #     print("В директории нет файлов.")

        # Просто скипаем в лайках плейлист
        # if '/sets/' in url:
        #     pass
        # else:
            # print(f"{i}: {url}")
            
            # print(f"{i}: {last_part}")

            # print(f"{i}: {last_part}")
            # options = {
            #     'format': 'bestaudio/best',
            #     'outtmpl': rf'music/{last_part}.%(ext)s',
            # }

            # with YoutubeDL(options) as ydl:
            #     ydl.download(['https://soundcloud.com' + url + "\n"])

asyncio.run(main())