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
        self.running = True

    async def fetch_dynamic_html(self, url, step=100, delay=0.1):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await (await browser.new_context()).new_page()
            await page.goto(url, wait_until="domcontentloaded")
            while True:
                previous_height = await page.evaluate("window.scrollY + window.innerHeight")
                await page.evaluate(f"window.scrollBy(0, {step})")
                await asyncio.sleep(delay)
                current_height = await page.evaluate("window.scrollY + window.innerHeight")
                if current_height >= await page.evaluate("document.body.scrollHeight") or current_height == previous_height:
                    break
            html = await page.content()
            await browser.close()
            return html

    async def main(self):
        while self.running:
            # if os.path.exists("config.txt"):
            #     with open("config.txt", 'r', encoding='utf-8') as file:
            #         self.url = file.read()

            #     print("Do you want to continue?\n" +
            #             "with this url: " + self.url + "\n" +
            #             "1. yes\n" + 
            #             "2. no")

            if not os.path.exists("config.txt"):
                print("Write your url like this \"https://soundcloud.com/username*/likes\"\n" +
                    "Which is from likes:")

                self.url = input()
                print("Hold on, it takes a lot of times if you have a lot of musics from your\n" +
                      "account")

                self.html = await self.scrape_dynamic_page(self.url)

                with open("fully_loaded_page.html", 'w', encoding='utf-8') as file:
                    file.write(self.html)

                with open("config.txt", 'w', encoding='utf-8') as file:
                    file.write(self.url)

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




            
                

                
            # if(int(input()) == 1):


            #     pattern = r'<a class="sound__coverArt" href="([^"]+)"'
            #     matches = re.findall(pattern, self.html)

            #     directory_path = 'music'


            #     for i, url in enumerate(matches, start=1):
            #         last_part = url.split("/")[-1]
            #         print(i-1)
            # else:
            #     os.remove("config.txt")
            #     pass

if __name__ == "__main__":
    start = Main()
    asyncio.run(start.main())