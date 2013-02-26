from dummydriver import DummyDriver

#singleton pattern
#taked from http://www.python.org/dev/peps/pep-0318/#examples


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Driver(object):
    """Driver singleton for general Driver"""
    def __init__(self):
        self._printer_driver = None

    @property
    def printer_driver(self):
        """if the printer_driver is none returns the dummy printer module"""
        if not self._printer_driver:
            self._printer_driver = DummyDriver()
        return self._printer_driver
