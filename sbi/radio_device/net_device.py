from sbi.common.net_device import NetDevice

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class RadioNetDevice(NetDevice):
    '''
    Base Class for Radio Network Device
    '''
    # Activation and deactivation of radio programs.

    def activate_radio_program(self, radio_program_id, **kwargs):
        """
        desc
        """
        raise NotImplementedError

    def deactivate_radio_program(self, radio_program_id):
        """
        desc
        """
        raise NotImplementedError

    def get_running_radio_program(self):
        """
        desc
        """
        raise NotImplementedError

    ''' Transmission of radio waveform (no MAC) '''

    def play_waveform(self, **kwargs):
        '''
        Starts transmitting a radio waveform (just PHY, no MAC).
        '''
        raise NotImplementedError

    def stop_waveform(self):
        '''
        Stops transmitting a radio waveform.
        '''
        raise NotImplementedError

    def spectral_scan_start(self, iface, freq_list, **kwargs):
        '''
        Perform spectral scanning.

        Returns:
            Power value for each frequency bin.
        '''
        raise NotImplementedError

    def spectral_scan_stop(self):
        '''
        Perform spectral scanning.

        Returns:
            Power value for each frequency bin.
        '''
        raise NotImplementedError

    def set_tx_power(self, power_dBm, iface):
        '''
        Set transmission power for a give interface
        '''
        raise NotImplementedError

    def get_tx_power(self, iface):
        '''
        Get transmission power of given interface
        '''
        raise NotImplementedError

    def get_noise(self):
        '''
        Returns the noise floor measured by the wireless driver.
        '''
        raise NotImplementedError

    def get_interfaces(self):
        '''
        Returns all network interfaces of device
        '''
        raise NotImplementedError

    def get_interface_info(self, iface):
        '''
        Returns info on network interface
        '''
        raise NotImplementedError

    def add_interface(self, iface, mode, **kwargs):
        '''
        Add wireless interface with iface and mode
        '''
        raise NotImplementedError

    def del_interface(self, iface):
        '''
        Delete interface by name
        '''
        raise NotImplementedError

    def set_interface_up(self, iface):
        '''
        Set interface UP
        '''
        raise NotImplementedError

    def set_interface_down(self, iface):
        '''
        Set interface DOWN
        '''
        raise NotImplementedError

    def is_interface_up(self, iface):
        '''
        Check if interface is up
        '''
        raise NotImplementedError

    def get_link_info(self, iface):
        '''
        Get link info of interface
        '''
        raise NotImplementedError

    def is_connected(self, iface):
        '''
        Check if interface is in connected state
        '''
        raise NotImplementedError

    def connect(self, iface, **kwargs):
        '''
        Connects a given interface to some network
        e.g. WiFi network identified by SSID.
        '''
        raise NotImplementedError

    def disconnect(self, iface):
        '''
        Disconnect interface
        '''
        raise NotImplementedError

    def get_regulatory_domain(self):
        '''
        Returns the regulatory domain (for all interfaces)
        '''
        raise NotImplementedError

    def set_regulatory_domain(self, new_domain):
        '''
        Sets the regulatory domain (for all interfaces)
        '''
        raise NotImplementedError
