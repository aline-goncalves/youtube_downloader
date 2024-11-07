import re
import urllib.request
import unicodedata
from pytubefix import *

def main():
    yt = gettingUrl()
    showingMessage(yt)
    
    title = gettingNormalizedTitle(yt)
    path = gettingPathToDownload(title)
    
    downloadingAudio(yt, path)
    downloadingVideo(yt, path)
    downloadingThumbnail(yt, f"{path}/{title}")

def gettingUrl():
    return YouTube(input('Insert the video URL to download: '))

def showingMessage(yt):
    print(f"Downloading ... {yt.title}")
    
def downloadingVideo(yt, path):
    video = yt.streams.get_highest_resolution()
    video.download(f"download/{path}")

def downloadingAudio(yt, path):
    audio = yt.streams.get_audio_only()
    audio.download(f"download/{path}")
    
def downloadingThumbnail(yt, path):
    urllib.request.urlretrieve(yt.thumbnail_url, f"download/{path}.jpg")

def gettingNormalizedTitle(yt):
    return unicodedata.normalize('NFKD', yt.title)
    
def gettingPathToDownload(title):
    return re.sub('[^A-Za-z0-9 ]+', '', title)

main()