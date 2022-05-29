####################################################
# I tried this method, and it tended to be failed.
# My new thought is to use non-linear Classifier,
# But this work may needs huge training photos So I should go back and try any other possibility.
####################################################
  def monster_detect_and_hit(self):
        gameName = "League of Legends (TM) Client"
        game = win32gui.FindWindow(None, gameName)
        x, y, w, h = win32gui.GetWindowRect(game)
        global flag
        print("it starts")
        self.pic(self, 'IMGS/INGAME/JPOINT.PNG', 2)
        # self.mouse_in(self, 'right', 47, 775)  # 前进
        time.sleep(25)
        for monster in ['IMGS/INGAME/JUNGLES/BBIRD.PNG',
                        'IMGS/INGAME/JUNGLES/BIRD.PNG',
                        'IMGS/INGAME/JUNGLES/BLUE.PNG',
                        'IMGS/INGAME/JUNGLES/FROG.PNG',
                        'IMGS/INGAME/JUNGLES/RED.PNG',
                        'IMGS/INGAME/JUNGLES/STONE.PNG',
                        'IMGS/INGAME/JUNGLES/STONE2.PNG',
                        'IMGS/INGAME/JUNGLES/STONE3.PNG',
                        'IMGS/INGAME/JUNGLES/WOLF.PNG']:

            monst = self.pic(self, monster, 2)
            if monst[2] == 1:
                print("Monster found")
            self.skills(self,'q')
            self.mouse_in(self, 'right', 723, 500)  # Attack
            self.skills(self, 'q')
            time.sleep(7)
            self.mouse_in(self,'right', int((w / 2) + 10), int((h / 2) - 20))  # Attack
            self.skills(self, 'q')
            time.sleep(7)
            self.skills(self, 'f')
            time.sleep(2)
            self.skills(self, 'w')
            time.sleep(4)
            print("it finished")
