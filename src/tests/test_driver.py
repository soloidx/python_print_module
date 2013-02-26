import sys
sys.path.append('.')
sys.path.append('../libs/.')

from driver import Driver
from driver.dummydriver import DummyDriver


class TestDriver:
    def test_instance_should_return_a_singleton(self):
        driver_a = Driver()
        driver_b = Driver()
        assert id(driver_a) == id(driver_b)

    def test_printer_driver_should_return_a_driver(self):
        driver = Driver()
        printer_driver = driver.printer_driver
        assert isinstance(printer_driver, DummyDriver)
