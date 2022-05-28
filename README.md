# 英雄自动化 LeagueAuto 

这是一个免费的Python开源项目
This is an Open-source Python Project

## 安装环境 Install Environments before use it
 
pip install pydirectinput && pyperclip && pywin32 && numpy && pyautogui && opencv-python

Run the main.py with python IDE and the opened game client in chinese language.

## 环境说明 Environmental Introductions

pyautogui: grab the screenshot only !!!
pywin32 -> win32gui & win32api:get the Windowinfo（E.g. axis positions of four corners）
pydirectinput:Any mouse&keyboard movements in the Game !!!
numpy & opencv-python -> cv2: simply process the (arrays)pictures

## 功能简介 Function info
Champions： Master Yi

1. Automatic Movements in client to start a VS VERY EASY BOT game, the functions in game is unfinished and to be developing.
2. Automatic Movements in client to enter the training mode.

## 交流 Communications
I'm trying use CV2.TemplateMatch() to detect the related buttons and objects, but I'm very confused about the next function to realize about minions, monsters and champions detecting and attacking.
This source image of function can only input the gray one, so I'm gonna use pyautogui.locateOnScreen() to complete the unfinished behavious tree.

## 欢迎提供宝贵的意见和帮助 Join us(Although only I'm doing this project with low effective speed) 

## 更新日志 Update Logs
date  ver.  log
5.27  0.01  can enter the bot game without hand
5.28  0.02  can simply reach around the tower



