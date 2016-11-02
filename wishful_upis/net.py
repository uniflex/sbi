from .upi import Upi
from wishful_agent.core.events import EventBase

__author__ = "Piotr Gawlowicz, Anatolij Zubow, Mikolaj Chwalisz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow, chwalisz}@tkn.tu-berlin.de"

'''
    The WiSHFUL network control interface, UPI_N, for
    configuration/monitoring of the higher layers of
    the network protocol stack (upper MAC and higher).
'''

# Generic API to control the higher layers, i.e. key-value configuration.


class Network(Upi):
    def set_parameters(self, param_key_values_dict):
        """
        The UPI_N interface is able to configure the protocol
        (routing, transport, application) behavior by changing parameters.
        Parameters correspond to the  variables used in the protocols.
        This function (re)set the value(s) of the parameters specified
        in the dictionary argument. The list of available parameters
        supported by all platforms/OS are defined in this module.
        Parameters specific to a subgroup of platforms/OS are defined in
        the corresponding submodules. A list of supported parameters can
        be dynamically obtained using the get_info function on each module.

        Examples:
            .. code-block:: python

                >> param_key_values = {ROUTING_MAX_TTL : 5}
                >> result = control_engine.net.set_parameters(param_key_values)
                >> print result
                {ROUTING_MAX_TTL : 0}

        Args:
            param_key_values_dict (dict): dictionary containing
                the key (string) value (any) pairs for each parameter.
                An example is:
                {CSMA_CW : 15, CSMA_CW_MIN : 15, CSMA_CW_MAX : 15}

        Returns:
            dict: A dictionary containing key (string name)
                error (0 = success, 1=fail, +1=error code)
                pairs for each parameter.
        """
        return

    def get_parameters(self, param_key_list):
        """
        Get the parameter on higher layers of protocol
        stack (higher MAC and above)

        Args:
           param_key: the parameter identified by this key.

        Returns:
           the parameter value
        """
        return

    def get_measurements(self, measurement_key_list):
        """
        Examples:
            .. code-block:: python

                >> measurement_keys = [NUM_FREEZING_COUNT]
                >> result = control_engine.net.iface("wlan0").get_measurements(measurement_keys)
                >> print result
                {UPI_RN.NUM_FREEZING_COUNT : 150}

        Args:
            measurement_key_list (list): list of requested measurements,
                                         an example of is
                                         [NUM_FREEZING_COUNT, TX_ACTIVITY].

        Returns:
            dict: A dictionary containing key (string name)
                  and values of the requested measurements.
        """
        return

    def get_network_info(self):
        return

    ''' App layer - set-up of packet flows '''

    def install_application(self, app_desc):
        '''
        Install application in node. Possible applications
        are IperfClient and IperfServer.
        '''
        return

    def start_application(application_id):
        '''
        Start previously installed application in node
        '''
        return

    def stop_application(application_id):
        '''
        Stop running application in node
        '''
        return

    ''' Network layer - routing, networking, etc. '''

    def get_ifaces(self):
        '''
        Returns list of interface names,
        e.g. ['lo', 'ens33', 'lxcbr0', 'ovs-system'].
        '''
        return

    def get_iface_hw_addr(self, iface):
        '''
        Returns the hardware address
        (MAC address) of a given interface.
        '''
        return

    def set_ip_address(self, iface, ip_address):
        '''
        Set IP address for given interface
        '''
        pass

    def get_iface_ip_addr(self, iface):
        '''
        Returns the IP address of a given interface.
        '''
        return

    def set_ARP_entry(self, iface, mac_addr, ip_addr):
        '''
        Manipulates the entries in the ARP cache.
        '''
        return

    def change_routing(self, current_gw_ip_addr,
                       new_gw_ip_addr, device_ip_addr):
        '''
        Controls the routing.
        '''
        return

    ''' Upper MAC layer - injection and sniffing of layer2 traffic '''

    def gen_layer2_traffic(self, iface, num_packets, pinter,
                           max_phy_broadcast_rate_mbps=None, **kwargs):
        '''
        Inject layer2 traffic into network device.
        '''
        return

    def inject_frame(self, iface, frame, is_layer_2_packet,
                     tx_count=1, pkt_interval=1):
        '''
        Inject L2/L3 frame injection into the protocol stack
        '''
        return

    def sniff_layer2_traffic(self, iface, sniff_timeout, **kwargs):
        '''
        Layer-2 packet sniffing from network device.
        '''
        return

    ''' Controlling network emulation (netem),
        i.e. emulation of variable delay, loss,
        duplication and re-ordering.
    '''

    def set_netem_profile(self, iface, profile):
        """
        Set emulation profile in given network interface
        """
        return

    def update_netem_profile(self, iface, profile):
        """
        Update emulation profile in given network interface
        """
        return

    def remove_netem_profile(self, iface):
        """
        Remove emulation profile from given network interface.
        """
        return

    def set_per_link_netem_profile(self, iface, dstIpAddr, profile):
        """
        Set emulation profile in network interface for
        given link identified with destination IP addre
        """
        return

    def update_per_link_netem_profile(self, iface, dstIpAddr, profile):
        """
        Update emulation profile in network interface
        for given link identified with MAC addresses.
        """
        return

    def remove_per_link_netem_profile(self, iface, dstIpAddr):
        """
        Remove emulation profile from network interface
        for given link identified with MAC addresses.
        """
        return

    ''' Controlling queuing disciplines '''

    def install_egress_scheduler(self, iface, scheduler):
        """
        Install Egress Scheduler in given network interface.
        """
        return

    def remove_egress_scheduler(self, iface):
        """
        Remove Egress Scheduler from network interface
        """
        return

    ''' Network filter tables '''

    def clear_nf_tables(self, table="ALL", chain="ALL"):
        """
        Clear all entries in all iptables
        """
        return

    def get_nf_table(self, tableName):
        """
        Get specific iptable and its entires
        """
        return

    ''' Packet marking - IP ToS '''

    def set_pkt_marking(self, flowId, markId=None,
                        table="mangle", chain="POSTROUTING"):
        """
        Add iptable rule for marking all packets belonging
        to flow identified with given 5-tuple
        """
        return

    def del_pkt_marking(self, flowId, markId=None,
                        table="mangle", chain="POSTROUTING"):
        """
        Remove rule used to mark given flow from iptable
        """
        return

    ''' Packet mangling - IP ToS '''

    def set_ip_tos(self, flowId, tos, table="mangle", chain="POSTROUTING"):
        """
        Add iptable rule for setting TOS (Type-of-Service)
        field in all packets
        """
        return

    def del_ip_tos(self, flowId, tos, table="mangle", chain="POSTROUTING"):
        """
        Remove rule used to setting TOS field from iptable
        """
        return


