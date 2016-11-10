from uniflex.core.events import EventBase
from sbi.radio_device.events import *

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''
    Handover operation
'''


class TriggerHandoverRequestEvent(EventBase):
    '''
    Event to trigger a handover operation.
    '''
    def __init__(self, sta_id, serving_node, target_node, gateway):
        super().__init__()
        self.sta_id = sta_id
        self.serving_node = serving_node
        self.targetAP_node = target_node
        self.gateway = gateway


class TriggerHandoverReplyEvent(EventBase):
    '''
    Reply send after triggering handover operation.
    '''
    def __init__(self, success):
        super().__init__()
        self.success = success


'''
    The protocol-specific global events for performing network-wide operations
    which go beyond just remote UPI_R/N calls

    IEEE 802.11 protocol family
'''


class WiFiTriggerHandoverRequestEvent(TriggerHandoverRequestEvent):
    '''
    Event to trigger a WiFi handover operation.
    Only supported in infrastructure mode.
    '''

    def __init__(self, sta_mac_addr, sta_ip, wlan_iface,
                 wlan_inject_iface, network_bssid, serving_AP, serving_AP_ip,
                 serving_channel, target_AP, target_AP_ip,
                 target_channel, gateway, ho_scheme):
        super().__init__(sta_mac_addr, serving_AP, target_AP, gateway)
        self.sta_ip = sta_ip
        self.wlan_iface = wlan_iface
        self.wlan_inject_iface = wlan_inject_iface
        self.network_bssid = network_bssid
        self.servingAP_ip = serving_AP_ip
        self.servingChannel = serving_channel
        self.targetAP_ip = target_AP_ip
        self.targetChannel = target_channel
        self.ho_scheme = ho_scheme


class WiFiGetServingAPRequestEvent(EventBase):
    '''
    Event to find out the access point serving
    a particular client station. Only supported
    in infrastructure mode.
    '''

    def __init__(self, sta_mac_addr, wifi_intf):
        super().__init__()
        self.sta_mac_addr = sta_mac_addr
        self.wifi_intf = wifi_intf


class WiFiGetServingAPReplyEvent(EventBase):
    '''
    Event containing the UUID of the AP serving the client station.
    '''
    def __init__(self, sta_mac_addr, wifi_intf, ap_uuid):
        super().__init__(sta_mac_addr, wifi_intf)
        self.ap_uuid = ap_uuid


class WiFiTestTwoNodesInCSRangeRequestEvent(EventBase):
    '''
    Event to test whether two nodes are in carrier sensing range or not.
    '''
    def __init__(self, node1, node2, mon_dev, TAU):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.mon_dev = mon_dev
        self.TAU = TAU


class WiFiTestTwoNodesInCSRangeReplyEvent(WiFiTestTwoNodesInCSRangeRequestEvent):
    '''
    Event containing information about whether two
    nodes are in carrier sensing range or not.
    '''
    def __init__(self, node1, node2, mon_dev, TAU, in_cs):
        super().__init__(node1, node2, mon_dev, TAU)
        self.in_cs = in_cs


class WiFiGetNodesInCSRangeRequestEvent(EventBase):
    '''
    Event to check each nodes pairs whether it is
    in carrier sensing range or not.
    '''
    def __init__(self, mon_dev, TAU):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = TAU


class WiFiTestTwoNodesInCommRangeRequestEvent(EventBase):
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


class WiFiGetNodesInCommRangeRequestEvent(EventBase):
    '''
    Event to check each nodes pairs whether it is
    in communication range or not.
    '''
    def __init__(self, mon_dev, MINPDR):
        super().__init__()
        self.mon_dev = mon_dev
        self.TAU = MINPDR
