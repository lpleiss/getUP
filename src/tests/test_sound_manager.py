from hardware.hardware_handler import HardwareHandler

def test_play_sound():

	hwh = HardwareHandler()
	hwh.start_sound("./media/sounds/error.mp3")
