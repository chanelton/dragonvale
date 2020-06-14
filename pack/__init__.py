import time
import threading
from pynput.mouse import Button, Controller
import pynput.keyboard
from pynput.keyboard import Listener, KeyCode
import datetime

keyboard = pynput.keyboard.Controller()
delay = 5
button = Button.left
# input keys
start_stop_gem_key = KeyCode(char='g')
start_stop_magic_key = KeyCode(char='m')
start_stop_tutorial_key = KeyCode(char='t')
start_stop_click_key = KeyCode(char='c')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.gem = False
        self.magic = False
        self.tutorial = False
        self.click = False
        self.program_running = True

    # start gem script
    def start_gem(self):
        self.magic = False
        self.tutorial = False
        self.click = False
        self.gem = True
        # Read pointer position

    # start magic script
    def start_magic(self):
        self.gem = False
        self.tutorial = False
        self.click = False
        self.magic = True

    # start tutorial script
    def start_tutorial(self):
        self.gem = False
        self.magic = False
        self.click = False
        self.tutorial = True

    def start_click(self):
        self.gem = False
        self.magic = False
        self.tutorial = False
        self.click = True

    # stops whichever script is running
    def stop(self):
        if self.gem:
            self.gem = False
        elif self.magic:
            self.magic = False
        elif self.tutorial:
            self.tutorial = False
        elif self.click:
            self.click = False

    # ends scripts
    def exit(self):
        self.stop()
        self.program_running = False

    def run(self):
        i = 0
        while self.program_running:
            while self.gem:
                run_gem()
            while self.magic:
                run_magic()
            while self.tutorial:
                run_tutorial()
            while self.click:
                mouse.click(button)
                time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


# key input reader
def on_press(key):
    if key == start_stop_gem_key:
        if click_thread.gem:
            click_thread.stop()
            print('Stop Gem')
        else:
            click_thread.start_gem()
            print('Start Gem')
    elif key == start_stop_magic_key:
        if click_thread.magic:
            click_thread.stop()
            print('Stop Magic')
        else:
            click_thread.start_magic()
            print('Start Magic')
    elif key == start_stop_tutorial_key:
        if click_thread.tutorial:
            click_thread.stop()
            print('Stop Tutorial')
        else:
            click_thread.start_tutorial()
            print('Start Tutorial')
    elif key == start_stop_click_key:
        if click_thread.click:
            click_thread.stop()
            print('Stop Click')
        else:
            click_thread.start_click()
            print('Start Click')
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


# breeds and sells plant dragon eggs
# nursery and breeding cave must be diagonal from each other
# zoom set to default zoom from opening the game
# click on breeding cave before running
# breeding cave must have previously bred 2 plant dragons
# so there's a "retry" button
# nursery must be full and have a plant dragon egg
# in the left most position
def run_magic():
    # center
    mouse.position = (720, 470)
    time.sleep(0.4)
    mouse.click(button)
    time.sleep(0.4)
    # redo
    mouse.position = (528, 764)
    time.sleep(0.25)
    mouse.click(button)
    time.sleep(0.25)
    # breed
    mouse.position = (700, 700)
    time.sleep(0.25)
    mouse.click(button)
    time.sleep(1)
    # nursery
    mouse.position = (600, 320)
    time.sleep(0.75)
    mouse.click(button)
    time.sleep(1.2)
    # center
    mouse.position = (720, 470)
    time.sleep(0.3)
    mouse.click(button)
    time.sleep(0.6)
    # egg
    mouse.position = (200, 771)
    time.sleep(0.6)
    mouse.click(button)
    time.sleep(0.3)
    # sell
    mouse.position = (816, 560)
    time.sleep(0.3)
    mouse.click(button)
    time.sleep(0.25)
    # confirm
    mouse.position = (650, 700)
    time.sleep(0.25)
    mouse.click(button)
    time.sleep(0.8)
    # click egg
    mouse.position = (815, 525)
    time.sleep(0.6)
    mouse.click(button)
    time.sleep(0.25)
    # confirm nursery
    mouse.position = (650, 700)
    time.sleep(0.25)
    mouse.click(button)
    time.sleep(0.5)
    # move middle
    mouse.position = (865.61328125, 493.32421875)
    time.sleep(0.25)
    mouse.click(button)
    time.sleep(0.5)


