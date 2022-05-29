#######################
# import
#######################
import time
import pyperclip
import win32api
import win32gui
import PIL.ImageGrab
import cv2
import numpy as np
import pydirectinput
import pyautogui
#######################

class LeagueAuto:

    def __init__(self):

        self.lvl = 0
        self.count = 0
        self.in_danger = 0
        self.s_state = ''
        self.order = ''
        self.q = 0
        self.w = 0
        self.e = 0
        self.r = 0

########################################
#       MouseEvent Controller
# Leftclick, Rightclick and EyePutting
########################################
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
#######################################
#   Paste KeyboardEvent
#######################################
    def paste(self):

        pydirectinput.keyDown('ctrl')
        pydirectinput.keyDown('v')
        time.sleep(0.1)
        pydirectinput.keyUp('v')
        pydirectinput.keyUp('ctrl')

#######################################
#   TemplateMatch Function
#   Input template and all screenshot
#   It then match the picture ,
#   Type 0 for only detect
#   Type 1 for Leftclick after detect
#   Type 2 for Rightclick after detect
#   Type 3 for Imshow the result after detect
#   Return 1 for success
#   Return 0 for failure
#   when pos[0],pos[1] = 9,9 ,
#   It shows no matchable img
#######################################
    def pic(self, template, type):

        try:
            # It seems that ImageGrab is slower than screenshot.
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
###############################################################################
#   Client MouseEvent to Start a Bot Game with automation
#   Added some accidental situations, so the code is a bit long.
#   VSBOT, RECONNECT, TRAINING three modes are supported.
###############################################################################
        def client_move(self, type):
        win_client = "League of Legends"
        client = win32gui.FindWindow(None, win_client)
        gameName = "League of Legends (TM) Client"
        game = win32gui.FindWindow(None, gameName)
        if client:

            print("Client has been found.")

            if type == 'recon':

                re = self.pic(self, 'IMGS/CLIENT/RECON.PNG', 1)
                if re[2] != 1:
                    re = self.pic(self, 'IMGS/CLIENT/RECON.PNG', 1)
                game = win32gui.FindWindow(None, gameName)
                if not game:
                    while game == False:

                        print("Waiting for game.")
                        time.sleep(1)
                        game = win32gui.FindWindow(None, gameName)
                self.game_move(self, 'jungle')
            elif type == 'train':

                a = self.pic(self, 'IMGS/CLIENT/PLAY.PNG', 1)
                if a[2] != 1:

                    self.pic(self, 'IMGS/CLIENT/PLAY_ED.PNG', 1)
                a = self.pic(self, 'IMGS/CLIENT/PLAY.PNG', 1)
                if a[2] != 1:
                    self.pic(self, 'IMGS/CLIENT/PLAY_ED.PNG', 1)
                t = self.pic(self, 'IMGS/CLIENT/TRAIN.PNG', 1)
                if t[2] != 1:

                    self.pic(self, 'IMGS/CLIENT/TRAIN_ED.PNG', 1)
                    time.sleep(1)
                tt = self.pic(self, 'IMGS/CLIENT/SEL_TRAIN.PNG', 1)
                if tt[2] != 1:

                    self.pic(self, 'IMGS/CLIENT/SEL_TRAIN_ED.PNG', 1)
            else:

                a = self.pic(self, 'IMGS/CLIENT/PLAY.PNG', 1)
                if a[2] != 1:
                    self.pic(self, 'IMGS/CLIENT/PLAY_ED.PNG', 1)
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
                    game = win32gui.FindWindow(None, gameName)

                self.game_move(self, 'jungle')

            if type != "train":

                loads = self.load(self)
                if loads != 1:

                    while loads != 1:

                        loads = self.load(self)
                        # time.sleep(0.1)
                self.game_move(self, 'jungle')
            else:

                # time.sleep(18)
                self.game_move(self, 'jungle')
                if (game != True):

                    time.sleep(15)
                    self.game_move(self, 'jungle')

        else:

            print("No client")
############################################
#   Press B to go home.
############################################
    def home_tele(self):

        print("start go home with teleport")
        pydirectinput.press('b')
        home = self.pic(self, 'IMGS/INGAME/HOME.PNG', 0)
        if home[2] != 1:

            for pach in range(1,9):
                home = self.pic(self, 'IMGS/INGAME/HOME.PNG', 0)
                time.sleep(1)
                if home[2] == 1:
                    print("Got home")
                    break
                if pach == 9:
                    if home[2] != 1:
                        print("Failed")
                        self.home_tele(self)
