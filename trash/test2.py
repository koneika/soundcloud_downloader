import requests
from bs4 import BeautifulSoup

url = "https://soundcloud.com/hyzrit/weird"  # Замените на URL страницы с музыкой
soup = BeautifulSoup(requests.get(url).content, "lxml")

for link in soup.select("[data-url]"):
    audio_url = link["data-url"]
    print(f"Загрузка {audio_url}")
    with open(audio_url.split("/")[-1], "wb") as f_out:
        f_out.write(requests.get(audio_url).content)
