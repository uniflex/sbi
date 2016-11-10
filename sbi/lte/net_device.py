from sbi.radio_device.net_device import RadioNetDevice

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class LteNetDevice(RadioNetDevice):
    '''
    Base Class for LTE Network Device
    '''
    def configure_mimo_mode(self, mimo_mode):
        '''
        Configures the MIMO mode
        '''
        raise NotImplementedError
