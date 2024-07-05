from sclib import SoundcloudAPI, Track, Playlist
import time

filename2 = []
counter = 0
retries = 0
another_counter = 0
skip_tracks = 0


def download_track(track_url):
    global retries
    global another_counter
    global skip_tracks

    if skip_tracks <= 0:
        print(retries)
        api = SoundcloudAPI()
        track = api.resolve(track_url)  # No need for 'await'

        if not isinstance(track, Track):
            if retries <= 2:
                
                print("Не удалось распознать трек. Пожалуйста, проверьте URL.")
                retries += 1
                time.sleep(10)
                print(retries)
                return download_track(track_url)
            else:
                retries = 0
                return
        retries = 0

        filename = f"{track.artist} - {track.title}.mp3"

        # if skip_tracks <= 0:
        try:
            with open(filename, "wb+") as file:
                track.write_mp3_to(file)  # No need for 'await'
            another_counter += 1
            print(f"{another_counter}. Трек '{filename}' успешно скачан.")
        except Exception as e:
            another_counter += 1
            print(f"Произошла ошибка при скачивании трека: {e}")
    else:
        another_counter += 1
        skip_tracks -= 1
        return

if __name__ == "__main__":
    with open(r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\data.txt", 'r') as file:
        
        # каждая строчка с data.txt будет теперь отрабатывать for line in file кек
        for line in file:
            # print(line)
            # input()
            # time.sleep(1)
            # filename2.append(line.strip())
            # time.sleep(1)
            # print(filename2[counter])# выведет каждую строчку с data.txt
            filename2.append(line.strip())

            print(filename2[counter], "\nПопыток: ", retries)
            track_url = filename2[counter]
            download_track(track_url)
            counter += 1
    
    #with open("data.txt", "wb+") as file:

# import asyncio
# from sclib import SoundcloudAPI, Track, Playlist
# from sclib.asyncio import SoundCloudAPI as AsyncSoundCloudAPI  # Import async API

# import asyncio
# from sclib import Track, Playlist  # Keep these imports
# from sclib import AsyncSoundCloudAPI  # Corrected import

# import asyncio
# from sclib import SoundcloudAPI, Track, Playlist 

# filename2 = []
# counter = 0

# async def download_track(track_url):
#     api = SoundcloudAPI()  # Use the async API
#     try:
#         track = await api.resolve(track_url)  # Await resolution
#     except Exception as e:  # Catch potential errors during resolution
#         print(f"Error resolving track URL: {e}")
#         return

#     if not isinstance(track, Track):
#         print("Не удалось распознать трек. Пожалуйста, проверьте URL.")
#         return

#     filename = f"{track.artist} - {track.title}.mp3"

#     try:
#         with open(filename, "wb+") as file:
#             await track.write_mp3_to(file)  # Await download
#         print(f"Трек '{filename}' успешно скачан.")
#     except Exception as e:
#         print(f"Произошла ошибка при скачивании трека: {e}")

# async def main():
#     global counter  # Access the global counter variable
#     with open("data.txt", 'r') as file:
#         track_urls = [line.strip() for line in file]  # Read URLs into a list

#         # Create a list of tasks to run concurrently
#         tasks = [download_track(url) for url in track_urls]
#         await asyncio.gather(*tasks)  # Run all tasks concurrently

# if __name__ == "__main__":
#     asyncio.run(main())