###############################################################################
#   Loading Detection
#   
###############################################################################
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
###############################################################################
#   Close the Room after winning
#   
###############################################################################
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
###############################################################################
#   Provide skill flags to the minds() function.
#   State Flags of level and skill 
###############################################################################
    def skills(self, order):

        self.__init__(self)

        for lvl in ['IMGS/SKILLS/LVL/L1.PNG',
                    'IMGS/SKILLS/LVL/L2.PNG',
                    'IMGS/SKILLS/LVL/L3.PNG',
                    'IMGS/SKILLS/LVL/L4.PNG',
                    'IMGS/SKILLS/LVL/L5.PNG',
                    'IMGS/SKILLS/LVL/L6.PNG']:

            l1 = self.pic(self, lvl, 0)
            if l1 == 1:
                    self.lvl == 1
            l2 = self.pic(self, lvl, 0)
            if l2 == 1:
                    self.lvl == 2
            l3 = self.pic(self, lvl, 0)
            if l3 == 1:
                    self.lvl == 3
            l4 = self.pic(self, lvl, 0)
            if l4 == 1:
                    self.lvl == 4
            l5 = self.pic(self, lvl, 0)
            if l5 == 1:
                    self.lvl == 5
            l6 = self.pic(self, lvl, 0)
            if l6 == 1:
                    self.lvl == 6

        for stl in ['IMGS/SKILLS/Q.PNG',
                    'IMGS/SKILLS/W.PNG',
                    'IMGS/SKILLS/E.PNG',
                    'IMGS/SKILLS/R.PNG']:

            q = self.pic(self, stl, 0)
            if q == 1:

                self.q = 1
            else:

                self.q = 0
            w = self.pic(self, stl, 0)
            if w == 1:

                self.w = 1
            else:

                self.w = 0
            e = self.pic(self, stl, 0)
            if e == 1:

                self.e = 1
            else:

                self.e = 0
            r = self.pic(self, stl, 0)
            if r == 1:

                self.r = 1
            else:

                self.r = 0

            q = self.pic(self, "/IMGS/SKILLS/Q_N.PNG", 0)
            if q[2] == 1:

                s_state = 'q_n'
            w = self.pic(self, "/IMGS/SKILLS/W_N.PNG", 0)
            if w[2] == 1:

                s_state = 'w_n'
            e = self.pic(self, "/IMGS/SKILLS/E_N.PNG", 0)
            if e[2] == 1:

                s_state = 'e_n'
            r = self.pic(self, "/IMGS/SKILLS/R_N.PNG", 0)
            if r[2] == 1:

                s_state = 'r_n'

            q_u = self.pic(self, "/IMGS/SKILLS/UGD/q_ugd.PNG", 0)
            if q_u[2] == 1:

                s_state = 'q_ugd'
            w_u = self.pic(self, "/IMGS/SKILLS/UGD/w_ugd.PNG", 0)
            if w_u[2] == 1:

                s_state = 'w_ugd'

            e_u = self.pic(self, "/IMGS/SKILLS/UGD/e_ugd.PNG", 0)
            if e_u[2] == 1:

                s_state = 'e_ugd'

            if self.lvl >= 7 and self.lvl != 11:

                s_state = random.randrange('q_ugd','w_ugd','e_ugd','r_ugd',1)
            elif self.lvl == 11:

                s_state = 'r_ugd'
            else:
                stt = ['q_ugd', 'w_ugd', 'e_ugd']
                i = random.randrange(0 ,2 , 1)
                s_state = stt[i]


        # q_u = self.pic(self, 'IMGS/SKILLS/q_ugd.PNG', 0)
        # if q_u[2] == 1:
        # return s_state, self.lvl
        self.minds(self, order, s_state, self.lvl)
###############################################################################
#   Unfinished Detecting and Attacking Core Part
#   Now jungle is developing and unusable.
###############################################################################
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

            elif way == 'jungle':
                print("Go wild")
                gameName = "League of Legends (TM) Client"
                game = win32gui.FindWindow(None, gameName)
                while game:
                    self.frog(self)
