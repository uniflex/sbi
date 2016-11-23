from uniflex.core.events import ParameterBase

__author__ = "Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{zubow}@tkn.tu-berlin.de"


'''
    Defintion of WiFi specific parameters used in function calls.
'''

class GenericWiFiParameter(ParameterBase):
    ''' base class for all WiFI parameters '''
    def __init__(self):
        super().__init__()
        pass

"""
    A hybrid TDMA CSMA MAC based on Atheros and ath9k wifi driver
"""
class HMACConfigParam(GenericWiFiParameter):
    def __init__(self, no_slots_in_superframe, slot_duration_ns):
        super().__init__()
        self.name = "HMAC_conf"
        self.desc = "works w/ patched ath9k driver"
        self.mNo_slots_in_superframe = no_slots_in_superframe
        self.mSlot_duration_ns = slot_duration_ns
        self.acs = []
        for ii in range(no_slots_in_superframe):
            self.acs.append(None)

    def getNumSlots(self):
        return self.mNo_slots_in_superframe

    def addAccessPolicy(self, slot_nr, ac):
        self.acs[slot_nr] = ac

    def getAccessPolicy(self, slot_nr):
        return self.acs[slot_nr]

    def getSlotDuration(self):
        return self.mSlot_duration_ns

    def createConfString(self):
        # create configuration string to be passed to HMAC daemon
        conf_str = None
        for ii in range(self.getNumSlots()):  # for each slot
            ac = self.getAccessPolicy(ii)
            entries = ac.getEntries()

            for ll in range(len(entries)):
                entry = entries[ll]

                # slot_id, mac_addr, tid_mask
                if conf_str is None:
                    conf_str = str(ii) + "," + str(entry[0]) + "," + str(entry[1])
                else:
                    conf_str = conf_str + "#" + str(ii) + "," + str(entry[0]) + "," + str(entry[1])

        return conf_str

    def createAllowAllConfString(self):
        # generate configuration string
        conf_str = None
        for ii in range(self.getNumSlots()):  # for each slot
            # slot_id, mac_addr, tid_mask
            if conf_str is None:
                conf_str = str(ii) + "," + 'FF:FF:FF:FF:FF:FF' + "," + str(255)
            else:
                conf_str = conf_str + "#" + str(ii) + "," + 'FF:FF:FF:FF:FF:FF' + "," + str(255)

        return conf_str


    def printConfiguration(self):
        s = '['
        for ii in range(self.getNumSlots()):
            s = s + str(ii) + ': ' + self.getAccessPolicy(ii).printConfiguration() + "\n"
        s = s + ']'
        return s

"""
    AccessPolicy for each slot
"""
class HMACAccessPolicyParam(GenericWiFiParameter):

    def __init__(self):
        super().__init__()
        self.entries = []

    def disableAll(self):
        self.entries = []

    def allowAll(self):
        self.entries = []
        self.entries.append(('FF:FF:FF:FF:FF:FF', 255))

    def addDestMacAndTosValues(self, dstHwAddr, *tosArgs):
        """add destination mac address and list of ToS fields
        :param dstHwAddr: destination mac address
        :param tosArgs: list of ToS values to be allowed here
        """
        tid_map = 0
        for ii in range(len(tosArgs)):
            # convert ToS into tid
            tos = tosArgs[ii]
            skb_prio = tos & 30 >> 1
            tid =skb_prio & 7
            tid_map = tid_map | 2**tid

        self.entries.append((dstHwAddr, tid_map))

    def getEntries(self):
        return self.entries

    def printConfiguration(self):
        s = ''
        for ii in range(len(self.entries)):
            s = str(self.entries[ii][0]) + "/" + str(self.entries[ii][1]) + "," + s
        return s
