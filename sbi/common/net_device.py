__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class NetDevice(object):
    '''
    Base Class for Network Device
    '''
    def is_up(self):
        '''
        Check state of net device
        '''
        raise NotImplementedError

    def set_up(self):
        '''
        desc
        '''
        raise NotImplementedError

    def set_down(self):
        '''
        desc
        '''
        raise NotImplementedError

    def set_hw_address(self, addr):
        '''
        desc
        '''
        raise NotImplementedError

    def get_hw_address(self):
        '''
        desc
        '''
        raise NotImplementedError
