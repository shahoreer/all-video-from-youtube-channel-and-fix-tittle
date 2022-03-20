from pytube import Channel
from pytube import YouTube
import os

def down():

    channel = Channel(input("Channel URL: "))

    start=int(input("Start: "))
    end=int(input("End: "))
    lengthlimit=int(input("Duration Limit: "))
    path=input("Download Path: ")

    for video in channel.video_urls[start-1 : end]:
        vd=YouTube(video)
        if vd.length<=lengthlimit:
            vd.streams.get_highest_resolution().download(path)
        else:
            print("over time limit : "+str(lengthlimit))


def givetitle():
    addafter="! Peter Griffin Comedy #tbcartoon.mp4"
    path=input("Path: ")
    os.chdir(path)
    for f in os.listdir():
        a,b=os.path.splitext(f)
        b=""
        a=a.split(" ")

        i=0
        j=len(a)

        while i<j:
            ck=a[i]
            if ck=="funny" or ck=="comedy" or ck=="familyguy" or ck.isdigit():
                i=j
            else:
                b+=" "+a[i]
                i+=1
        os.rename(f,path+"/"+b+addafter)

which=input("Which? (down/tittle)")

if which=="down":
    down()
elif which == "tittle":
    givetitle()