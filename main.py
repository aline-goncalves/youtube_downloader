import re
import urllib.request
import unicodedata
from pytubefix import *

def main():    
    yt = gettingUrl()    
    op = gettingDownloadOption()    
    title = gettingNormalizedTitle(yt)
    path = gettingPathToDownload(title)
    
    choosingDownload(op, yt, path, title)

def gettingUrl():
    return YouTube(input('Insert the video URL to download: '))

def gettingDownloadOption():
    return input('Choose the download option: \n 1- Download only video (mp4); \n 2- Download only audio (m4a); \n 3- Download only thumbnail (jpg); \n 4- Download all three. \n ')

def choosingDownload(op, yt, path, title):
    match op:
        case '1':
            downloadingVideo(yt, path)
            showingMessage(yt, '- video (mp4)')
        
        case '2':
            downloadingAudio(yt, path)
            showingMessage(yt, '- audio (m4a)')
        
        case '3': 
            downloadingThumbnail(yt, f"{path}/{title}")
            showingMessage(yt, '- thumbnail (jpg)')
            
        case _:
            downloadingAudio(yt, path)
            downloadingVideo(yt, path)
            downloadingThumbnail(yt, f"{path}/{title}")
            showingMessage(yt, '- video (mp4), audio (m4a) and thumbnail (jpg)')
            
def showingMessage(yt, op):
    print(f"Downloading ... {yt.title} {op}")
    
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