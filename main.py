import os
from src.server import Server
from src.client import Client


def main():
    log_path = os.path.join(os.path.dirname(__file__), "logs", "log_conferencia.txt")

    if os.path.exists(log_path):
        os.remove(log_path)

    srv = Server()
    alice = Client("Alice")
    bob = Client("Bob")
    charlie = Client("Charlie")

    print("=== INICIANDO PROTOCOLO DE TESTES (Auditoria) ===")

    srv.route(alice.send("Oi Bob!", receiver=bob))
    srv.process()

    devs = srv.create_channel("devs")
    devs.join(alice)
    devs.join(bob)
    srv.route(charlie.send("Olá devs!", channel="devs"))
    srv.process()

    geral = srv.create_channel("geral")
    for u in [alice, bob, charlie]: geral.join(u)
    srv.route(alice.send("AVISO GERAL", channel="geral"))
    srv.process()

    print(f"\n[SUCESSO] Testes finalizados. Verifique em: {log_path}")


if __name__ == "__main__":
    main()