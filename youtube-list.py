import urllib2
import urlparse
#import shutil
import sys
#from __future__ import print_function
import re

if len(sys.argv) == 1: 
    print "Usage: python youtube-dl.py YOUTUBE_PLAYLIST_URL"
    exit (-1)


#print sys.argv
#for arg in sys.argv:
#    print arg


playlist = "https://www.youtube.com/playlist?list=PLkIselvEzpM6pZ76FD3NoCvvgkj_p-dE8"
playlist = "http://jsp.6connexchina.com/playlist.htm"
playlist = sys.argv[1]

print playlist
#a = "https://www.youtube.com/watch?v=ETvkf5a5rUo&index=4&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF"
#a = "https://www.youtube.com/watch?v=DNIauUrRIEM&list=PLkIselvEzpM7Pjo94m1e7J5jkIZkbQAl4"

#a = sys.argv[1]

resp = urllib2.urlopen(playlist)
data = resp.read()

#print data

#pattern = re.compile('<tr class="pl-video yt-uix-tile " data-video-id="(.*?)" data-set-video-id')

# search the line which contains the video id and the title
# <tr class="pl-video yt-uix-tile " data-video-id="Pxhp1OhEZFc" data-set-video-id="" data-title="kmeansClustering">
pattern = re.compile('<tr class="pl-video yt-uix-tile ".*?>')
items = re.findall(pattern, data)



for item in items:
    print item
    pattern = re.compile('data-video-id="(.*?)"')
    print re.search(pattern, item).group()
    print re.search(pattern, item).group(0)
    print re.search(pattern, item).group(1)
    #print pattern.search(item).group()

    pattern = re.compile('data-title="(.*?)"')
    print re.search(pattern, item).group()
    print re.search(pattern, item).group(0)
    print re.search(pattern, item).group(1)
    #print pattern.search(item).group()


