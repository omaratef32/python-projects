from asyncio import streams
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=F0fjYblUGDg')

stream = yt.streams.get_by_itag(18)

stream.download()