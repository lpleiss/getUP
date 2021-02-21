from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.button import Button
from kivy.clock import Clock

import os
import time
import random
from pathlib import Path
from datetime import datetime
from py_utils import config_utils
from hardware.hardware_handler import HardwareHandler


widgets_path = str(Path(__file__).parent.absolute()) + "/kv/widgets.kv"
Builder.load_file(widgets_path)


class MainClockWidget(FloatLayout):
    current_time = StringProperty()

    def __init__(self, **kwargs):
        """
        This function initiates the clock, when the program is launched.
        """
        super(MainClockWidget, self).__init__(**kwargs)
        Clock.schedule_interval(lambda x: self.update_time(), 1)

    def update_time(self):
        """
        This function updates the time on the display every second.
        """
        self.current_time = datetime.now().strftime('%H:%M:%S')


class MainOptionButtons(FloatLayout):
    """
    This class enables the functioning of the lightswitch in the main menu.
    """
    light_on = True

    def __init__(self, **kwargs):
        """
        This function initiates the light toggling options when the program is launched.
        """
        super(MainOptionButtons, self).__init__(**kwargs)

    def toggle_light(self):
        """
        This function enables the lightswitch by accessing the lights_off- and lights_on-Functions (.src/hardware/lights_on.py // .src/hardware/lights_on.py).
        """
        if self.light_on:
            HardwareHandler().lights_off()
            self.light_on = False
        else:
            HardwareHandler().lights_on()
            self.light_on = True


