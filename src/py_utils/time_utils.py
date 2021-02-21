import os
from datetime import datetime

def get_current_time():
	"""
	Reads current time rom system and returns it as a string. 

	Returns:
        str: string of current time in format %H:%M:%S.
	"""
	return datetime.now().strftime('%H:%M:%S')

def make_datetime_str(time_str):
	"""
    Gets the current date and changes the time to the given time_str. Returns combination as a string.

    Args:
        time_str (str): input string for time to be set in forma %H:%M
    
    Returns:
        str: string of date with given time in format %day %d %m %H:%M:%S %timezone %y.
	"""
	date = os.popen('sudo date').read()
	date = [part.strip() for part in date.split(" ")]
	date[-3] = time_str+":00"
	datetime_str = " ".join(date)
	return datetime_str

def set_date(date_str):
	"""
    Sets sytsem time to passed date specified by string.
    Requires root privileges. 
    """
	os.system('sudo date --set="{}"'.format(date_str))