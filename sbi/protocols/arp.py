from sbi.common.protocol import Protocol

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class ArpProtocol(Protocol):
    '''
    Base Class for ARP protocol
    '''
    def set_ARP_entry(self, iface, mac_addr, ip_addr):
        '''
        Manipulates the entries in the ARP cache.
        '''
        raise NotImplementedError

    def get_ARP_entries(self):
        '''
        Manipulates the entries in the ARP cache.
        '''
        raise NotImplementedError
