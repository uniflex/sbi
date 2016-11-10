from sbi.common.protocol import Protocol

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class Qdisc(Protocol):
    ''' Controlling network emulation (netem),
        i.e. emulation of variable delay, loss,
        duplication and re-ordering.
    '''

    def set_netem_profile(self, iface, profile):
        """
        Set emulation profile in given network interface
        """
        raise NotImplementedError

    def update_netem_profile(self, iface, profile):
        """
        Update emulation profile in given network interface
        """
        raise NotImplementedError

    def remove_netem_profile(self, iface):
        """
        Remove emulation profile from given network interface.
        """
        raise NotImplementedError

    def set_per_link_netem_profile(self, iface, dstIpAddr, profile):
        """
        Set emulation profile in network interface for
        given link identified with destination IP addre
        """
        raise NotImplementedError

    def update_per_link_netem_profile(self, iface, dstIpAddr, profile):
        """
        Update emulation profile in network interface
        for given link identified with MAC addresses.
        """
        raise NotImplementedError

    def remove_per_link_netem_profile(self, iface, dstIpAddr):
        """
        Remove emulation profile from network interface
        for given link identified with MAC addresses.
        """
        raise NotImplementedError

    ''' Controlling queuing disciplines '''

    def install_egress_scheduler(self, iface, scheduler):
        """
        Install Egress Scheduler in given network interface.
        """
        raise NotImplementedError

    def remove_egress_scheduler(self, iface):
        """
        Remove Egress Scheduler from network interface
        """
        raise NotImplementedError
