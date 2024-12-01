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
    async def main(self):
        if not os.path.exists("config.txt"):
            print("Write your url like this \"https://soundcloud.com/username*/likes\"\n" +
                  "Which is from likes:")

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

            print("Do you want to continue?\n" +
                  "with this url: " + self.url + "\n" +
                  "1. yes\n" + 
                  "2. no")
            if(int(input()) == 1):


                pattern = r'<a class="sound__coverArt" href="([^"]+)"'
                matches = re.findall(pattern, self.html)

                directory_path = 'music'

                files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
                print("Файлы в директории:", files)


                for i, url in enumerate(matches, start=1):
                    last_part = url.split("/")[-1]
                    print(i-1)
            else:
                with open("config.txt", 'w', encoding='utf-8') as file:
                    file.write("")
                return

if __name__ == "__main__":
    start = Main()
    asyncio.run(start.main())