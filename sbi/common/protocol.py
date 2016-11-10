__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class Protocol(object):
    '''
    Base Class for Protocol
    '''
    def is_enabled(self):
        '''
        Check state of net device
        '''
        raise NotImplementedError

    def enable(self):
        '''
        desc
        '''
        raise NotImplementedError

    def disable(self):
        '''
        desc
        '''
        raise NotImplementedError
