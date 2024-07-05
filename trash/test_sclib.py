from sclib import SoundcloudAPI, Track

api = SoundcloudAPI()
track = api.resolve('https://soundcloud.com/hyzrit/weird')

assert type(track) is Track

filename = f'./{track.artist} - {track.title}.mp3'

with open(filename, 'wb+') as file:
    track.write_mp3_to(file)
