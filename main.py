import time

import pyperclip
import win32api
import win32gui

import PIL.ImageGrab
import cv2
import numpy as np
import pydirectinput
import pyautogui


class LeagueAuto:

    def __init__(self):

        self.count = 0
        self.in_danger = 0
        self.s_state = ''
        self.order = ''

    def mouse_in(self, type, x, y):

        try:

            if type == 'left':

                pydirectinput.mouseDown(x, y, 'left')
                time.sleep(0.1)
                pydirectinput.mouseUp(x, y, 'left')
                time.sleep(0.1)
            elif type == 'right':

                pydirectinput.mouseDown(x, y, 'right')
                time.sleep(0.3)
                pydirectinput.mouseUp(x, y, 'right')
                time.sleep(0.3)
            elif type == 'eye':

                pydirectinput.moveTo(x, y)
                time.sleep(0.5)
                pydirectinput.press('4')
        except:

            print("Restart this project with admin mode, failed to use the mouse.")

    def paste(self):

        pydirectinput.keyDown('ctrl')
        pydirectinput.keyDown('v')
        time.sleep(0.1)
        pydirectinput.keyUp('v')
        pydirectinput.keyUp('ctrl')

    def pic(self, template, type):

        try:

            img = pyautogui.screenshot(region=[0, 0, 2240, 1400])
            # img = PIL.ImageGrab.grab(bbox=(0, 0, 2240, 1400)) #(0, 0, 2240, 1400 )

            img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            temp = cv2.imread(template,0)
            w, h = temp.shape[::-1]

            res = cv2.matchTemplate(img1, temp, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.83)
            for pos in zip(*loc[::-1]):

                bottom_right = (pos[0] + w, pos[1] + h)
                cv2.rectangle(img, pos, bottom_right, (0, 0, 255), 2)
            if pos[0] and pos[1]:

                if type == 1:

                    pydirectinput.leftClick(pos[0]+int(w/2),pos[1]+int(h/2))
                    time.sleep(0.5)
                elif type == 2:

                    pydirectinput.rightClick(pos[0] + int(w / 2), pos[1] + int(h / 2))
                    time.sleep(0.5)

                elif type == 3:

                    cv2.imshow('i',img)
                    cv2.waitKey(0)
                else:

                    print("Found it and Keep waiting")
                    # this above is used for detect flag.

                return pos[0], pos[1], 1
            else:

                print("Object does not exist.")
                return 9, 9, 0
        except:

            print("Object does not exist.")
            return 9, 9, 0

    def client_move(self, type):
        win_client = "League of Legends"
        client = win32gui.FindWindow(None, win_client)
        gameName = "League of Legends (TM) Client"
        game = win32gui.FindWindow(None, gameName)
        if client:

            print("Client has been found.")
            a = self.pic(self,'IMGS/CLIENT/PLAY.PNG', 1)
            if a[2] != 1:

                self.pic(self, 'IMGS/CLIENT/PLAY_ED.PNG', 1)
            if type == 'train':

                t = self.pic(self, 'IMGS/CLIENT/TRAIN.PNG', 1)
                if t[2] != 1:

                    self.pic(self, 'IMGS/CLIENT/TRAIN_ED.PNG', 1)
                    time.sleep(1)
                tt = self.pic(self, 'IMGS/CLIENT/SEL_TRAIN.PNG', 1)
                if tt[2] != 1:

                    self.pic(self, 'IMGS/CLIENT/SEL_TRAIN_ED.PNG', 1)
            else:
                b = self.pic(self,'IMGS/CLIENT/VSBOT.PNG', 1)
                if b[2] != 1:

                    self.pic(self, 'IMGS/CLIENT/BOT_ED.PNG', 1)
                c = self.pic(self,'IMGS/CLIENT/FOOL.PNG', 1)
                if c[2] != 1:

                    self.pic(self,'IMGS/CLIENT/NULL.PNG', 1)
            time.sleep(1)
            d = self.pic(self, 'IMGS/CLIENT/CONFIRM.PNG', 1)
            if d[2] != 1:

                while d[2] != 1:

                    print("Not Found -1")
                    d = self.pic(self, 'IMGS/CLIENT/CONFIRM.PNG', 1)
                    time.sleep(1)
                print("Found -1")
            time.sleep(1)
            aa = self.pic(self, 'IMGS/CLIENT/ROOMED.PNG', 0)
            if aa[2] != 1:

                self.pic(self, 'IMGS/CLIENT/CONFIRM.PNG', 1)
            if type == 'train':
                start = self.pic(self, 'IMGS/CLIENT/START.PNG', 1)
                if start[2] != 1:

                    while start[2] != 1:

                        start = self.pic(self, 'IMGS/CLIENT/START_ED.PNG', 1)
                        time.sleep(1)
            else:
                e = self.pic(self, 'IMGS/CLIENT/FIND.PNG', 1)
                if e[2] != 1:

                    while e[2] != 1:

                        print("Not Found 0")
                        e = self.pic(self, 'IMGS/CLIENT/FIND.PNG', 1)
                        time.sleep(1)
                    print("Found 0")
                f = self.pic(self, 'IMGS/CLIENT/FUND.PNG', 0)
                if f[2] != 1:

                    while f[2] != 1:

                        print("Not Found 1")
                        f = self.pic(self, 'IMGS/CLIENT/FUND.PNG', 0)
                        time.sleep(1)
                    print("Found 1")
                time.sleep(1)
                g = self.pic(self, 'IMGS/CLIENT/YES.PNG', 1)
                if g[2] != 1:

                    while g[2] != 1:

                        print("Not Found 2")
                        g = self.pic(self, 'IMGS/CLIENT/YES.PNG', 1)
                        time.sleep(1)
                    print("Found 2")
                time.sleep(1)
            h = self.pic(self, 'IMGS/CLIENT/SEARCH.PNG', 1)
            if h[2] != 1:

                while h[2] != 1:

                    print("Not Found 3")
                    h = self.pic(self, 'IMGS/CLIENT/SEARCH.PNG', 1)
                    time.sleep(1)
                print("Found 3")
            time.sleep(1)
            pyperclip.copy('无极剑圣')
            self.paste(self)
            time.sleep(1)
            i = self.pic(self, 'IMGS/CLIENT/YI.PNG', 1)
            if i[2] != 1:

                while i[2] != 1:

                    print("Not Found 4")
                    i = self.pic(self, 'IMGS/CLIENT/SEARCH.PNG', 1)
                    time.sleep(1)
                print("Found 4")
            time.sleep(1)
            self.pic(self, 'IMGS/CLIENT/LOCK.PNG', 1)
            print("Game is going to start.")
            if game != True:

                while game == False:

                    print("Waiting for game.")
                    time.sleep(1)

            if type != "train":

                loads = self.load(self)
                if loads != 1:

                    while loads != 1:

                        loads = self.load(self)
                        # time.sleep(0.1)
                self.game_move(self, 'mid')
            else:

                # time.sleep(18)
                self.game_move(self, 'mid')
                if (game != True):

                    time.sleep(15)
                    self.game_move(self, 'mid')

        else:

            print("No client")

    def load(self):

        gameName = "League of Legends (TM) Client"
        game = win32gui.FindWindow(None, gameName)
        if game:

            print("Game has been opened in load")
            ld = self.pic(self, 'IMGS/INGAME/LOADING.PNG', 0)
            if ld[2] != 1:

                while ld[2] != 1:

                    print("Loading...1 starts")
                    ld = self.pic(self, 'IMGS/INGAME/LOADING.PNG', 0)
                    # time.sleep(0.1)
                print("Loading...1 over")
                while ld[2] == 1:

                    print("Loading...2 starts")
                    ld = self.pic(self, 'IMGS/INGAME/LOADING.PNG', 0)
                    # time.sleep(0.1)
                print("Loading...2 over")
            print("Load over")
            return 1
        else:

            return 0

    def game_finish(self):

        gameName = "League of Legends (TM) Client"
        game = win32gui.FindWindow(None, gameName)
        if game:

            end = self.pic(self, 'IMGS/INGAME/OVER.PNG', 0)
            if end[2] != 1:

                while end[2] != 1:

                    print("Over-ing...")
                    end = self.pic(self, 'IMGS/INGAME/OVER.PNG', 0)
                    time.sleep(1)
                print("Over-ed")
            time.sleep(1)
            quex = self.pic(self, 'IMGS/CLIENT/EXITT.PNG', 1)
            if quex[2] != 1:

                while quex[2] != 1:

                    print("Over-ing...")
                    quex = self.pic(self, 'IMGS/CLIENT/EXITT.PNG', 1)
                    time.sleep(1)
                print("Over-ed")
            time.sleep(1)
            self.count += 1
            print("Step Over :",self.count)

    def game_move(self, way):

        gameName = "League of Legends (TM) Client"
        game = win32gui.FindWindow(None, gameName)
        if game:

            print("Game has been found. Loading...")

            a = self.pic(self,'IMGS/INGAME/LOADINGss.PNG', 0)
            while a[2] == 1:
                print("Game Loading...")
                a = self.pic(self, 'IMGS/INGAME/LOADINGss.PNG', 0)
                time.sleep(0.1)
            print("Game Loaded")
            home = self.pic(self,'IMGS/INGAME/HOME.PNG', 0)
            if home[2] != 1:

                while home[2] != 1:

                    home = self.pic(self,'IMGS/INGAME/HOME.PNG', 0)
                    time.sleep(1)
            print("Script is ready for game.")
            time.sleep(4)
            if way == 'top':

                print("Go up")
                up = self.pic(self,'IMGS/INGAME/BTOPT.PNG', 2)
                if up[2] != 1:

                    while up[2] != 1:
                        up = self.pic(self, 'IMGS/INGAME/BTOPT.PNG', 0)
                        time.sleep(1)
                else:

                    self.pic(self, 'IMGS/INGAME/BTOPT.PNG', 2)

            elif way == 'mid':
                print("Go mid")
                mid = self.pic(self, 'IMGS/INGAME/BMIDT.PNG', 2)
                if mid[2] != 1:

                    while mid[2] != 1:
                        mid = self.pic(self, 'IMGS/INGAME/BMIDT.PNG', 0)
                        time.sleep(1)
                else:

                    self.pic(self, 'IMGS/INGAME/BMIDT.PNG', 2)

            elif way == 'down':
                print("Go down")
                dwn = self.pic(self, 'IMGS/INGAME/BDWNT.PNG', 2)
                if dwn[2] != 1:

                    while dwn[2] != 1:
                        dwn = self.pic(self, 'IMGS/INGAME/BDWNT.PNG', 0)
                        time.sleep(1)
                else:

                    self.pic(self, 'IMGS/INGAME/BDWNT.PNG', 2)

            # elif way == 'jungle':
            #     print("Go wild")
            #     jung = self.pic(self,'IMGS/INGAME/BTOPT.PNG', 0)








        else:

            print("No Game")

    def minds(self, mouse_need, order, s_state, lvl, x=None, y=None):

        if mouse_need == 1:

            if s_state == 'q_n':

                if lvl == 1:
                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'w_n':

                if lvl == 2:
                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'e_n':

                if lvl == 3:
                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'r_n':

                if lvl == 6:
                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'q_ugd':

                if lvl == 4:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
                else:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'w_ugd':

                if lvl == 5:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
                else:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'e_ugd':

                if lvl == 7:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
                else:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            elif s_state == 'r_ugd':

                if lvl == 11:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
                else:

                    self.ctrl.mouseDown(x, y, 'left')
                    self.tm.sleep(0.1)
                    self.ctrl.mouseUp(x, y, 'left')
            else:

                print("No this s_state")

            if order == 'q' | s_state == 'q_able':

                self.ctrl.mouseDown(x, y, 'q')
                self.tm.sleep(0.1)
                self.ctrl.mouseUp(x, y, 'q')
            else:

                print("No this order")


        else:

            if order == 'w' | s_state == 'w_able':

                self.ctrl.press('w')
                self.tm.sleep(0.1)
            elif order == 'e' | s_state == 'e_able':

                self.ctrl.press('e')
                self.tm.sleep(0.1)
            elif order == 'r' | s_state == 'r_able':

                self.ctrl.press('r')
                self.tm.sleep(0.1)
            elif order == 'd':

                self.ctrl.press('d')
                self.tm.sleep(0.1)
            elif order == 'f':

                self.ctrl.press('f')
                self.tm.sleep(0.1)
            elif order == 'b':

                self.ctrl.press('b')
                self.tm.sleep(0.1)
            else:
                print("No this order")

    # def frog(self):
    #
    #     global flag
    #     print("frog starts")
    #     self.mouse_in('right', x + 47, y + 775)  # 前进
    #     time.sleep(25)
    #     self.pic(self, '.IMGS/JUNGLES/FROG.png', 2)
    #     self.mouse_in('eye', x + 723, y + 500)  # Eyes got
    #     self.mouse_in('right', x + 723, y + 500)  # Attack
    #     pydirectinput.press('q')
    #     time.sleep(7)
    #     self.mouse_in('right', int((w / 2) + 10), int((h / 2) - 20))  # Attack
    #     pydirectinput.press('q')
    #     time.sleep(7)
    #     pydirectinput.keyDown('ctrl')
    #     pydirectinput.keyDown('w')
    #     pydirectinput.keyUp('ctrl')
    #     pydirectinput.keyUp('w')
    #     pydirectinput.press('f')
    #     time.sleep(2)
    #     pydirectinput.press('w')
    #     time.sleep(4)
    #     print("frog finished")


def jungle_clean(obj):
    if obj == 1:
        pass
    elif obj == 2:
        pass
    elif obj == 3:
        pass
    elif obj == 4:
        pass
    elif obj == 5:
        pass
    elif obj == 6:
        pass

gametitle = "League of Legends (TM) Client"
clienttitle = "League of Legends"
if __name__ == '__main__':

    main = LeagueAuto
    main.client_move(main, 'train')
    main.game_move(main, 'mid')



