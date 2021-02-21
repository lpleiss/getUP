from kivy.lang.builder import Builder
from pathlib import Path

from kivy.uix.screenmanager import Screen

screens_path = str(Path(__file__).parent.absolute()) + "/kv/screens.kv"
Builder.load_file(screens_path)

# Declare all screens


class MenuScreen(Screen):
    """
    Screen holding all widgets of the the Main Menu. Setup sepcified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)


class SetAlarmScreen(Screen):
    """
    Screen holding all widgets of the the Set Alarm-Screen. Setup sepcified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(SetAlarmScreen, self).__init__(**kwargs)


class SetClockScreen(Screen):
    """
    Screen holding all widgets of the the Set Clock-Screen. Setup sepcified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(SetClockScreen, self).__init__(**kwargs)


class WakeScreen(Screen):
    """
    Screen holding all widgets of the the Initiation of the wake up-routine. Setup sepcified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(WakeScreen, self).__init__(**kwargs)


class BlobScreen(Screen):
    """
    Screen holding all widgets of the the Blob-Game. Setup sepcified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(BlobScreen, self).__init__(**kwargs)

    def initialise(self):
        """
        Calls initialise function of widget attached to screen.
        """
        self.children[0].initialise()


class CalcScreen(Screen):
    """
    Screen holding all widgets of the the Calculator-Game. Setup specified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(CalcScreen, self).__init__(**kwargs)

    def initialise(self):
        """
        Calls initialise function of widget attached to screen.
        """
        self.children[0].initialise()


class StretchScreen(Screen):
    """
    Screen holding all widgets of the the Stretching-Task. Setup specified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(StretchScreen, self).__init__(**kwargs)

    def initialise(self):
        """
        Calls initialise function of widget attached to screen.
        """
        self.children[0].initialise()


class SquatScreen(Screen):
    """
    Screen holding all widgets of the the Squatting-Task. Setup specified in "src/gui/kv/screens.kv"
    """

    def __init__(self, **kwargs):
        super(SquatScreen, self).__init__(**kwargs)

    def initialise(self):
        """
        Calls initialise function of widget attached to screen.
        """
        self.children[0].initialise()
