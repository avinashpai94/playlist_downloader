# SYPlaylist Downloader

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://https://www.python.org/)

## SYPlaylist Downloader is a python based script to download mp3 versions of your favourite songs from a publicly available Spotify or YouTube playlist.

## Tech

SYPlaylist Downloader uses a number of open source projects to work properly:

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - To parse the playlists' contents and obtain links
[youtube_dl](https://github.com/ytdl-org/youtube-dl) - To download and rip the video from a valid YouTube url
[ffmpeg](https://ffmpeg.org/) - For AV manipulation of downloaded videos

And of course SYPlaylist Downloader itself is open source with a [public repository](https://github.com/avinashpai94/playlist_downloader) on GitHub.

## Installation

SYPlaylist requires FFMPEG to run on your system. You can download that for your system from [ffmpeg.org](https://ffmpeg.org/)

Steps to install FFMPEG will vary depending on your OS. Please make sure you have successfully installed FFMPEG before proceeding.

#### Linux
```
sudo apt update
sudo apt install ffmpeg
```
At this point you can run the below command to check if ffmpeg has been installed properly.
```
ffmpeg -version 
```

#### Windows
- Download a suitable Windows version of ffmpeg from [ffmpeg.org](https://ffmpeg.org/)
- Extract the zip file and copy the folder to destination directory
- Point System variable path to bin directory inside ffmpeg directory.
- At this point you can run the below command in command prompt to check if ffmpeg has been installed properly.
```
ffmpeg
```

#### Python Dependencies
Install the following python dependencies. 
| Dependency |
| ------ |
| BeautifulSoup |
| requests |
| urllib3 |
| youtube-dl |

Alternatively, you can also download the requirements.txt file from the repository and run 
``` 
pip install -r requirements.txt
```


## Usage
The script takes 1 argument, the url of the playlist to be downloaded. Only publicly available Spotify and YouTube playlists are currently supported.

Run as 
```
python syplaylist_downloader.py <playlist_url>
###Example###
python syplaylist_downloader.py https://www.youtube.com/playlist?list=PLpXA1IqBgeZQJetsVTviU8cZUBEa9sAc0
```

For doubts please contact on [GitHub](https://github.com/avinashpai94). 