class SetClockWidget(FloatLayout):
    '''
    This class containts all necessary functionalities and variables of the Set Clock-Screen.
    '''

    minutes = 0
    tenMinutes = 0
    hours = 0
    tenHours = 0
    waketime = StringProperty()

    def __init__(self, **kwargs):
        '''
        This function is used to convert the time components (tenHours, hours, ten Minutes, minutes) into the proper format.
        '''
        super(SetClockWidget, self).__init__(**kwargs)
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def confirm_and_return(self):
        '''
        This function enables the confirmation of the time or alarm after setting it in the SetAlarm or SetTime-Screen and a return to the main screen.
        '''
        if self.parent.name == 'set_clock':
            date = os.popen('sudo date').read().strip().split(" ")
            print(date)
            date = date[1:3] + date[5:6] + [self.waketime + ":00"]
            date = " ".join(date)
            print(date)
            os.system('sudo date --set="{}"'.format(date))

        elif self.parent.name == 'set_alarm':
            config_utils.set_config_value('WAKE_TIME', self.waketime + ":00")

        self.parent.parent.current = 'menu'

    def moreMinutes(self):
        '''
        This function adds one more minute to the current time in the setAlarm- or setClock-Screen, when the moreMinutes-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.minutes = self.minutes + 1
        if self.minutes == 10:
            self.minutes = 0
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def moreTenMinutes(self):
        '''
        This function adds ten more minutes to the current time in the setAlarm- or setClock-Screen, when the tenMoreMinutes-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.tenMinutes = self.tenMinutes + 1
        if self.tenMinutes == 6:
            self.tenMinutes = 0
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def moreHours(self):
        '''
        This function adds one more hour to the current time in the setAlarm- or setClock-Screen, when the moreHours-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.hours = self.hours + 1
        if self.tenHours == 0:
            if self.hours == 10:
                self.hours = 0
        if self.tenHours == 1:
            if self.hours == 10:
                self.hours = 0
        if self.tenHours == 2:
            if self.hours == 4:
                self.hours = 0
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def moreTenHours(self):
        '''
        This function adds ten more hours to the current time in the setAlarm- or setClock-Screen, when the tenMoreHours-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.tenHours = self.tenHours + 1
        if self.tenHours == 3:
            self.tenHours = 0
        if self.tenHours == 2:
            if self.hours > 3:
                self.hours = 3
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def lessMinutes(self):
        '''
        This function reduces the current time in the setAlarm- or setClock-Screen by one minute, when the lessMinutes-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.minutes = self.minutes - 1
        if self.minutes == -1:
            self.minutes = 9
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def lessTenMinutes(self):
        '''
        This function reduces the current time in the setAlarm- or setClock-Screen by ten minutes, when the lessTenMinutes-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.tenMinutes = self.tenMinutes - 1
        if self.tenMinutes == -1:
            self.tenMinutes = 5
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def lessHours(self):
        '''
        This function reduces the current time in the setAlarm- or setClock-Screen by one hour, when the lessHours-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.hours = self.hours - 1
        if self.tenHours == 0:
            if self.hours == -1:
                self.hours = 9
        if self.tenHours == 1:
            if self.hours == -1:
                self.hours = 9
        if self.tenHours == 2:
            if self.hours == -1:
                self.hours = 3
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)

    def lessTenHours(self):
        '''
        This function reduces the current time in the setAlarm- or setClock-Screen by ten hours, when the lessTenHours-button is pressed.
        Needed exceptions are declared to secure a span of 00:00:00 to 23:59:59.
        '''
        self.tenHours = self.tenHours - 1
        if self.tenHours == -1:
            self.tenHours = 2
        if self.tenHours == 2:
            if self.hours > 3:
                self.hours = 3
        self.waketime = str(self.tenHours) + str(self.hours) + ":" + str(self.tenMinutes) + str(self.minutes)
        print(self.waketime)


class BlobGameButton(Button):
    '''
    This class containts all necessary functionalities and variables of the BlobGame-Buttons.
    '''
    red = (255, 0, 0, 1)
    blue = (0, 0, 255, 1)
    black = (0, 0, 0, 1)
    white = (255, 255, 255, 1)
    score = 0

    def __init__(self, targetColor, distractorColor, **kwargs):
        '''
        This function initiates the buttons, when the blobGame is started.
        '''
        self.targetColor = targetColor
        self.distractorColor = distractorColor
        super(BlobGameButton, self).__init__(**kwargs)
        self.bind(on_press=lambda x: self.colorCheck())
        self.bind(on_release=lambda x: self.notTrue())

    def colorCheck(self):
        '''
        This function checks, whether a click on the button is correct (that is, when the clicked button is colored in the targetColor.
        If the click is correct, the button will disappear by switching its color to the background-color.
        When all target buttons are clicked, the blobGame is done.
        '''
        if tuple(self.background_color) == self.targetColor:
            self.background_color = self.white
            self.parent.buttonsClicked += 1
            if self.parent.buttonsClicked == self.parent.numberOfButtons:
                self.parent.parent.parent.set_current("finished", True)

        elif tuple(self.background_color) != self.targetColor and tuple(self.background_color) != self.white:
            if tuple(self.distractorColor) != self.black:
                self.background_color = self.black

    def notTrue(self):
        '''
        This function checks, whether a click on the button is incorrect (that is, when the clicked button is not colored in the targetColor.
        If the click is incorrect, the button will change its color while being held and will switch to the original color after being released.
        '''
        if tuple(self.distractorColor) == self.white:
            if self.targetColor == self.red:
                self.background_color = self.blue
            elif self.targetColor == self.blue:
                self.background_color = self.red


class BlobGameWidget(FloatLayout):
    '''
    This class containts all necessary functionalities and variables of the BlobGameWidget, except for the buttons (declared earlier).
    '''
    red = (255, 0, 0, 1)
    blue = (0, 0, 255, 1)
    black = (0, 0, 0, 1)
    white = (255, 255, 255, 1)
    score = 0

    #Possible Coordinates for the buttons are declared.
    yCoordinates = [0.1, 0.3, 0.5, 0.7]
    xCoordinates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    #the targetColor is set.
    possibleColors = ['blue', 'red']
    targetColorString = random.choice(possibleColors)

    #The Instruction is set in the targetColor.
    instruction = StringProperty()
    instruction = "Hurry! Click all the " + targetColorString + " Buttons!"

    targetColor = NumericProperty()
    distractorColor = NumericProperty()

    if targetColorString == 'blue':
        targetColor = blue
    elif targetColorString == 'red':
        targetColor = red

    # The Distractor-Color is set.
    distractorColorString = random.choice(possibleColors)
    if distractorColorString == 'blue':
        distractorColor = blue
    elif distractorColorString == 'red':
        distractorColor = red

    #Lists for the blue and red buttons are set up.
    blueButtons = []
    redButtons = []

    def __init__(self, **kwargs):
        '''
        This function enables the BlobGameWidget when the program is launched.
        '''
        super(BlobGameWidget, self).__init__(**kwargs)
       
        


    def initialise(self):
        '''
        This function initiates the BlobGameWidget.
        '''
        self.numberOfButtons = 10
        self.buttonsClicked = 0
        self.remove_all_buttons()
        self.add_buttons()

    def add_buttons(self):
        '''
        This function creates the correct number of blue and red buttons.
        '''
        self.blueButtons = []
        self.redButtons = []
        for i in range(1, self.numberOfButtons + 1):
            b_red = "b_red_" + str(i)
            self.redButtons.append(b_red)
            b_blue = "b_blue" + str(i)
            self.blueButtons.append(b_blue)

        self.buttonPositions = [" "]
        self.add_blue_buttons()
        self.add_red_buttons()

    def add_blue_buttons(self):
        '''
        This function makes sure that blue buttons are not overlapping with one another.
        '''
        for btn_name in self.blueButtons:
            buttonAdded = False
            xPosition = random.choice(self.xCoordinates)
            yPosition = random.choice(self.yCoordinates)
            buttonPosition = (xPosition, yPosition)

            while buttonAdded == False:
                if buttonPosition in self.buttonPositions:
                    xPosition = random.choice(self.xCoordinates)
                    yPosition = random.choice(self.yCoordinates)
                    buttonPosition = (xPosition, yPosition)
                else:
                    self.buttonPositions.append(buttonPosition)
                    xFinalPosition = buttonPosition[0]
                    yFinalPosition = buttonPosition[1]
                    buttonAdded = True

            #If the buttons are not overlapping with any other blue buttons, they are added to the screen.
            btn_name = BlobGameButton(self.targetColor, self.distractorColor, size_hint=(.1, .1),
                               pos_hint={'center_x': xFinalPosition, 'center_y': yFinalPosition},
                               background_color=self.blue)
            self.add_widget(btn_name)

    def add_red_buttons(self):
        '''
        This function makes sure that red buttons are not overlapping with one another.
        '''
        for btn_name in self.redButtons:
            buttonAdded = False
            xPosition = random.choice(self.xCoordinates)
            yPosition = random.choice(self.yCoordinates)
            buttonPosition = (xPosition, yPosition)

            while buttonAdded == False:
                if buttonPosition in self.buttonPositions:
                    xPosition = random.choice(self.xCoordinates)
                    yPosition = random.choice(self.yCoordinates)
                    buttonPosition = (xPosition, yPosition)
                else:
                    self.buttonPositions.append(buttonPosition)
                    xFinalPosition = buttonPosition[0]
                    yFinalPosition = buttonPosition[1]
                    buttonAdded = True

            #If the buttons are not overlapping with any other blue OR red buttons, they are added to the screen.
            btn_name = BlobGameButton(self.targetColor, self.distractorColor, size_hint=(.1, .1),
                               pos_hint={'center_x': xFinalPosition, 'center_y': yFinalPosition},
                               background_color=self.red)
            self.add_widget(btn_name)

    def remove_all_buttons(self):
        '''
        This function removes all buttons.
        '''

        all_btns = self.blueButtons + self.redButtons
        for btn_name in all_btns:
            try:
                self.remove_widget(btn_name)
            except:
                pass


class CalculatorGameWidget(FloatLayout):
    '''
    This class containts all necessary functionalities and variables of the CalculatorGame.
    '''

    #Error Sound, the task and 4 solution choices are declared.
    error_sound = config_utils.get_config_value("ERROR_SOUND")
    result = 0
    calculusTask = StringProperty()
    option1 = NumericProperty()
    option2 = NumericProperty()
    option3 = NumericProperty()
    option4 = NumericProperty()


    def __init__(self, **kwargs):
        '''
        This function enables the calculator game, when the program is launched.
        '''
        super(CalculatorGameWidget, self).__init__(**kwargs)


    def initialise(self):
        '''
        This function initialises the calculator game.
        '''
        self.generate_questions()

    def generate_questions(self):
        '''
        This function generates questions by creating 3 random numbers and chaining them with one of 5 combinations of operators.
        '''

        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        whichTask = random.randint(1, 5)

        if whichTask == 1:
            self.calculusTask = str(a) + " + " + str(b) + " + " + str(c)
            self.result = a + b + c
        elif whichTask == 2:
            self.calculusTask = str(a) + " - " + str(b) + " + " + str(c)
            self.result = a - b + c
        elif whichTask == 3:
            self.calculusTask = str(a) + " * " + str(b) + " + " + str(c)
            self.result = a * b + c
        elif whichTask == 4:
            self.calculusTask = str(a) + " * " + str(b) + " - " + str(c)
            self.result = a * b - c
        elif whichTask == 5:
            self.calculusTask = str(a) + " - " + str(b) + " - " + str(c)
            self.result = a - b - c

        '''
        3 distractors are created by adapting the result by adding or subtracting a random number.
        '''

        distractor1 = self.result + random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        distractor2 = self.result + random.choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
        distractor3 = self.result + random.choice([-15, -14, -13, -12, -11, 11, 12, 13, 14, 15])

        possAnswers = [self.result, distractor1, distractor2, distractor3]
        random.shuffle(possAnswers)

        self.option1 = possAnswers[0]
        self.option2 = possAnswers[1]
        self.option3 = possAnswers[2]
        self.option4 = possAnswers[3]

    def checkResult(self, option):
        '''
        The clicked button is checked. If the clicked button does not contain the correct result, and error sound is played.

        Args:
            option (int): one of the numeric options (self.option1 - self.option4) attached to the respective button in widgets.kv.

        '''
        if option == self.result:
            self.parent.parent.set_current("finished", True)
        else:
            HardwareHandler().start_sound(self.error_sound)


class StretchWidget(FloatLayout):
    '''
    This class containts all necessary functionalities and variables of the Stretching Task.
    '''
    hwh = None
    timer = None
    starting_score = 0
    instruction = StringProperty()
    score = NumericProperty()

    def __init__(self, **kwargs):
        '''
        This function enables the stretch task, when the program is launched.
        '''
        super(StretchWidget, self).__init__(**kwargs)
        self.hwh = HardwareHandler()
        self.starting_score = config_utils.get_config_value("SECS_STRETCH")

    def initialise(self):
        '''
        This function initialises the strech task.
        '''
        self.score = self.starting_score
        self.instruction = "Please make sure that the top of the getUP\nis facing upwards during the exercise."
        self.timer = Clock.schedule_interval(lambda x: self.check_phase(), 1)

    def check_phase(self):
        '''
        This function adapts the seconds to hold the stretch according to the input of the distance sensor.
        When the time is up, the task is declared finished.
        '''
        self.hwh.update_distance()
        if self.hwh.distance == 0:
            self.instruction = "Now hold until the time is up."
            self.score = self.score - 1
        if self.score == 0:
            self.parent.parent.set_current("finished", True)
            self.timer.cancel()


class SquatWidget(FloatLayout):
    '''
    This class containts all necessary functionalities and variables of the Squatting Task.
    '''
    hwh = None
    timer = None
    starting_score = 0
    img_source = StringProperty()
    score = NumericProperty()

    def __init__(self, **kwargs):
        '''
        This function enables the squatting task, when the program is launched.
        '''
        super(SquatWidget, self).__init__(**kwargs)
        self.hwh = HardwareHandler()
        self.starting_score = config_utils.get_config_value("NUM_SQUAT")

    def initialise(self):
        '''
        This function initialises the squatting task.
        '''
        self.score = self.starting_score
        self.prev = self.hwh.distance
        self.standing = True
        self.timer = Clock.schedule_interval(lambda x: self.check_phase(), 0.5)

    def check_phase(self):
        '''
        This function adapts the image shown in the screen according to the input of the distance sensor.
        When the time is up, the task is declared finished.
        '''
        self.check_position()

        if self.standing:
            self.img_source = "./media/icons/squat.png"
        else:
            self.img_source = "./media/icons/startpos.png"

        if self.score == 0:
            self.parent.parent.set_current("finished", True)
            self.timer.cancel()

    def check_position(self):
        '''
        This function adapts the remaining repitions to hold the stretch according to the input of the distance sensor.
        When the time is up, the task is declared finished.
        '''
        self.hwh.update_distance()
        print("prev: {}, now: {}".format(self.prev, self.hwh.distance))
        if self.hwh.distance == 0 and self.prev == 1:
            if not self.standing:
                self.score = self.score - 1
                self.standing = True
        elif self.hwh.distance == 1 and self.prev == 0:
            self.standing = False
        self.prev = self.hwh.distance
