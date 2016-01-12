import warnings
import pkg_resources
__version__ = pkg_resources.get_distribution("bika.bbk").version

# import this to create messages in the bika domain.
from zope.i18nmessageid import MessageFactory
bbkMessageFactory = MessageFactory('bika.bbk')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
