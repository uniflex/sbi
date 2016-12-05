__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class NetDevice(object):
    '''
    Base Class for all Network Devices, i.e. wired/wireless
    This basic functionality should be available on any device.
    '''

    ''' Device control '''
    def is_up(self):
        '''
        Check state of net device
        '''
        raise NotImplementedError

    def set_up(self):
        '''
        Set-up net device, i.e. if-up
        '''
        raise NotImplementedError

    def set_down(self):
        '''
        Set-down net device, i.e. if-down
        '''
        raise NotImplementedError

    def set_hw_address(self, addr):
        '''
        Set device hardware address, i.e. MAC address
        '''
        raise NotImplementedError

    def get_hw_address(self):
        '''
        Get device hardware address, i.e. MAC address
        '''
        raise NotImplementedError

    def get_info(self, iface=None):
        """
        Get generic information about this device - technology dependent
        """
        raise NotImplementedError

    def set_parameters(self, param_key_values):
        """
        Generic function to set parameter on device.
        """
        raise NotImplementedError

    def get_parameters(self, param_key_list):
        """
        Generic function to get parameter on device.
        """
        raise NotImplementedError

    '''
        Configuration (add/del) of interfaces on that device. Note a network device can have
        multiple interfaces, e.g. WiFi phy0 -> wlan0, mon0, ...
    '''

    def get_interfaces(self):
        '''
        Returns list of network interfaces of that device
        '''
        raise NotImplementedError


    def get_interface_info(self, iface):
        '''
        Returns info about particular network interface
        '''
        raise NotImplementedError


    def add_interface(self, iface, mode, **kwargs):
        '''
        Create wireless interface with name iface and mode
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

    ''' Functionality on interface level '''

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
        e.g. in WiFi network identified by SSID.
        '''
        raise NotImplementedError


    def disconnect(self, iface):
        '''
        Disconnect interface from network
        '''
        raise NotImplementedError


    ''' DEBUG '''
    def debug(self, out):
        '''
        For debug purposes
        '''
        raise NotImplementedError
