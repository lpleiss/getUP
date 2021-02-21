# getUP
This project aims at developing an interactive alarm clock that really makes you get up in the morning.
## Needed Hardware
| Hardware Name                                         | Connection Instructions                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------------------|
| RaspberryPi3                                          | connect your raspberry Pi to the power bank, conenct mouse and keyboard           |
| GrovePi+                                              | stick the GrovePi on top of your RaspberryPi3s Pins                               |
| TouchscreenAdafruit TFT HDMI Backpack (7“, 800 x 480) | connect he touchscreen via HDMI to your RaspberryPi3, attach it to the Powerbank  |
| Zerone Wlan Lautsprecher                              | connect the AUX-cable to the Rasperry Pi 3, connect the speaker to the power bank |
| Grove IR Distance Interrupter                         | attach to a I2C-Port on the GrovePi (specify port [DIST_PORT] in config.txt)      |
| 8x16 Adafruit LED-Matrix                              | connect to GrovePi‘s PINS as specified on GPIO                                    |
| HDMI-Kabel                                            | used to connect Toucscreen and RaspberryPi3                                       |
| Evary Powerbank, 5000 mAh                             | used to Power RaspberryPi3, speaker and touchscreen                               |

Feel free to use any case you want for the getUP. We went for a rather simplistic design based on wood using lasercut technology.

## Project Setup
1. download via ```git clone https://gitlab.tubit.tu-berlin.de/lseiling/getUP.git```
2. we recommend using a virtual enviroment to install and store the needed libraries. 
	* First, please make sure to install virtualenv by using ```pip install virtualenv```
	* Thnm, you can create a virtualenv instance using ```virtualenv getUP``` and activate it with ```source getUP/bin/activate```.
	* Install all required dependencies using ```pip install -r requirements.txt```
	* if you want to deactivate the virtual enviroment, simply type ```deactivate``` into your console
3. additionally, you will have to install two additional libraries on the Raspberry Pi's system: 
	* Install mplayer with ```sudo apt-get install mplayer``` 
	* Install grovepi using ```sudo curl -kL dexterindustries.com/update_grovepi | bash```
4. restart the system using ```sudo reboot```

## Run Tests
To run all test run ```pytest -v -s```.

## Run Project
- start complete clock with hardware and specified config.txt via ```sudo python3 src/main.py``` from root directory.
- to mock hardware input, change to ```mock-hardware``` branch via ```git checkout mock-hardware``` fist, then start using ```sudo python3 src/main.py```

  
  
A project by Lukas Seiling, Leonard Pleiss and Nadja Hemming