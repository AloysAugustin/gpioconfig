
# Author: Aloys

import RPi.GPIO as GPIO

class PairConfig:
    """ 
    Utility class to check whether two GPIO pins are shorted 

    All pin numbers should be board numbers
    """

    def __init__(self, read, invert, config):
        """
        Initializes this class

        Parameters:
        read - number of the pin to read
        invert - if False, status() will return True if the read pin is high, if True, status will return True if the pin is low
        config - List of dictionaries that contain the arguments necessary to setup the pins
        """
        self.read = read
        self.invert = invert
        self.config = config

    def status(self):
        """ Returns True if the pair of pins is connected, False otherwise """
        # Pin setup
        GPIO.setmode(GPIO.BOARD)
        for conf in self.config:
            GPIO.setup(**conf)
        # Reading
        status = (GPIO.input(self.read) != self.invert)
        # Pin cleanup (saves power)
        for conf in self.config:
            GPIO.cleanup(conf['channel'])
        return status

PAIRS = {
    1 : PairConfig(40, True, [{'channel': 40, 'direction': GPIO.IN, 'pull_up_down': GPIO.PUD_UP}]),
    2 : PairConfig(38, True, [{'channel': 38, 'direction': GPIO.IN, 'pull_up_down': GPIO.PUD_UP}, 
                              {'channel': 37, 'direction': GPIO.OUT, 'initial': GPIO.LOW}]),
    3 : PairConfig(36, True, [{'channel': 36, 'direction': GPIO.IN, 'pull_up_down': GPIO.PUD_UP}, 
                              {'channel': 35, 'direction': GPIO.OUT, 'initial': GPIO.LOW}]),
}


def get_status(pair):
    return PAIRS[pair].status()

