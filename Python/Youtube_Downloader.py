import os
import tkinter as tk
from pytube import YouTube
from tkinter import *


root = tk.Tk()
root.title("Youtube Downloader!")
root.geometry("300x150")


def downloader(url):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    print("video downloaded")


button = tk.Button(root, text="Click to download!", command=lambda: downloader("https://youtu.be/tpLyWjg17kI"))
button.pack(side="bottom")

root.mainloop()
