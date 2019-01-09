"""
Author: Romain Fafet (farom57@gmail.com)
"""
from skyfield.api import load

class Configuration(object):
    """ A Configuration store all the settings for the Tracker.

    Those settings can be edited through the UI. Configuration class also
    provide functions to load and save itself on a file
    """
    def __init__(self):
        self.indi_server_ip = "127.0.0.1"
        self.indi_port = 7624
        self.indi_telescope_driver = ""
        self.indi_joystick_driver = ""

        self.satellites_url = "http://celestrak.com/NORAD/elements/stations.txt"
        self.selected_satellite = "ISS (ZARYA)"
        self.satellites_tle = load.tle(self.satellites_url)

        self.observer_alt = 5
        self.observer_lat = "43.538 N"
        self.observer_lon = "6.955 E"

        self.selected_satellite = "ISS (ZARYA)"

        self.p_gain = 1
        self.i_gain = 0


