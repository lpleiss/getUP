from py_utils.config_utils import *

def test_read_config():
	"""
	Tests reading from config.txt.
	"""
	time = get_config_value('WAKE_TIME')
	assert type(time) == str

def test_write_config():
	"""
	Tests writing to config.txt.
	"""
	set_config_value('WAKE_TIME', '09:00:00')
	assert get_config_value('WAKE_TIME') == '09:00:00'