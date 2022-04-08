import cv2
import os
import ffmpy3
startstr = "0:10"
endstr = "1:18"

#批量截取MP4两个时间之间的图片，-r 1 按一秒一截取，-r 24一秒24帧

file = "./video/SourceVideo.mp4"

start1 = int(startstr.split(":")[0])
start2 = int(startstr.split(":")[1])

end1 = int(endstr.split(":")[0])
end2 = int(endstr.split(":")[1])
#print(start1,start2,end1,end2)

flag1=0
flag2=0

def oneClickScreenShot(flag1, flag2):
     os.system("ffmpeg -ss "+ str(flag1)+':' +str(flag2) +  " -i \"" +file+ "\" -f image2 -r 2 -t 00:01 ./input/fromvideo/"+ str(flag1)+'min' +str(flag2) +"%3d.jpg")
     print(flag1,flag2)

def screenshotter(start1,start2):
    while start1 <= end1:
        if start1 == end1:
            if start2 ==end2:
                # exit()
                break
            else:
                while start2 < end2:
                    oneClickScreenShot(start1, start2)
                    start2 += 1
        else:
            if start2 == 60:
                start2=0
                start1+=1
                oneClickScreenShot(start1, start2)
            else:
                while start2 < 60:
                    oneClickScreenShot(start1, start2)
                    start2 += 1