#                     self.buffB(self)
#                     self.buffR(self)
#                     self.stone(self)
#                     self.bird(self)
                    game = win32gui.FindWindow(None, gameName)
                    if not game:
                        break
                self.game_finish(self)

        else:

            print("No Game")
###############################################################################
#   Unfinished Decision Tree for other behaviours in game
#   Provide auto skills lvl up and the order to skills.
#   s_state is the state of every champion's skills
###############################################################################
        def minds(self, order, s_state, lvl):

        if s_state == 'q_n':

            if lvl == 1:
                q = self.pic(self, 'IMGS/SKILLS/Q_N.PNG', 0)
                if q[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('q')
                    pydirectinput.keyUp('q')
                    pydirectinput.keyUp('ctrl')

        elif s_state == 'w_n':

            if lvl == 2:
                w = self.pic(self, 'IMGS/SKILLS/W_N.PNG', 0)
                if w[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('w')
                    pydirectinput.keyUp('w')
                    pydirectinput.keyUp('ctrl')
        elif s_state == 'e_n':

            if lvl == 3:
                e = self.pic(self, 'IMGS/SKILLS/E_N.PNG', 0)
                if e[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('e')
                    pydirectinput.keyUp('e')
                    pydirectinput.keyUp('ctrl')
        elif s_state == 'r_n':

            if lvl == 6:
                r = self.pic(self, 'IMGS/SKILLS/R_N.PNG', 0)
                if r[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('r')
                    pydirectinput.keyUp('r')
                    pydirectinput.keyUp('ctrl')
        elif s_state == 'q_ugd':

            if lvl == 4:

                q_u = self.pic(self, 'IMGS/SKILLS/q_ugd.PNG', 0)
                if q_u[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('q')
                    pydirectinput.keyUp('q')
                    pydirectinput.keyUp('ctrl')

        elif s_state == 'w_ugd':

            if lvl == 5:

                w_u = self.pic(self, 'IMGS/SKILLS/w_ugd.PNG', 0)
                if w_u[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('w')
                    pydirectinput.keyUp('w')
                    pydirectinput.keyUp('ctrl')
        elif s_state == 'e_ugd':

            if lvl == 7:

                e_u = self.pic(self, 'IMGS/SKILLS/e_ugd.PNG', 0)
                if e_u[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('e')
                    pydirectinput.keyUp('e')
                    pydirectinput.keyUp('ctrl')
        elif s_state == 'r_ugd':

            if lvl == 11:

                r_u = self.pic(self, 'IMGS/SKILLS/r_ugd.PNG', 0)
                if r_u[2] == 1:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('r')
                    pydirectinput.keyUp('r')
                    pydirectinput.keyUp('ctrl')

        if order == 'q':
            q = self.pic(self, 'IMGS/SKILLS/Q.PNG', 0)
            if q[2] == 1:
                pydirectinput.press('q')
        else:

            print("No this order")

        if order == 'w':

            w = self.pic(self, 'IMGS/SKILLS/W.PNG', 0)
            if w[2] == 1:
                pydirectinput.press('w')
        elif order == 'e':

            e = self.pic(self, 'IMGS/SKILLS/E.PNG', 0)
            if q[2] == 1:
                pydirectinput.press('e')
        elif order == 'r':

            r = self.pic(self, 'IMGS/SKILLS/R.PNG', 0)
            if q[2] == 1:
                pydirectinput.press('r')
        elif order == 'd':

            d = self.pic(self, 'IMGS/SKILLS/D.PNG', 0)
            if d[2] == 1:
                pydirectinput.press('d')
        elif order == 'f':

            f = self.pic(self, 'IMGS/SKILLS/F.PNG', 0)
            if f[2] == 1:
                pydirectinput.press('f')
            else:

                pydirectinput.press('f')
        elif order == 'b':

            pydirectinput.press('b')
        else:

            print("No this order")
###############################################################################
#   Pure Axis MEthod, I think it's not very nice.
###############################################################################
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


###############################################################################
#   Main
###############################################################################

gametitle = "League of Legends (TM) Client"
clienttitle = "League of Legends"

if __name__ == '__main__':

    main = LeagueAuto
    main.client_move(main, 'train')
    main.game_move(main, 'mid')



