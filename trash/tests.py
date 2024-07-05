from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import requests

with open('page_code.html', 'r', encoding='utf-8') as file:
    page_source = file.read()

# with open('new_page_code.html', 'w', encoding='utf-8') as file:
#     file.write(page_source)
with open('data.txt', 'w', encoding='utf-8') as file:
    if f'<a class="sound__coverArt" href="' in page_source:
        print(-1)
        # Ваша строка с текстом
        # text = "Ваш текст до символа ?"

        # Ищем индекс символа "?"
        word_for_find = f'<a class="sound__coverArt" href="'
        index = page_source.find(word_for_find)
        i = 0
        counter = 0
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
                    index = page_source.find(word_for_find, index + len(word_for_find))
                    print(str(counter) + ". " + "https://soundcloud.com" + result)
                    file.write("https://soundcloud.com" + result + '\n')
            #     else if 
        
            
    else:
        print("Символ не найден в тексте.")

print("end")
input()
# print(page_source)


    # if 'h2' and 'a' and 'href' in tag.attrs:
    # # if tag.name:
    #     gg = f"{tag['href']}"
    #     print(f"{tag['href']}")


