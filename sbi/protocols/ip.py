from sbi.common.protocol import Protocol

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class IpProtocol(Protocol):
    '''
    Base Class for IP protocol
    '''
    def set_ip_address(self, iface, ip_address):
        '''
        Set IP address for given interface
        '''
        raise NotImplementedError

    def get_ip_address(self):
        '''
        Get IP address of given interface
        '''
        raise NotImplementedError

    def get_ifaces(self):
        '''
        Returns list of interface names,
        e.g. ['lo', 'ens33', 'lxcbr0', 'ovs-system'].
        '''
        raise NotImplementedError

    def change_routing(self, current_gw_ip_addr,
                       new_gw_ip_addr, device_ip_addr):
        '''
        Controls the routing.
        '''
        raise NotImplementedError


class FlowId(object):
    def __init__(self, srcAddress=None, dstAddress=None,
                 prot=None, srcPort=None, dstPort=None):
        self.srcAddress = srcAddress
        self.dstAddress = dstAddress
        self.prot = prot
        self.srcPort = srcPort
        self.dstPort = dstPort
