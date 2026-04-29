import unittest
from src.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    # NAME
    def test_client_name(self):
        self.assertEqual(self.alice.name, "Alice")

    # INITIAL CLOCK
    def test_initial_clock_is_zero(self):
        self.assertEqual(self.alice.clock.time, 0)

    # SEND MESSAGE
    def test_send_increments_clock(self):
        msg = self.alice.send("Oi Bob", receiver=self.bob)

        self.assertEqual(self.alice.clock.time, 1)
        self.assertEqual(msg.timestamp, 1)
        self.assertEqual(msg.content, "Oi Bob")
        self.assertEqual(msg.sender.name, "Alice")

    # RECEIVE MESSAGE
    def test_receive_syncs_clock(self):
        msg = self.alice.send("Oi Bob", receiver=self.bob)

        # bob recebe mensagem da alice
        self.bob.receive(msg)

        # clock do bob deve ser max(0,1)+1 = 2
        self.assertEqual(self.bob.clock.time, 2)

    # ORDERING BEHAVIOR
    def test_multiple_sends_increment_clock(self):
        self.alice.send("msg1", receiver=self.bob)
        self.alice.send("msg2", receiver=self.bob)

        self.assertEqual(self.alice.clock.time, 2)


if __name__ == "__main__":
    unittest.main()