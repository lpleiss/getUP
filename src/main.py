from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition
from gui.task_screenmanager import TaskScreenManager
from gui.screens import MenuScreen, SetAlarmScreen, SetClockScreen, WakeScreen, BlobScreen, CalcScreen, StretchScreen, SquatScreen


class GetUPMain(App):
    """
    The GetUPMain represents the application (window) containing the TaskScreenManager to which it attaches all neccessary screens.
    All further interaction is handled by the TaskScreenManager class.
    """

    # Create the screen manager and add screens
    sm = TaskScreenManager(transition=FadeTransition())

    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(SetAlarmScreen(name='set_alarm'))
    sm.add_widget(SetClockScreen(name='set_clock'))
    sm.add_widget(WakeScreen(name='wake'))
    sm.add_widget(BlobScreen(name='blob'))
    sm.add_widget(CalcScreen(name='calc'))
    sm.add_widget(StretchScreen(name='stretch'))
    sm.add_widget(SquatScreen(name='squat'))
    sm.current = "menu"

    def build(self):
        return self.sm


if __name__ == '__main__':
    GetUPMain().run()
