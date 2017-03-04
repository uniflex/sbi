from sbi.common.net_device import NetDevice

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class RadioNetDevice(NetDevice):
    '''
    Base Class for all Radio (Wireless) Network Devices. It inherits functionality from NetDevice.
    '''

    '''
        Activation and deactivation of custom radio programs. This is mostly for SDR platforms
        (GnuRadio, ...).
    '''

    def activate_radio_program(self, radio_program_id=None, radio_program=None, iface=None):
        """
        Activates the given radio program, i.e. is loaded and started.
        """
        raise NotImplementedError

    def update_radio_program(self, radio_program_id=None, radio_program=None, iface=None):
        """
        Updates/replaces running radio program.
        """
        raise NotImplementedError

    def deactivate_radio_program(self, radio_program_id=None, do_pause=False):
        """
        Deactivates the given radio program, i.e. it is stopped.
        """
        raise NotImplementedError

    def get_running_radio_program(self):
        """
        Returns the identifier of the running radio program or None.
        """
        raise NotImplementedError

    ''' Transmission of radio waveforms (just PHY, no MAC). This is mostly supported by SDR platforms '''

    def play_waveform(self, **kwargs):
        '''
        Starts transmission of radio waveform (just PHY, no MAC).
        '''
        raise NotImplementedError

    def stop_waveform(self):
        '''
        Stops transmission of radio waveform.
        '''
        raise NotImplementedError

    ''' Spectral scanning capabilities '''

    def spectral_scan_start(self, iface, freq_list, **kwargs):
        '''
        Perform spectral scanning. This is mostly supported by SDR but sometimes also COTS hardware.

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

    def is_spectral_scan_running(self):
        '''
        Check if spectral scanning is running.

        Returns:
            True or False
        '''
        raise NotImplementedError

    ''' Transmit power control '''

    def set_tx_power(self, power_dBm, iface):
        '''
        Set transmission power for the device. Note: sometimes you can set per interface.
        '''
        raise NotImplementedError

    def get_tx_power(self, iface):
        '''
        Get transmission power of device/interface.
        '''
        raise NotImplementedError

    def get_noise(self):
        '''
        Returns the noise floor.
        '''
        raise NotImplementedError


    ''' For radio technologies the regulation domain need sometimes to be set '''

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
