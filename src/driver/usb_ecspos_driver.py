import sys
sys.path.append('../libs/pyusb/.')
from usb import core
from usb import util
from dummydriver import DummyDriver


class EscPosDriver(DummyDriver):
    """This class is a merge between the USB lib and escpos driver"""
    def listPrinters(self):
        printers = core.find(find_all=True)  # , bDeviceClass=7)
        for printer in printers:
            print printer.bDeviceClass
            try:
                print util.get_string(printer, 256, 3)
            except:
                print 'dispositivo oculto'
