# work with chatgpt LMAO
import asyncio
import re
import os
import time

from playwright.async_api import async_playwright
from yt_dlp import YoutubeDL

class Main:
    def __init__(self):
        self.url = ''
        self.html = ""

    # chatgpt
    async def scrape_dynamic_page(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(self.url)

            last_height = await page.evaluate("document.body.scrollHeight")

            while True:
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

                await page.wait_for_timeout(1000)

                new_height = await page.evaluate("document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            html_content = await page.content()
            await browser.close()
            return html_content

    # little mine
    async def main(self, url, html):
        if not os.path.exists("config.txt"):
            print("write your url of likes musics from your web-browser, " +
            "should be looks like this: https://soundcloud.com/username/likes")
            self.url = input()
            self.html = await self.scrape_dynamic_page(self.url)
            print(self.html)
            # try-except, then open for a write
            with open("fully_loaded_page.html", 'w', encoding='utf-8') as file:
                file.write(self.html)

            # # try-except reading
            # with open("fully_loaded_page.html", 'r', encoding='utf-8') as file:
            #     html = file.read()
            # html = await scrape_dynamic_page(url)

            with open("config.txt", 'w', encoding='utf-8') as file:
                file.write(self.url)
        else:
            # try-except reading
            with open("config.txt", 'r', encoding='utf-8') as file:
                self.url = file.read()

            print("do you want to continue? with this url: " + self.url + "\n" +
            "1. yes\n" + 
            "2. no")
            choose = input()


            pattern = r'<a class="sound__coverArt" href="([^"]+)"'
            matches = re.findall(pattern, html)

            # if last_part
            directory_path = 'music'

            files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
            print("Файлы в директории:", files)

            # # check
            # with open("new_file.txt", 'w', encoding='utf-8') as file:
            #     file.write("")
            # for i, url in enumerate(matches, start=1):
            #     with open("new_file.txt", 'a', encoding='utf-8') as file:
            #         file.write(url + "\n")

            for i, url in enumerate(matches, start=1):
                last_part = url.split("/")[-1]
                # with open("new_file.txt", 'r', encoding='utf-8') as file:
                #     linkes = file.read()
                # print(linkes)
                # if files[i] == last_part

                # if files[i]:
                # for i in range(len(files)):
                print(i-1)


                # else:
                #     print("В директории нет файлов.")

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

if __name__ == "__main__":
    start = Main()
    asyncio.run(start.main())