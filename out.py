#ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4
import os
 
base = "/home/han/source/python/tsfiles"
fp = open("filelist.txt",'a+')

for i in range(0,1034):
    url = base + "/{0}.ts".format(i)
    out = "file '"+ url + "'" + "\n"
    fp.write(out)

fp.close()
