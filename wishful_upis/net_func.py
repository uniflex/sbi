from .upi import Upi
from uniflex.core.events import EventBase

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''
Events for performing network-wide operations which go beyond just remote
UPI_R/N calls. Example are estimating the nodes in carrier sensing range,
performing handover operation, etc.
'''

'''
Generic functionality which should be supported by most of the platforms.
'''
class NetFun(Upi):
    def estimate_nodes_in_carrier_sensing_range(self, nodes, interface,
                                                **kwargs):
        """
        Estimate which nodes are in carrier sensing range using UPIs.

        For a network with N nodes all combinations are evaluated,
        i.e. N over 2.

        Note:
           make sure that all nodes are time synchronized.

        Returns:
            list of tuples: In form of (node1, node2, True/False),
            where True/False if nodes are in carrier sensing range
        """
        pass

    def is_in_carrier_sensing_range(self, node1, node2, interface, **kwargs):
        """
        Estimate whether two nodes are in carrier sensing range or not.

        Note:
            it is implemented differently on different platforms
        """
        pass

    def estimate_nodes_in_communication_range(self, nodes, interface,
                                              **kwargs):
        """
        Estimate which nodes are in communication range using UPIs.

        For a network with N nodes all combinations are evaluated,
        i.e. N over 2.

        Note:
            make sure that all nodes are time synchronized.

        Returns:
            list of tuples: In form of (node1, node2, True/False),
            where True/False if nodes are in communication range
        """
        pass

    def is_in_communication_range(self, node1, node2, interface, **kwargs):
        """Estimate whether two nodes are in communication range or not.
        """
        pass


'''
NetworkFunction event base class
'''
class NetFunEvent(EventBase):
    def __init__(self):
        super().__init__()
        pass


'''
    Handover operation
'''
class TriggerHandoverRequestEvent(NetFunEvent):
    '''
    Event to trigger a handover operation.
    '''
    def __init__(self, sta_id, serving_node, target_node, gateway):
        super().__init__()
        self.sta_id = sta_id
        self.serving_node = serving_node
        self.targetAP_node = target_node
        self.gateway = gateway


class TriggerHandoverReplyEvent(NetFunEvent):
    '''
    Reply send after triggering handover operation.
    '''
    def __init__(self, success):
        super().__init__()
        self.success = success
