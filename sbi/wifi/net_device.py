from sbi.radio_device.net_device import RadioNetDevice

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class WiFiNetDevice(RadioNetDevice):
    '''
    Base Class for all WiFi Network Device, i.e. WiFi COTS (Atheros, Broadcom, etc.)
    and SDR (GnuRadio, NI-SDR)
    '''

    '''
        PHY layer
    '''

    def get_airtime_utilization(self):
        '''
        Returns the relative time the spectrum is occupied.
        '''
        raise NotImplementedError

    def set_channel(self, channel, iface, **kwargs):
        '''
        Set channel for given interface, i.e. center frequency of the primary band. Secondary bands are given in
        optional arguments

        Args:
            channel: channel to set
            iface: interface
        '''
        raise NotImplementedError

    def get_channel(self, iface, **kwargs):
        '''
        Get channel of given interface,
        i.e. center frequency of the primary band or optionally secondaries.

        Args:
            iface: interface
        '''
        raise NotImplementedError

    def set_modulation_rate(self, ifaceName,
                            is5Ghzband, isLegacy, rate_Mbps_or_ht_mcs):
        '''
        Sets a fix PHY modulation rate:
        - legacy: bitrate
        - 11n/ac: ht_mcs
        '''
        raise NotImplementedError

    def configure_radio_sensitivity(self, ani_mode):
        '''
        Configuring the receiving sensitivity of the IEEE 802.11 radio.
        '''
        raise NotImplementedError

    ''' Per flow transmit power control '''

    def set_per_flow_tx_power(self, iface, flowId, txPower):
        """
        Sets for a flow identified by an 5-tuple
        (IP header) the transmit power to be used.
        """
        raise NotImplementedError

    def clean_per_flow_tx_power_table(self, iface):
        """
        Remove any entries in the transmit power table.
        """
        raise NotImplementedError

    def get_per_flow_tx_power(self, flowId):
        """
        Return the transmit power level used for the given flow.
        """
        raise NotImplementedError

    def get_per_flow_tx_power_table(self, iface):
        """
        Return the whole transmit power table.
        """
        raise NotImplementedError

    '''
        Channel state information and spectrum scanning capabilities.
    '''

    def get_csi(self, num_samplesi, withMetaData=False):
        '''
        Return CSI values; i.e. the next num_samples CSI samples from the driver.
        '''
        raise NotImplementedError

    def csi_collector_start(self, ival):
        '''
        Start CSI service to receives CSI samples from wifi driver.
        '''
        raise NotImplementedError

    def csi_collector_stop(self):
        '''
        Stops CSI service.
        '''
        raise NotImplementedError

    def is_csi_collector_running(self):
        '''
        Is CSI collector running
        '''
        raise NotImplementedError


    def is_rf_blocked(self, iface):
        '''
        Returns information about rf blocks (Soft Block, Hard Block)
        '''
        raise NotImplementedError

    def rf_unblock(self, iface):
        '''
        Turn off the softblock
        '''
        raise NotImplementedError

    '''
        MAC layer
    '''
    def set_mac_access_parameters(self, iface, queueId, qParam):
        '''
        MAC access parameters in 802.11e: the configuration
        of the access categories
        '''
        raise NotImplementedError

    def get_mac_access_parameters(self, queueId):
        '''
        MAC access parameters: in 802.11e:
        the configuration of the access categories
        '''
        raise NotImplementedError

    def set_power_management(self, iface, value):
        '''
        Sets power management
        '''
        raise NotImplementedError

    def get_power_management(self, iface):
        '''
        Get power management
        '''
        raise NotImplementedError

    def set_retry_short(self, iface, value):
        '''
        Sets retry short
        '''
        raise NotImplementedError

    def get_retry_short(self, iface):
        '''
        Get retry short
        '''
        raise NotImplementedError

    def set_retry_long(self, iface, value):
        '''
        Sets retry long
        '''
        raise NotImplementedError

    def get_retry_long(self, iface):
        '''
        Get retry long
        '''
        raise NotImplementedError

    def set_rts_threshold(self, iface, value):
        '''
        Sets RTS threshold
        '''
        raise NotImplementedError

    def get_rts_threshold(self, iface):
        '''
        Get RTS threshold
        '''
        raise NotImplementedError

    def set_fragmentation_threshold(self, iface, value):
        '''
        Sets framgmentation threshold
        '''
        raise NotImplementedError

    def get_fragmentation_threshold(self, iface):
        '''
        Get framgmentation threshold
        '''
        raise NotImplementedError

    def get_supported_modes(self, iface):
        '''
        Get supported WiFi modes
        '''
        raise NotImplementedError

    def get_supported_swmodes(self, iface):
        '''
        Get supported WiFi software modes
        '''
        raise NotImplementedError

    def get_rf_band_info(self, iface):
        '''
        Get info about supported RF bands
        '''
        raise NotImplementedError

    def get_ciphers(self, iface):
        '''
        Get info about supported ciphers
        '''
        raise NotImplementedError

    def get_supported_wifi_standards(self, iface):
        '''
        Get info about supported WiFi standards, i.e. 802.11a/n/g/ac/b
        '''
        raise NotImplementedError

    def get_wifi_mode(self, iface):
        '''
        Get the mode of the interface: managed, monitor, ...
        '''
        raise NotImplementedError

    '''
        Upper MAC layer
    '''

    def start_ap(self, iface, config):
        '''
        Set hostapd configuration, provide functionality
        to setting Access Point station
        Start hostapd, provide functionality to run Access Point
        '''
        raise NotImplementedError

    def stop_ap(self):
        '''
        Stop hostapd, provide functionality to stop Access Point
        '''
        raise NotImplementedError

    def add_device_to_blacklist(self, iface, device_mac_addr):
        '''
        Add the given device to the blacklist

        - 802.11 AP: the device is a client and the result of blacklisting
        is that the client cannot associate with this node.
        '''
        raise NotImplementedError

    def remove_device_from_blacklist(self, iface, device_mac_addr):
        '''
        Remove the given device from the blacklist

        - 802.11 AP: the device is a client and the result of unblacklisting
        is that the client can associate with this node.
        '''
        raise NotImplementedError

    def disconnect_device(self, iface, device_mac_addr):
        '''
        Disconnects the given device from this node

        - 802.11 AP: send dissassociation request to client device
        - 802.11 adhoc: no meaning
        '''
        raise NotImplementedError

    def register_new_device(self, iface, sta_mac_addr):
        '''
        Register the given device

        - 802.11 AP: the device is associated with this AP.
        '''
        raise NotImplementedError

    def trigger_channel_switch_in_device(self, iface,
                                         device_mac_addr, target_channel,
                                         serving_channel, **kwargs):
        '''
        Trigger a channel switch in the device connected to this node

        - 802.11 AP: send channel switch announcement to client STA,
        '''
        raise NotImplementedError

    def get_info_of_connected_devices(self, iface):
        '''
        Returns information about associated devices

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_inactivity_time_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - inactivity time

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_avg_sigpower_of_connected_devices(self, iface):
        '''
        Returns information about associated devices,
        i.e. link average signal power

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_sigpower_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - link signal power

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_tx_retries_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx retries

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_tx_packets_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx packets

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_tx_failed_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx failed

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_tx_bytes_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx bytes

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_tx_bitrate_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - tx bitrate

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_rx_bytes_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - rx bytes

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_rx_packets_of_connected_devices(self, iface):
        '''
        Returns information about associated devices - rx packets

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_authorized_connected_device(self, iface):
        '''
        Returns information about associated devices - is authorized

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_authenticated_connected_device(self, iface):
        '''
        Returns information about associated devices - is authenticated

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_used_preamble_connected_device(self, iface):
        '''
        Returns information about associated devices - preamble used

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_mfp_connected_device(self, iface):
        '''
        Returns information about associated devices - MFP

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_wmm_wme_connected_device(self, iface):
        '''
        Returns information about associated devices - WMM/WME

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    def get_tdls_peer_connected_device(self, iface):
        '''
        Returns information about associated devices - TDLS peer

        - 802.11 AP: info about the associated client devices of that AP.
        '''
        raise NotImplementedError

    '''
        Upper MAC layer - injection and sniffing of layer2 traffic
    '''

    def gen_layer2_traffic(self, iface, num_packets, pkt_interval,
                           max_phy_broadcast_rate_mbps, **kwargs):
        '''
        Inject layer2 traffic into network device.
        '''
        raise NotImplementedError

    def stop_gen_layer2_traffic(self, iface, num_packets, pinter,
                                max_phy_broadcast_rate_mbps=None, **kwargs):
        '''
        Inject layer2 traffic into network device.
        '''
        raise NotImplementedError

    def start_l2_sniffing(self, iface, sniff_timeout, **kwargs):
        '''
        Layer-2 packet sniffing from network device.
        '''
        raise NotImplementedError

    def stop_l2_sniffing(self, iface, sniff_timeout, **kwargs):
        '''
        Layer-2 packet sniffing from network device.
        '''
        raise NotImplementedError

    def inject_frame(self, iface, frame, is_layer_2_packet,
                     tx_count=1, pkt_interval=1):
        '''
        Inject L2/L3 frame injection into the protocol stack
        '''
        raise NotImplementedError
