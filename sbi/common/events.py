from uniflex.core.events import EventBase

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"

'''
    Defintion of device events.
'''

class GenericNetDeviceEvent(EventBase):
    ''' base class for all net device events '''
    def __init__(self):
        super().__init__()
        pass

''' Link events '''

class LinkDownEvent(GenericNetDeviceEvent):
    def __init__(self):
        super().__init__()
        pass


class LinkUpEvent(GenericNetDeviceEvent):
    def __init__(self):
        super().__init__()
        pass