from enum import Enum

__author__ = "Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{zubow}@tkn.tu-berlin.de"


''' Possible values: Query, bulk transfer, keepalives, control traffic, stream '''
class Category(Enum):
    QUERY = 1
    BULK_TRANSFER = 2
    KEEP_ALIVES = 3
    CONTROL_TRAFFIC = 4
    STREAM = 5

''' Random bursts, regular bursts, no bursts or bulk (congestion window limited) '''
class Burstiness(Enum):
    RANDOM_BURSTS = 1
    REGULAR_BURSTS = 2
    NO_BURSTS = 3
    BULK = 4

class Timeliness(Enum):
    ''' low delay, low jitter '''
    STREAM = 1
    ''' low delay '''
    INTERACTIVE = 2
    ''' completes eventually '''
    TRANSFER = 3
    ''' only loose time constraint '''
    BACKGROUND_TRAFFIC = 4

class Resilience(Enum):
    ''' Sensitive to connection loss (application fails) '''
    SENSITIVE_CONN_LOSS = 1
    ''' undesirable (loss is fairly inconvenient) '''
    UNDESIRABLE = 2
    ''' resilient (loss is tolerable) '''
    RESILENT = 3

class Direction(Enum):
    ''' downlink '''
    DOWNLINK = 1
    ''' uplink '''
    UPLINK = 2
    ''' DL/UL '''
    DOWNLINK_UPLINK = 3

class ApplicationIntent(object):
    '''
    Application intent class following characteristics from Schmidt et al., 2013.
    '''

    def __init__(self, direction = Direction.DOWNLINK_UPLINK, category = Category.BULK_TRANSFER, burstiness = Burstiness.BULK,
                 timeliness = Timeliness.TRANSFER, resilience = Resilience.UNDESIRABLE, file_size_bytes = 1e6, duration_sec = 1e2, bitrate = 1e4):
        ''' direction: NEW; i.e. not proposed by Schmidt et al. '''
        self.direction = direction
        ''' Query, bulk transfer, keepalives, control traffic, stream '''
        self.category = category
        ''' Random bursts, regular bursts, no bursts or bulk (congestion window limited) '''
        self.burstiness = burstiness
        ''' timeliness, ... '''
        self.timeliness = timeliness
        ''' resilience '''
        self.resilience = resilience
        ''' Number of bytes transferred by the application '''
        self.file_size_bytes = file_size_bytes
        ''' Time between first and last packet in seconds '''
        self.duration_sec = duration_sec
        ''' Size divided by duration in bytes per second '''
        self.bitrate = bitrate

class LongBulkTransferIntent(ApplicationIntent):
    ''' Example for intent of a bulk transfer of 100s duration and total file size of 1 GByte/s '''
    def __init__(self, file_size_bytes = 1e9, duration_sec = 100, bitrate = 1e7):
        super(LongBulkTransferIntent, self).__init__(Direction.DOWNLINK_UPLINK, Category.BULK_TRANSFER,
                                                     Burstiness.BULK, Timeliness.TRANSFER,
                                                     Resilience.UNDESIRABLE, file_size_bytes, duration_sec, bitrate)
        pass

class ControlTrafficIntent(ApplicationIntent):
    ''' Example for endless control traffic intent with low bitrate of 1kByte/s '''
    def __init__(self, bitrate = 1e3):
        super(ControlTrafficIntent, self).__init__(Direction.DOWNLINK_UPLINK, Category.CONTROL_TRAFFIC, Burstiness.NO_BURSTS,
                                                   Timeliness.INTERACTIVE, Resilience.SENSITIVE_CONN_LOSS,
                                                   file_size_bytes=float('inf'), duration_sec=float('inf'), bitrate=bitrate)
        pass
