from sbi.common.protocol import Protocol

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class TcpProtocol(Protocol):
    '''
    Base Class for TCP protocol
    '''
    def set_tx_window_size(self):
        '''
        Set TX window size
        '''
        raise NotImplementedError

    def get_tx_window_size(self):
        '''
        Get TX window size
        '''
        raise NotImplementedError
