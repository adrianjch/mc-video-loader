import cv2
import os

density = 5 # Amount of particles that fit in a block size
outWidth = 96 # Amount of particles on the X axis
outHeight = 72 # Amount of particles on the Y axis
videoName = "input.mp4"

def averageColor(frame, x1:int, y1:int, x2:int, y2:int):
    total = [0,0,0]
    count = 0
    for x in range(x1, x2):
        for y in range(y1, y2):
            total += frame[y][x]
            count += 1
    return total / count

def generateCommand(color, x, y):
    return "particle minecraft:dust {r:.2f} {g:.2f} {b:.2f} 1 ^{x:.2f} ^{y:.2f} ^0 0 0 0 0 1 force @a".format(r=color[0], g=color[1], b=color[2], x=x/density, y=y/density)

def generateUpdateFile(frameCount):
    command = ""
    for x in range(1, frameCount+1):
        command += "execute if score frame variables matches {} run function video:frames/{}".format(x,x)
        command += "\n"
    f = open("update.mcfunction", "w")
    f.write(command)
    f.close()
    
def generateInitFile():
    f = open("init.mcfunction", "w")
    f.write("scoreboard objectives add variables trigger\n")
    f.write("function video:reset")
    f.close()
    
def generateResetFile():
    f = open("reset.mcfunction", "w")
    f.write("scoreboard players set frame variables 1")
    f.close()

vid = cv2.VideoCapture(videoName)
inWidth = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
inHeight = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
scaleX = inWidth / outWidth
scaleY = inHeight / outHeight
frameId = 0
totalFrames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

# If 'frames' folder doesn't exist, create it
if not os.path.exists("frames"):
    os.makedirs("frames")
    
while True:
    ret, frame = vid.read()
    frameId = int(vid.get(cv2.CAP_PROP_POS_FRAMES))
    if not ret:
        break
    print("{}/{} ({:.2f}%)".format(frameId, totalFrames, frameId/totalFrames*100))
    command = ""
    y = 0
    while y < inHeight:
        x = 0
        while x < inWidth:
            color = averageColor(frame, int(x), int(y), int(x+scaleX), int(y+scaleY))
            command += generateCommand(color/255, x/scaleX, outHeight-y/scaleY)
            command += "\n"
            x += scaleX
        y += scaleY
    f = open("frames/"+str(frameId)+".mcfunction", "w")
    f.write(command)
    f.close()
vid.release()
generateUpdateFile(frameId)
generateInitFile()
generateResetFile()
