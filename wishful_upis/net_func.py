__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


def transaction_begin():
    '''
        func desc
    '''
    pass


def transaction_abort():
    '''
        func desc
    '''
    pass


def transaction_commit():
    '''
        func desc
    '''
    pass


def perform_handover(interface, servingNode, targetNode, device_mac_addr, **kwargs):
    '''
    Performing an handover operation. Note: this is not supported on any wireless technology.
    - 802.11 - in infrastructure mode an STA can be handovered; not supported in 802.11 adhoc
    - other technologies?
    '''
    pass


def is_associated_with(nodes, interface, device_mac_addr):
    '''
    Estimate the AP/BS with which a given device is associated. Note: this is not supported on any wireless technology.
    - enabled om 802.11 infrastructure mode
    - other technologies?
    '''
    pass


def estimate_nodes_in_carrier_sensing_range(nodes, interface, **kwargs):
    """
    Estimate which nodes are in carrier sensing range using UPIs.
    For a network with N nodes all combinations are evaluated, i.e. N over 2.
    Note: make sure that all nodes are time synchronized.
    @return a list of triples (node1, node2, True/False) True/False if nodes are in carrier sensing range
    """
    pass


def is_in_carrier_sensing_range(node1, node2, interface, **kwargs):
    """
    Estimate whether two nodes are in carrier sensing range or not.
    Note: it is implemented differently on different platforms
    """
    pass


def estimate_nodes_in_communication_range(self, nodes, interface, **kwargs):
    """
    Estimate which nodes are in communication range using UPIs.
    For a network with N nodes all combinations are evaluated, i.e. N over 2.
    Note: make sure that all nodes are time synchronized.
    @return a list of triples (node1, node2, True/False) True/False if nodes are in communication range
    """


def is_in_communication_range(node1, node2, interface, **kwargs):
    """
    Estimate whether two nodes are in communication range or not.
    """
    pass
