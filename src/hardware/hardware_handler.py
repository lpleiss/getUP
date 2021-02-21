import subprocess
from py_utils import config_utils
from grovepi import digitalRead, pinMode


class HardwareHandler:
    '''
    The HardwareHandler groups all interactions with the hardware that are not detected through the touchscreen (or clicks) and reads from the
    connected sensors.

    Attributes:
        distance (int): value read from infrared distance sensor (either 1 or 0)
        dist_port (int): IC2 port from which to read distance sensor data, specified in config.txt
        lights (subprocess): variable pointing to subprocess that runs light scripts in background
        player (subprocess): variable pointing to subprocess that runs mplayer in background to enable sound starting and stopping
    '''

    distance = None
    dist_port = None
    lights = None
    player = None

    def __init__(self):
        '''
        Initialises HardwareHandler by setting class attributes.
        '''
        self.distance = None
        self.player = None
        self.dist_port = config_utils.get_config_value("DIST_PORT")

    
    def update_distance(self):
        '''
        Reads distance output from infrared distance sensor and saves the value to self.distance.
        '''
        pinMode(self.dist_port,"INPUT")
        self.distance = digitalRead(self.dist_port)
        pass

    def lights_on(self):
        '''
        Tries to run lights_on.py file as a background process.
        '''
        print("lights on")
        self.lights = subprocess.Popen(["python3", "src/hardware/lights_on.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def lights_off(self):
        '''
        Tries to run lights_off.py file as a background process.
        '''
        print("lights off")
        self.lights = subprocess.Popen(["python3", "src/hardware/lights_off.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def sunrise(self):
        '''
        Tries to run sunrise.py file as a background process.
        '''
        self.lights = subprocess.Popen(["python3", "src/hardware/sunrise.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def start_sound(self, sound_file, loop=False):
        '''
        Starts mplayer subprocess playing specified sound file and attaching it to this class' player variable.

        Args:
            sound_file (str): str value specifying path to sound file
            loop (bool): boolean value indicating if sound file should be looped indefinetely, default: False
        '''
        print("Playing {}".format(sound_file))
        if not loop:
            self.player = subprocess.Popen(["mplayer", sound_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            self.player = subprocess.Popen(["mplayer", "-loop", "0", sound_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def stop_sound(self):
        '''
        Stops currently running mplayer subprocess attached to this class if one exists.
        '''
        try:
            self.player.kill()
        except:
            pass
