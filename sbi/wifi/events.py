from uniflex.core.events import EventBase
from sbi.radio_device.events import *
from sbi.radio_device.events import GenericRadioDeviceEvent

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


'''
    Defintion of WiFi specific device events.
'''

class GenericWiFiEvent(GenericRadioDeviceEvent):
    ''' base class for all WiFI events '''
    def __init__(self):
        super().__init__()
        pass

'''
    Events enabling handover operation in WiFi infrastructure networks. Note, it is a network-wide operation
    as multiple nodes are involved.
'''

class WiFiHandoverRequestEvent(GenericWiFiEvent):
    '''
    Event to trigger a handover operation.
    '''
    def __init__(self, client_sta_id, serving_AP, target_AP, gateway, **kwargs):
        super().__init__()
        self.client_sta_id = client_sta_id
        self.serving_AP = serving_AP
        self.target_AP = target_AP
        self.gateway = gateway
        self.kwargs = kwargs


class WiFiHandoverReplyEvent(GenericWiFiEvent):
    '''
    Reply sent after handover operation was performed.
    '''
    def __init__(self, success):
        super().__init__()
        self.success = success


''' Get serving AP '''

class WiFiGetServingAPRequestEvent(GenericWiFiEvent):
    '''
    Event to find out the AP serving a particular client station. Only supported in WiFI infrastructure mode.
    Note, it is a network-wide operation.
    '''

    def __init__(self, sta_mac_addr, wifi_intf):
        super().__init__()
        self.sta_mac_addr = sta_mac_addr
        self.wifi_intf = wifi_intf


class WiFiGetServingAPReplyEvent(GenericWiFiEvent):
    '''
    Event containing the UUID of the AP serving the client station.
    '''
    def __init__(self, sta_mac_addr, wifi_intf, ap_uuid):
        super().__init__(sta_mac_addr, wifi_intf)
        self.ap_uuid = ap_uuid


''' Test whether two WiFi nodes are in carrier sensing range of each other '''

class WiFiTestTwoNodesInCSRangeRequestEvent(GenericWiFiEvent):
    '''
    Event to test whether two nodes are in carrier sensing range or not.
    Note, it is a network-wide operation.
    '''
    def __init__(self, node1, node2, mon_dev, TAU):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.mon_dev = mon_dev
        self.TAU = TAU


class WiFiTestTwoNodesInCSRangeReplyEvent(WiFiTestTwoNodesInCSRangeRequestEvent):
    '''
    Reply event containing information about whether two nodes are in carrier sensing range or not.
    '''
    def __init__(self, node1, node2, mon_dev, TAU, in_cs):
        super().__init__(node1, node2, mon_dev, TAU)
        self.in_cs = in_cs


''' Pair-wise carrier sensing test. All pair of nodes in the network will be tested '''

class WiFiGetNodesInCSRangeRequestEvent(GenericWiFiEvent):
    '''
    Event to check each nodes pairs whether it is
    in carrier sensing range or not.
    '''
    def __init__(self, mon_dev, TAU):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = TAU


''' Test whether two WiFi nodes are in communication range of each other '''

class WiFiTestTwoNodesInCommRangeRequestEvent(GenericWiFiEvent):
    '''
    Event to test whether two nodes are in communication range or not.
    '''
    def __init__(self, node1, node2, mon_dev, MINPDR):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.mon_dev = mon_dev
        self.MINPDR = MINPDR


class WiFiTestTwoNodesInCommRangeReplyEvent(WiFiTestTwoNodesInCommRangeRequestEvent):
    '''
    Event containing information about whether two
    nodes are in communication range or not.
    '''
    def __init__(self, node1, node2, mon_dev, MINPDR, in_comm):
        super().__init__(node1, node2, mon_dev, MINPDR)
        self.in_comm = in_comm


''' Pair-wise communication range test. All pair of nodes in the network will be tested '''

class WiFiGetNodesInCommRangeRequestEvent(GenericWiFiEvent):
    '''
    Event to check each nodes pairs whether it is
    in communication range or not.
    '''
    def __init__(self, mon_dev, MINPDR):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = MINPDR
