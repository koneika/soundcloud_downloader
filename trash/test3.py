# import requests

# url = 'https://rr1---sn-a5msen7z.googlevideo.com/videoplayback?expire=1715304482&ei=wiM9ZtDdLKPS1sQPr56mgAQ&ip=181.64.92.40&id=o-AJDD9Cu7qunq5G-t1ZqWE651mKiXWXdnhRPlAVCxFTE7&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AWRWj2Q4SW2pTNCk5SfcZo4M3GyzsmGeZKuAQaH3a4ZJNFj8yiSdSkiShV72WLVXJcZuT3AueVb2Qbx1&spc=UWF9fzJvNAKt54qnWQdYb5j_fNFk7FiEAPbLh070DT6P98Vlevyrl-MLpWm3&vprv=1&svpuc=1&mime=video%2Fmp4&ns=M_LpQjoHrtLCQ3ZiThxRKnwQ&rqh=1&gir=yes&clen=27488670&ratebypass=yes&dur=785.832&lmt=1714806849165247&c=WEB&sefc=1&txp=5538434&n=bX6iF1kvT7pveg&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAMbZEjvwSMdRa8vRGnvFZrNJHcu3bwWoNjqCTLGe6LgfAiA7GgTNe4wCRnyHWLFf77TxfYiAJJm5A2jzCg8RYYY7aQ%3D%3D&title=%D0%92%D0%9E%D0%A2%20%D0%9F%D0%9E%D0%A7%D0%95%D0%9C%D0%A3%20%D0%A2%D0%AB%20%D0%91%D0%A0%D0%9E%D0%A1%D0%98%D0%A8%D0%AC%20%D0%9F%D0%A0%D0%9E%D0%93%D0%A0%D0%90%D0%9C%D0%9C%D0%98%D0%A0%D0%9E%D0%92%D0%90%D0%9D%D0%98%D0%95!%20%D0%A2%D0%B2%D0%BE%D0%B8%20%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8.&rm=sn-uqx2-aphzl7l&req_id=d4233e4387e6a3ee&redirect_counter=2&cm2rm=sn-njaey7e&cms_redirect=yes&cmsv=e&mh=f0&mip=85.118.74.72&mm=34&mn=sn-a5msen7z&ms=ltu&mt=1715282097&mv=D&mvi=1&pl=0&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AHWaYeowRAIgK3ouPdZztM3WIf2GZftw-PFx3cZxRvviTSNyMP8NBGYCIDUiurCM-70FG1iUg0_22UTojnJ3FmUctk3chIHY4CeK'
# file_name = 'video.mp4'

# response = requests.get(url)
# with open(file_name, 'wb') as f:
#     f.write(response.content)

# import pafy

# url = 'https://www.youtube.com/watch?v=D6rI19iUXHs'
# video = pafy.new(url)
# best_audio = video.getbestaudio()
# best_audio.download(filepath='audio.mp3')

# import requests
# from bs4 import BeautifulSoup

# # URL страницы с медиафайлом
# url = 'https://rr1---sn-a5msen7z.googlevideo.com/videoplayback?expire=1715304482&ei=wiM9ZtDdLKPS1sQPr56mgAQ&ip=181.64.92.40&id=o-AJDD9Cu7qunq5G-t1ZqWE651mKiXWXdnhRPlAVCxFTE7&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AWRWj2Q4SW2pTNCk5SfcZo4M3GyzsmGeZKuAQaH3a4ZJNFj8yiSdSkiShV72WLVXJcZuT3AueVb2Qbx1&spc=UWF9fzJvNAKt54qnWQdYb5j_fNFk7FiEAPbLh070DT6P98Vlevyrl-MLpWm3&vprv=1&svpuc=1&mime=video%2Fmp4&ns=M_LpQjoHrtLCQ3ZiThxRKnwQ&rqh=1&gir=yes&clen=27488670&ratebypass=yes&dur=785.832&lmt=1714806849165247&c=WEB&sefc=1&txp=5538434&n=bX6iF1kvT7pveg&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAMbZEjvwSMdRa8vRGnvFZrNJHcu3bwWoNjqCTLGe6LgfAiA7GgTNe4wCRnyHWLFf77TxfYiAJJm5A2jzCg8RYYY7aQ%3D%3D&title=%D0%92%D0%9E%D0%A2%20%D0%9F%D0%9E%D0%A7%D0%95%D0%9C%D0%A3%20%D0%A2%D0%AB%20%D0%91%D0%A0%D0%9E%D0%A1%D0%98%D0%A8%D0%AC%20%D0%9F%D0%A0%D0%9E%D0%93%D0%A0%D0%90%D0%9C%D0%9C%D0%98%D0%A0%D0%9E%D0%92%D0%90%D0%9D%D0%98%D0%95!%20%D0%A2%D0%B2%D0%BE%D0%B8%20%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8.&rm=sn-uqx2-aphzl7l&req_id=d4233e4387e6a3ee&redirect_counter=2&cm2rm=sn-njaey7e&cms_redirect=yes&cmsv=e&mh=f0&mip=85.118.74.72&mm=34&mn=sn-a5msen7z&ms=ltu&mt=1715282097&mv=D&mvi=1&pl=0&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AHWaYeowRAIgK3ouPdZztM3WIf2GZftw-PFx3cZxRvviTSNyMP8NBGYCIDUiurCM-70FG1iUg0_22UTojnJ3FmUctk3chIHY4CeK'

# # Отправляем запрос на получение HTML-кода страницы
# response = requests.get(url)
# html = response.text

# # Создаем объект BeautifulSoup для анализа HTML
# soup = BeautifulSoup(html, 'html.parser')

# # Находим ссылку на медиафайл
# media_tag = soup.find('video')  # Например, для видео
# if media_tag:
#     media_url = media_tag['src']

from sclib import SoundcloudAPI, Track, Playlist

# do not pass a Soundcloud client ID that did not come from this library, but you can save a client_id that this lib found and reuse it
api = SoundcloudAPI()  
track = api.resolve('https://soundcloud.com/hyzrit/weird')

assert type(track) is Track

filename = f'./{track.artist} - {track.title}.mp3'

with open(filename, 'wb+') as file:
    track.write_mp3_to(file)