__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


'''
IEEE 802.15.4 protocol family

The protocol-specific definition of the WiSHFUL radio control interface, UPI_R,
for configuration/monitoring of the lower layers of the network protocol stack
(lower MAC and PHY).

'''

IEEE802154_macMaxBE = 1
IEEE802154_macMaxCSMABackoffs = 2
IEEE802154_macMaxFrameRetries = 3
IEEE802154_macMinBE = 4
IEEE802154_macPANId = 5
IEEE802154_macShortAddress = 6
IEEE802154_macExtendedAddress = 7
IEEE802154_phyCurrentChannel = 8
IEEE802154_phyTXPower = 9
IEEE802154e_macHoppingSequenceLength = 10
IEEE802154e_macHoppingSequenceList = 11
IEEE802154e_macSlotframeSize = 12
IEEE802154e_macTimeslot = 13
IEEE802154e_macTsTimeslotLength = 14
TAISC_ACTIVERADIOPROGRAM = 15
IEEE802154_MACSTATS = 16
IEEE802154_event_macStats = 17
