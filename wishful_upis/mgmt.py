from .upi import Upi
from .upi import EventBase

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"

'''
    The WiSHFUL management interface.
'''


class Mgmt(Upi):
    ''' Wishful rule-matching engine '''

    def add_rule(self, rule):
        '''Add new rule to rule-matching engine
        '''
        pass

    def delete_rule(self, rule_id):
        '''Remove rule to rule-matching engine
        '''
        pass

    '''
        Framework functionality
    '''

    def start_local_control_program(self, program_name, program_code):
        '''
        Execute a given control program on loca/remote node.
        '''
        pass

    def stop_local_control_program(self, program_id):
        '''
        Stops execution of a given control program
        on loca/remote node.
        '''
        pass

    def send_msg_to_local_control_program(self, program_id, msg):
        '''
        Hierarchical control function allows the global
        control program to send messages to local control programs.
        '''
        pass

    def transaction_begin(self):
        '''
        Start a transaction
        i.e. all subsequent UPI calls are executed in transactional scope.
        '''
        pass

    def transaction_abort(self):
        '''
        Aborts a running transaction
        i.e. all changes are roll backed.
        '''
        pass

    def transaction_commit(self):
        '''Commit an open transaction.
        '''
        pass


class AgentStartEvent(EventBase):
    def __init__(self):
        super().__init__()


class AgentExitEvent(EventBase):
    def __init__(self):
        super().__init__()


class BrokerDiscoveredEvent(EventBase):
    def __init__(self, dlink, ulink):
        super().__init__()
        self.dlink = dlink
        self.ulink = ulink


class ConnectionEstablishedEvent(EventBase):
    def __init__(self):
        super().__init__()


class ConnectionLostEvent(EventBase):
    def __init__(self):
        super().__init__()


class NewNodeEvent(EventBase):
    def __init__(self):
        super().__init__()


class NodeExitEvent(EventBase):
    def __init__(self, reason):
        super().__init__()
        self.reason = reason


class NodeLostEvent(EventBase):
    def __init__(self, reason):
        super().__init__()
        self.reason = reason


class HelloTimeoutEvent(EventBase):
    def __init__(self):
        super().__init__()


class HelloMsgEvent(EventBase):
    def __init__(self):
        super().__init__()


class ExceptionEvent(EventBase):
    def __init__(self, dest, cmdDesc, msg):
        super().__init__()
        self.dest = dest
        self.cmdDesc = cmdDesc
        self.msg = msg


class CommandEvent(EventBase):
    def __init__(self, ctx):
        super().__init__()
        self.dstNode = None
        self.dstModule = None
        self.ctx = ctx
        self.responseQueue = None


class ReturnValueEvent(EventBase):
    def __init__(self, ctx, msg):
        super().__init__()
        self.dstNode = None
        self.dstModule = None
        self.ctx = ctx
        self.msg = msg

    def to_string(self):
        return str(self.dstNode) + ', ' + str(self.ctx) + ', ' + str(self.msg)


class TimeEvent(EventBase):
    """docstring for TimeEvent"""

    def __init__(self):
        super().__init__()
