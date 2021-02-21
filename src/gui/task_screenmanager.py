from random import shuffle
from kivy.clock import Clock
from py_utils import config_utils, time_utils

from hardware.hardware_handler import HardwareHandler
from kivy.uix.screenmanager import ScreenManager

class TaskScreenManager(ScreenManager):
    '''
    The TaskScreenManager an extension of kivy's own ScreenManager class and serves as GetUP's central screen manager.
    It continously checks if the alarm time is reached and handles the display and switching of screens when the
    GetUP routine in initiated. 

    Attributes:
        routine_started (bool): tracks if the GetUP routine has started
        current_phase (int): tracks the current screen state (-2: main and setting screens, -1: waking screen, >=0: task at index)
        alarm_started (bool): tracks if the alarm has started ringing
        moved_alarm (bool): tracks if the alarm has been moved (neccessary for the alarm to stop)

        tasks (list): list of tasks that are to be passed through in the GetUP routine (read from config.txt)
        shuffle_tasks (bool): boolean indicating if tasks in GetUP routine should be shuffled (read from config.txt)
        task_screen_states (list): list of dictionaries for each task in task list. 
                                   each element contains two boolean value for the keys "started" and finished, indicating task state.

        alarm_sound (str): path to sound file with alarm sound (read from config.txt)
        workout_sound (str): path to sound file with workout sound (read from config.txt)

        alarm_checker (kivy.Clock): kivy.Clock object that checks every second if the current time equals the alarm time and initiates 
                                    GetUP routine if that is the case.
        hwh (HardwareHandler): Instance of the HardwareHandler class used to interface with external in-/output.
    '''
    
    routine_started = False
    current_phase = None
    alarm_started = False
    moved_alarm = False

    tasks = None
    shuffle_tasks = False
    task_screen_states = []

    alarm_sound = ""
    workout_sound = ""

    alarm_checker = None
    hwh = None


    def __init__(self, **kwargs):
        '''
        Initialises TaskScreenManager class inheriting from kivy's own Screen manager class and sets/initialises class attributes.
        '''
        super(ScreenManager, self).__init__(**kwargs)

        self.current_phase = -2

        self.tasks = config_utils.get_config_value("TASKS")
        self.shuffle_tasks = config_utils.get_config_value("SHUFFLE")
        self.reset_task_states()

        self.alarm_sound = config_utils.get_config_value("ALARM_SOUND")
        self.workout_sound = config_utils.get_config_value("WORKOUT_SOUND")
        
        self.hwh = HardwareHandler()
        self.alarm_checker = Clock.schedule_interval(lambda x: self.check_alarm(), 0.1)

    def reset_task_states(self):
        '''
        Resets all elements in task_screen_states to dictionaries containing only False values for the given keys.
        This state represents that no GetUP routine tasks have started or have been completed.
        '''
        self.task_screen_states = [{"started": False, "finished": False} for element in self.tasks]

    def check_alarm(self):
        '''
        Called every second, comparing the current time with the set waking time. If the waking time is reached, the routine is started.
        If the routine is started the state of the ui is checked and potentially altered, based on the input received through touchscreen
        or hardware.
        '''
        WAKE_TIME = config_utils.get_config_value("WAKE_TIME")
        CURR_TIME = time_utils.get_current_time()

        if (WAKE_TIME == CURR_TIME) and not self.routine_started:
            self.start_routine()
        elif self.routine_started:
            self.check_ui_state()

    def start_routine(self):
        '''
        Shuffles the tasks if corresponding config.txt-value is set to true. Changes to the wake screen after updating the current_phase and
        routine_started attributes.
        '''
        if self.shuffle_tasks:
            shuffle(self.tasks)
        self.routine_started = True
        self.current_phase = self.current_phase + 1
        self.current = 'wake'

    def check_ui_state(self):
        '''
        Checks current_state and attribute and sets the current screen based on the completion of conditions neccessary to progress through
        the GetUP routine. Reverts back to original state and main menu after all tasks have been completed.
        '''
        # == -1 --> waking phase
        if self.current_phase == -1:
            self.check_alarm_state()

        # != len(self.tasks) --> any kind of task
        elif self.current_phase != len(self.tasks):

            if not self.get_current("started"):
                # setting screen by key defined in value in self.tasks at current index
                self.current = self.tasks[self.current_phase]

                # screen might take a split second to load --> check if screen is loaded as child
                if self.children:
                    self.children[0].initialise()
                    self.set_current("started", True)

            elif self.get_current("finished"):
                self.current_phase = self.current_phase +1

        # == len(self.tasks) --> iterated through all tasks, end of getUP routine
        else:
            self.routine_started = False
            self.reset_task_states()
            self.hwh.stop_sound()
            print("Reached end")
            self.current = 'menu'
            self.current_phase = -2


    def check_alarm_state(self):
        """
        Starts playing the alarm and initiates "sunrise" effect of LEDs. Alarm is stopped and current_phase is update only if clock is lifted.
        """
        self.hwh.update_distance()

        if self.alarm_started == False and self.moved_alarm == False:
            self.hwh.start_sound(self.alarm_sound, loop=True)
            self.hwh.sunrise()
            self.alarm_started = True

        elif self.alarm_started == True and self.moved_alarm == False:
            if self.hwh.distance == 1:
                self.moved_alarm = True

        elif self.alarm_started == True and self.moved_alarm == True:
            self.hwh.stop_sound()
            self.hwh.start_sound(self.workout_sound, loop=True)
            self.current_phase = self.current_phase + 1

    def set_current(self, state, boolean):
        '''
        Set "finished" key in dictionary at current_phase index in task_screen_states list.

        Args:
            state (str): str value (either "started" or "finished") indicating key to which corresponding value is to be returned.
            boolean (bool): boolean value to which "finished" should be set.
        '''
        self.task_screen_states[self.current_phase][state] = boolean

    def get_current(self, state):
        '''
        Returns value for either "started" or "finished" key at current_phase index in task_screen_states list.

        Args:
            state (str): str value (either "started" or "finished") indicating key to which corresponding value is to be returned.

        Returns:
            bool: boolean value indicating current task state.
        '''
        return self.task_screen_states[self.current_phase][state]
