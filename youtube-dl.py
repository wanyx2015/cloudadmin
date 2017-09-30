import urllib2
import urllib
import urlparse
#import shutil
import sys
#from __future__ import print_function
import re
import socket
socket.setdefaulttimeout(300.0)


if len(sys.argv) == 1: print "Usage: python youtube-dl.py YOUTUBE_WATCH_URL"

print sys.argv
#for arg in sys.argv:
#    print arg


playlist = "https://www.youtube.com/playlist?list=PLkIselvEzpM6pZ76FD3NoCvvgkj_p-dE8"
a = "https://www.youtube.com/watch?v=ETvkf5a5rUo&index=4&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF"
a = "https://www.youtube.com/watch?v=DNIauUrRIEM&list=PLkIselvEzpM7Pjo94m1e7J5jkIZkbQAl4"

a = sys.argv[1]
fname = ""

if len(sys.argv) == 3: fname = sys.argv[2]

print "URL: " + a
pattern = re.compile('v=(.*?)&')
items = re.findall(pattern, a)
print items

if len(items) == 0:
    pattern = re.compile('v=(.*?)$')
    items = re.findall(pattern, a)
    print items

url = "https://www.youtube.com/get_video_info?video_id=" + items[0]

print url

#resp = urllib2.urlopen("https://www.youtube.com/get_video_info?video_id=ygyX7qnxXH4")
resp = urllib2.urlopen(url, timeout = 300)
data = resp.read()
#print data
info = urlparse.parse_qs(data)
title = info['title']
print title

if len(fname) == 0:
    fname = title[0] + ".mp4"
    fname = fname.replace('/', '-')
    print fname

stream_map = info['url_encoded_fmt_stream_map'][0] 
#print stream_map
print "______________________________________"
v_info = stream_map.split(",")

for video in v_info:
    print video
    print "************"
    item = urlparse.parse_qs(video)
    print item
    print "############" 
    if "video/mp4" in item['type'][0]:
        print item['type'][0]
        print item['quality'][0]
        url = item['url'][0]
        print "downloading..."
        print url
        
#        START DOWNLOADING NOW

#        urllib.urlretrieve(url, "./"+ fname);
#        break;
        
        
        resp = urllib2.urlopen(url, timeout = 300)
        print resp.headers
        size = int(resp.headers['Content-Length'])
        print size


        #fname = "Boeing FA-18 Hornet Anatomy of the FA-18 Hornet Fighter Attack Airplane.mp4"
        myfile = open("./" + fname, "w+")
        done = 0
        
        
        
        #new tets code
#        data = resp.read()
#        with open("./" + fname, "wb") as code:
#            code.write(data)
        
        
        chunk = 8*1024
#        
        buff = resp.read(chunk)
        while buff:
            myfile.write(buff)
            done += chunk
            percent = done * 100.0 / size
            #print str(percent) + "%" + '\r'
            sys.stdout.write( str(percent) + "% \r")
            buff = resp.read(chunk)


        #res2 = requests.get(url, stream=True)

        #f = open(fname, 'wb')
        #shutil.copyfileobj(res2.raw, f)
        #f.close()
        break

