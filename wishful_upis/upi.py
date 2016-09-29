__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


class RegisterLeafClasses(type):
    def __init__(cls, name, bases, nmspc):
        super(RegisterLeafClasses, cls).__init__(name, bases, nmspc)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        cls.registry.add(cls)
        cls.registry -= set(bases)  # Remove base classes

    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)

    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])


class Upi(object):
    __metaclass__ = RegisterLeafClasses


class AttributeBase(object):
    # Nothing yet
    pass


class FunctionBase(object):
    # Nothing yet
    pass


class EventBase(object):
    """ event cannot be parametrized, user may only start it once"""

    def __init__(self):
        super().__init__()
        self.srcNode = None
        self.srcModule = None
        self.node = None
        self.device = None


class ServiceBase(object):
    # service may be parametrized, it possible it may be
    # started multiple times with different parameters
    pass
