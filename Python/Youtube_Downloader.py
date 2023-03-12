import os
from pytube import YouTube


def downloader(url):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    print("video downloaded")


downloader("https://youtu.be/I7cajVnzm8k")
