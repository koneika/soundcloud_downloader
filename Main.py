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
        self.choose = ""

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

    async def main(self):
        while self.running:
            if os.path.exists("fully_loaded_page.html"):
                with open("fully_loaded_page.html", 'r', encoding='utf-8') as file:
                    self.html = file.read()
            
            
            if os.path.exists("config.txt"):
                with open("config.txt", 'r', encoding='utf-8') as file:
                    self.url = file.read()

                print("Do you want to continue?\n" +
                        "with this url: " + self.url + "\n" +
                        "1. yes\n" + 
                        "2. no")
                self.choose = input()

            if(self.choose == "1" or not os.path.exists("config.txt")):
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
                # if(int(input()) == 1):
                pattern = r'<a class="sound__coverArt" href="([^"]+)"'
                matches = re.findall(pattern, self.html)

                directory_path = 'music'


                # for i, url in enumerate(matches, start=1):
                #     last_part = url.split("/")[-1]
                #     print(i-1)

                for i, url in enumerate(matches, start=1):
                    last_part = url.split("/")[-1]
                    
                    # with open("new_file.txt", 'r', encoding='utf-8') as file:
                    #     linkes = file.read()
                    # print(linkes)
                    # if files[i] == last_part

                    print(i-1)

                    if '/sets/' in url:
                        pass
                    else:
                        print(f"{i}: {url}")
                        
                        print(f"{i}: {last_part}")
                        print(f"{i}: {last_part}")
                        options = {
                            'format': 'bestaudio/best',
                            'outtmpl': rf'music/{last_part}.%(ext)s',
                        }
                        with YoutubeDL(options) as ydl:
                            ydl.download(['https://soundcloud.com' + url + "\n"])
                    self.running = False
            elif(self.choose == "2"):
                os.remove("config.txt")
                pass
                
            
            
if __name__ == "__main__":
    start = Main()
    asyncio.run(start.main())