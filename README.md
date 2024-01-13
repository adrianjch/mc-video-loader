# mc-video-loader

This repository shows how to convert a video into dust particles in Minecraft.
Showcase (Bad Apple): https://www.youtube.com/watch?v=YDE2voX_v_E

The idea is that for every frame of the input video, an mcfunction is created, which will create the whole canvas of dust colored particles.
<br/>
At a resolution of 96x72 particles the video runs smoothly on my machine, if you are going to increase the resolution too much Minecraft could lag.
<br/>
The python code to create all the mcfunctions lasts about 20 minutes in my machine for all 6572 frames of Bad Apple.


# How to run this on my computer
- Download "McVideoLoader.py"
- You will need Python3 and pip installed on your machine
- Run "pip install opencv-python" on your command-line to install the only python dependency
- You can open "McVideoLoader.py" on any text file editor and change the density, outWidth and outHeight values to the ones you wish
- Add the video you wish to convert to the same folder as the python file and rename it to input.mp4
- Open the comand-line and run "py McVideoLoader.py". This will start generating all the frames in a new folder. You can see the progress in the command-line window

## I generated all the frames for my video, how do I run this on my Minecraft world?
You will have to create a datapack to run all those mcfunctions. If you don't know how to do that, I have provided an example datapack "ikunobu" in this repository, you can just download it and place it inside your ".minecraft/saves/{YourWorldName}/datapacks/" folder.
<br/>
You will need to place all your frames inside "ikunobu/data/functions/frames/". An init, reset and update mcfunctions were also created in the same file folder as your input.mp4, you shall place them inside "ikunobu/data/functions/".

With all that done, we are ready to open our Minecraft world! Make sure your world has cheats enabled, because we will need to run some commands.
- Type in the Minecraft chat: /function video:init
- From now on it's all command blocks, I recommend you check out the world I provide so you can look at them, but I will provide some screenshots to make this fast.

Make sure everything looks exactly like in the screenshots. You need to put correctly all the command blocks types and all the commands.
---
First command block. Power it with redstone to show the video. Removing its redstone will hide the video.
<br/>
Full command: execute at @e[tag=projector] run function video:update

![image](https://github.com/adrianjch/mc-video-loader/assets/36569774/a106f1be-e0f5-4d12-8df5-cdc5718bc305)
---
Second command block. Power it with redstone to play the video. Removing its redstone will pause the video.
<br/>
Full command: scoreboard players add frame variables 1

![image](https://github.com/adrianjch/mc-video-loader/assets/36569774/d2ed6727-3cc2-4ff4-b18f-ad359fb57e33)
---
Finally, we have to choose a place where the video will play. Create a command block where you want the video to play and execute it once. This will create an invisible armor stand with a special tag. You can remove the command block after you have executed it if you want to.
<br/>
Full command: execute positioned ~ ~6 ~ align xyz run summon armor_stand ~ ~ ~ {Tags:["projector"],Invisible:1}

![image](https://github.com/adrianjch/mc-video-loader/assets/36569774/36ca110f-dc0d-42d1-bcbb-7f1f496c7429)
<br/><br/>
To play the video from the beginning you can just type "/function video:reset"
<br/><br/>
To reproduce the video at the same rate as the original video you can use the tick rate function. If your video was at 30 fps, your command would be "/tick rate 30"
<br/><br/>
If all the particles causes too much lag, you can either reduce the amount of particles from the python code or slowmo the video by reducing the tick rate. For example "/tick rate 5"
<br/><br/>
If you want to remove these invisible armor stands that generate the particles positions you can type "/kill @e[tag=projector]". This action will remove the video.
<br/><br/>
If you want to remove all those spammy command block messages in the chat you can type "/gamerule commandBlockOutput false"
