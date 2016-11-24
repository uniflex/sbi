from sbi.common.protocol import Protocol

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class NetFilter(Protocol):
    '''
    Network filter tables
    '''

    def clear_nf_tables(self, table="ALL", chain="ALL"):
        """
        Clear all entries in all iptables
        """
        raise NotImplementedError

    def get_nf_table(self, tableName):
        """
        Get specific iptable and its entires
        """
        raise NotImplementedError

    ''' Packet marking - IP ToS '''

    def set_pkt_marking(self, flowId, markId=None,
                        table="mangle", chain="POSTROUTING"):
        """
        Add iptable rule for marking all packets belonging
        to flow identified with given 5-tuple
        """
        raise NotImplementedError

    def del_pkt_marking(self, flowId, markId=None,
                        table="mangle", chain="POSTROUTING"):
        """
        Remove rule used to mark given flow from iptable
        """
        raise NotImplementedError

    ''' Packet mangling - IP ToS '''

    def set_ip_tos(self, flowId, tos, table="mangle", chain="POSTROUTING"):
        """
        Add iptable rule for setting TOS (Type-of-Service)
        field in all packets
        """
        raise NotImplementedError

    def del_ip_tos(self, flowId, tos, table="mangle", chain="POSTROUTING"):
        """
        Remove rule used to setting TOS field from iptable
        """
        raise NotImplementedError
