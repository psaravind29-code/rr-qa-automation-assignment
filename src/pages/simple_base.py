import logging

class SimpleBase:
    """Simple base class without complex dependencies"""
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)