__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz}@tkn.tu-berlin.de"


def set_channel(channel=1):
    '''
    set_channel 
    ch - channel to set
    '''
    pass

def get_channel():
    '''
        func desc
    '''
    pass

def set_power(power):
    '''
        func desc
    '''
    pass

def get_power():
    '''
        func desc
    '''
    pass

def get_noise():
    '''
        func desc
    '''
    pass

def get_rssi():
    '''
        func desc
    '''
    pass

def get_csi():
    '''
        func desc
    '''
    pass

def get_airtime_utilzation():
    '''
        func desc
    '''
    pass

def set_edca_parameters(queueId, qParam):
    '''
        func desc
    '''
    pass


def getEdcaParameters(queueId):
    '''
        func desc
    '''
    pass

def inject_frame(frame):
    '''
        func desc
    '''
    pass

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

def set_rf_channel(iface, channel):
    '''
        func desc
    '''
    pass

def perform_active_spectral_scanning(iface, freq_list, mode):
    '''
        func desc
    '''
    pass

def playWaveform(iface, freq, power_lvl):
    '''
        func desc
    '''
    pass

def stopWaveform(iface):
    '''
        func desc
    '''
    pass