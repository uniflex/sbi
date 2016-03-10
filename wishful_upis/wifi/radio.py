__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The WiSHFUL radio control interface, UPI_R, for configuration/monitoring of the lower
    layers of the network protocol stack (lower MAC and PHY).
'''

'''
    MAC layer
'''

def install_mac_processor(interface, mac_profile):
    '''
        func desc
    '''
    pass


def update_mac_processor(interface, mac_profile):
    '''
        func desc
    '''
    pass


def uninstall_mac_processor(interface, mac_profile):
    '''
        func desc
    '''
    pass


def set_mac_access_parameters(queueId, qParam):
    '''
        MAC access parameters:
        - in 802.11e: the configuration of the access categories
    '''
    pass


def get_mac_access_parameters(queueId):
    '''
        MAC access parameters:
        - in 802.11e: the configuration of the access categories
    '''
    pass

'''
    PHY layer
'''

def perform_spectral_scanning(iface, freq_list, mode):
    '''
        Perform spectral scanning. Returns a power value for each frequency bin.
    '''
    pass


def get_airtime_utilization():
    '''
        Returns the relative time the spectrum is empty.
    '''
    pass


def play_waveform(iface, freq, power_lvl, **kwargs):
    '''
        Starts transmitting a specified waveform (just PHY, no MAC).
    '''
    pass


def stop_waveform(iface, **kwargs):
    '''
        Stops transmitting a specified waveform.
    '''
    pass


def set_channel(channel):
    '''
    Set channel, i.e. center frequency
    ch - channel to set
    '''
    pass


def get_channel():
    '''
        func desc
    '''
    pass


def get_rssi():
    '''
        func desc
    '''
    pass


def get_noise():
    '''
        func desc
    '''
    pass


def configure_radio_sensitivity(phy_dev, **kwargs):
    '''
        Configuring the receiving sensitivity of the radio:
         - IEEE 802.11: carrier sensing sensitivity (Atheros chipsets: ANI)
    '''
    pass
