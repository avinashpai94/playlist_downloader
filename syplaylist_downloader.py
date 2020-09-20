from __future__ import unicode_literals

import getopt
import re
import sys
import urllib
from urllib.parse import urlparse

import requests
import youtube_dl
from bs4 import BeautifulSoup

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
}


def youtube_download(video_link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])


def youtube_playlist_downloader(url):
    html = urllib.request.urlopen(url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for video_id in video_ids:
        link = "https://www.youtube.com/watch?v=" + video_id
        youtube_download(link)


def spotify_playlist_downloader(url):
    playlist_url = url
    page = requests.get(playlist_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    track_selection = 'track-name'
    artist_selection = 'artists-albums'
    tracks = soup.find_all("span", class_=track_selection)
    artists = soup.find_all("span", class_=artist_selection)

    contents = []
    for track, artist in zip(tracks, artists):
        contents.append([track.text, artist.text])

    for line in contents:
        track, artist = line
        video_search = re.sub(r"\s+", " ", track)
        search_url = ('https://www.youtube.com/results?search_query={}&page=&utm_source=opensearch'.format(
        video_search.replace(' ', '+')))
        html = urllib.request.urlopen(search_url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = "https://www.youtube.com/watch?v=" + video_ids[0]
        youtube_download(link)


def main():
    try:
        url = sys.argv[1]
    except getopt.GetoptError:
        print("Run as 'python playlist_downloader.py <playlist_url>")
        sys.exit()
    parsed_uri = urlparse(url)
    if parsed_uri.netloc == "www.youtube.com":
        youtube_playlist_downloader(url)
    else:
        spotify_playlist_downloader(url)


if __name__ == '__main__':
    main()


