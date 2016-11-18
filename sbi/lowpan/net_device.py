from sbi.radio_device.net_device import RadioNetDevice

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class LowPanNetDevice(RadioNetDevice):
    '''
    Base Class for WiFi Network Device
    '''
    def disable_carrier_sensing(self):
        '''
        Disables carrier sensing

        i.e. no listen-before-talk.
        '''
        raise NotImplementedError

    def blacklist_channels(self):
        '''
        desc
        '''
        raise NotImplementedError