"""
Application classes:
 (1) iperf

 TODO: move me to app.py
"""


class Application(object):
    def __init__(self):
        # do not include logging here, beacuse this cannot be pickled
        self.startTime = 0
        self.type = None
        self.resultReportInterval = None
        self.port = 5001
        self.protocol = "TCP"
        self.tcpWindow = None

        self.results = []
        self.newResult = False

    def setStartTime(self, value):
        self.startTime = value

    def setProtocol(self, protocol):
        self.protocol = protocol

    def setPort(self, port):
        self.port = port

    def collectResults(self, result):
        self.results.append(result)
        self.newResult = True

    def isNewResult(self):
        return self.newResult

    def getResult(self):
        retValue = self.results[0]
        del self.results[0]
        return retValue


class ServerApplication(Application):
    def __init__(self):
        super(ServerApplication, self).__init__()
        self.type = "Server"
        self.bind = None

    def setBind(self, bind):
        self.bind = bind


class ClientApplication(Application):
    def __init__(self):
        super(ClientApplication, self).__init__()
        self.type = "Client"
        self.destination = None
        self.udpBandwidth = "1M"
        self.dualtest = False
        self.dataToSend = None
        self.transmissionTime = None
        self.frameLen = None

    def setDestination(self, dest):
        self.destination = dest

    def setBandwidth(self, band):
        self.udpBandwidth = band

    def setDualTest(self, value):
        self.dualtest = value

    def setDataSize(self, value):
        self.dataToSend = value

    def setTransmissionTime(self, value):
        self.transmissionTime = value

    def setFrameLen(self, value):
        self.frameLen = value


class RawperfClientApplication(Application):
    def __init__(self):
        super(RawperfClientApplication, self).__init__()
        self.type = "RawperfClient"
        self.destination = None
        self.udpBandwidth = "1M"
        self.dualtest = False
        self.dataToSend = None
        self.transmissionTime = None
        self.frameLen = None
        self.waitTime = 1

    def setWaitTime(self, value):
        self.waitTime = value

    def setDestination(self, dest):
        self.destination = dest

    def setBandwidth(self, band):
        self.udpBandwidth = band

    def setDualTest(self, value):
        self.dualtest = value

    def setDataSize(self, value):
        self.dataToSend = value

    def setTransmissionTime(self, value):
        self.transmissionTime = value

    def setFrameLen(self, value):
        self.frameLen = value


class FlowId(object):
    def __init__(self, srcAddress=None, dstAddress=None,
                 prot=None, srcPort=None, dstPort=None):
        self.srcAddress = srcAddress
        self.dstAddress = dstAddress
        self.prot = prot
        self.srcPort = srcPort
        self.dstPort = dstPort

'''
IP tables classes
'''


class SimpleMatch(object):
    def __init__(self, match):
        self.name = match.name


class SimpleTarget(object):
    def __init__(self, target):
        self.name = target.name


class SimplePolicy(object):
    def __init__(self, policy):
        self.name = policy.name


class SimpleRule(object):
    def __init__(self, rule):
        self.protocol = rule.protocol
        self.src = rule.src
        self.dst = rule.dst
        self.in_interface = rule.in_interface
        self.out_interface = rule.out_interface
        self.fragment = rule.fragment

        (packets, byte) = rule.get_counters()
        self.pktCounter = packets
        self.byteCounter = byte

        self.matches = []
        for match in rule.matches:
            self.matches.append(SimpleMatch(match))

        self.target = SimpleTarget(rule.target)


class SimpleChain(object):
    def __init__(self, chain):
        self.name = chain.name

        (packets, byte) = chain.get_counters()
        self.pktCounter = packets
        self.byteCounter = byte

        self.rules = []
        for rule in chain.rules:
            self.rules.append(SimpleRule(rule))


class SimpleTable(object):
    def __init__(self, table):
        self.name = table.name
        self.chains = []
        for chain in table.chains:
            self.chains.append(SimpleChain(chain))


'''
    Network event base class
'''


class NetEvent(EventBase):
    def __init__(self):
        super().__init__()
        pass


'''
    List of network events
'''