# drags one cell down in "switch park" menu
def drag(n):
    for i in range(n):
        time.sleep(0.2)
        mouse.press(button)
        for i in range(7210):
            y = mouse.position[1]
            mouse.position = (mouse.position[0], y - 0.03)
        time.sleep(0.2)
        mouse.release(button)
        mouse.position = (700, 300)


# runs through alt accounts and gives single gem
# start with first account open
# runs 21 times
# different "close daily login page" mouse position
# depending on login day
def run_gem():
    zero_day = datetime.date(2020, 6, 10)
    cell = 0
    while cell < 21:
        # start in first account
        # collect daily login
        time.sleep(2)
        mouse.position = (722.41796875, 537.734375)
        time.sleep(0.1)
        mouse.click(button)
        # ok daily login
        time.sleep(1.4582030773162842)
        mouse.position = (720.515625, 670.0234375)
        time.sleep(0.1)
        mouse.click(button)
        # close daily login page
        time.sleep(3.279383182525635)
        # first galaxy dragon condition
        day = int(str(datetime.date.today() - zero_day)[0])
        if day != 30 or 60 or 90:
            if day == 2:
                mouse.position = (1300, 750)
            else:
                mouse.position = (1296.0625, 147.94140625)
            time.sleep(0.1)
            mouse.click(button)
        # social
        time.sleep(1.6)
        mouse.position = (1172.41015625, 746.703125)
        time.sleep(0.1)
        mouse.click(button)
        # friend
        time.sleep(1.2)
        mouse.position = (729.16015625, 180.94921875)
        time.sleep(0.1)
        mouse.click(button)
        # gift
        time.sleep(.7)
        mouse.position = (995.4375, 547.265625)
        time.sleep(0.1)
        mouse.click(button)
        # exit
        time.sleep(1.4)
        mouse.position = (1217.96484375, 118.78125)
        time.sleep(0.1)
        mouse.click(button)
        # settings
        time.sleep(1)
        mouse.position = (1030.07421875, 753.34375)
        time.sleep(0.1)
        mouse.click(button)
        # switch park
        time.sleep(2)
        mouse.position = (1022.9140625, 347.01171875)
        time.sleep(0.1)
        mouse.click(button)
        # scroll
        time.sleep(3)
        # doesn't drag on last loop through
        if cell < 20:
            drag(cell)
        cell += 1
        # click second-celled park, confirm
        time.sleep(2)
        mouse.position = (708.9921875, 416.26953125)
        time.sleep(0.1)
        mouse.click(button)
        # confirm
        time.sleep(1.5)
        mouse.position = (650.515625, 690.0234375)
        time.sleep(0.1)
        mouse.click(button)
        time.sleep(12)
    click_thread.exit()


# goes through tutorial process of making new account
# runs 21 times
# named 0-9, 90-99, 999 to keep order
# all naming of plant dragons automated to "a"
# change the numbers on line 275 to own friend code
# "coords" file must be in a package
def run_tutorial():
    park_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '999']
    park = 0
    while park <= 21:
        g = open("coords")
        for line in g:
            f = line
            if f == 'name\n':
                delay_ = g.readline()
                time.sleep(float(delay_))
                keyboard.press('a')
                f = g.readline()
            if f == 'id\n':
                delay_ = g.readline()
                time.sleep(float(delay_))
                for key in ['3', '1', '3', '0', '7', '9', '4']:
                    keyboard.press(key)
                f = g.readline()
            if f == 'parkname\n':
                delay_ = g.readline()
                time.sleep(float(delay_))
                if len(park_names[0]) > 1:
                    keyboard.press(park_names[park][0])
                    keyboard.press(park_names[park][1])
                else:
                    keyboard.press(park_names[park])
                park += 1
                f = g.readline()
            pos = f.replace("(", "").replace(")", "").split(',')
            delay_ = g.readline()
            time.sleep(float(delay_))
            mouse.position = (float(pos[0]), float(pos[1]))
            time.sleep(.1)
            mouse.click(button)
            print(mouse.position)
    click_thread.exit()


with Listener(on_press=on_press) as listener:
    listener.join()