import unittest
from src.logical_clock import LogicalClock

class TestLogicalClock(unittest.TestCase):
    def setUp(self):
        self.lc = LogicalClock()

    def test_initial_clock_is_zero(self):
        self.assertEqual(self.lc.time, 0)

    def test_send_tick_increments_clock(self):
        self.lc.send_tick()
        self.assertEqual(self.lc.time, 1)

    def test_receive_tick_sync(self):
        self.lc.receive_tick(10)
        self.assertEqual(self.lc.time, 11)