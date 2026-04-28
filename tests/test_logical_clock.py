import unittest
from src.logical_clock import LogicalClock

class TestLogicalClock(unittest.TestCase):

    def setUp(self):
        # O setUp roda antes de cada teste (igual ao @Before do JUnit)
        self.lc = LogicalClock()

    # Testa se o relógio começa corretamente em zero ao ser instanciado
    def test_initial_clock_is_zero(self):
        self.assertEqual(self.lc.clock, 0)

    # Testa se o método send_tick incrementa o valor do relógio em 1 unidade
    def test_send_tick_increments_clock(self):
        self.lc.send_tick()
        self.assertEqual(self.lc.clock, 1)

    # Testa a sincronização: ao receber um tempo maior, o relógio deve assumir esse valor e somar 1
    def test_receive_tick_with_greater_time(self):
        # Se recebe 10, o relógio (0) pula para 10 e incrementa para 11
        self.lc.receive_tick(10)
        self.assertEqual(self.lc.clock, 11)

    # Testa se o Setter está funcionando corretamente para forçar um novo valor ao tempo
    def test_setter_updates_time(self):
        self.lc.clock = 100
        self.assertEqual(self.lc.clock, 100)

if __name__ == '__main__':
    unittest.main()
