from uniflex.core.events import EventBase

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class PacketLossEvent(EventBase):
    def __init__(self):
        super().__init__()
        pass


class RssiSampleEvent(EventBase):
    def __init__(self, ta, rssi):
        super().__init__()
        self.ta = ta
        self.receiverUuid = None
        self.rssi = rssi


class SpectralScanSampleEvent(EventBase):
    def __init__(self, sample):
        super().__init__()
        self.sample = sample

    def serialize(self):
        return {"sample": self.sample}

    @classmethod
    def parse(cls, buf):
        sample = buf.get("sample", None)
        return cls(sample)
