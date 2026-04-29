import unittest
from src.logical_clock import LogicalClock


class TestLogicalClock(unittest.TestCase):

    def setUp(self):
        self.lc = LogicalClock()

    # clock inicia em zero
    def test_initial_clock_is_zero(self):
        self.assertEqual(self.lc.time, 0)

    # evento local incrementa o clock
    def test_send_tick_increments_clock(self):
        self.lc.send_tick()
        self.assertEqual(self.lc.time, 1)

    # recebimento de tempo maior sincroniza e incrementa
    def test_receive_tick_with_greater_time(self):
        self.lc.receive_tick(10)
        self.assertEqual(self.lc.time, 11)

    # recebimento de tempo menor ainda incrementa corretamente
    def test_receive_tick_with_smaller_time(self):
        self.lc.send_tick()  # 1
        self.lc.receive_tick(0)
        self.assertEqual(self.lc.time, 2)


if __name__ == '__main__':
    unittest.main()