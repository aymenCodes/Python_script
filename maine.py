#!/usr/bin/python3

"""
=========================================================
====                                                 ====
==== By Aymen benchiheub                             ====
==== my twitter: https://twitter.com/BenchiheubAymen ====
==== my gmail : benchiheub.aymen@gmail.com           ====                                                ====
=========================================================
"""
import urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube

class download():
    def start_download(self,url,video_type,place):
        url_open = urllib.request.urlopen(url)
        url_open = url_open.read(50000)
        soup = BeautifulSoup(url_open,"html.parser")
        title = soup.html.head.title.text
        title = title.replace(" - YouTube","")
        yt = YouTube(url)
        yt.set_filename(title)
        video = yt.get('mp4', video_type)
        video.download(place)
