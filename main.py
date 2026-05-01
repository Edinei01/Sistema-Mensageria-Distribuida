import os
from src.server import Server
from src.client import Client


def main():
    log_path = os.path.join(os.path.dirname(__file__), "logs", "log_conferencia.txt")
    if os.path.exists(log_path):
        os.remove(log_path)

    srv = Server()  #

    alice = Client("Alice")
    bob = Client("Bob")
    charlie = Client("Charlie")

    print("=== INICIANDO PROTOCOLO PGP (Kurose Model) ===")

    alice.save_public_key("Bob", bob.get_my_public_key())
    bob.save_public_key("Alice", alice.get_my_public_key())

    print(f"[INFO] Chaves públicas trocadas entre Alice e Bob.")

    print("\n[TESTE 1] Enviando mensagem PGP de Alice para Bob...")
    msg_to_bob = alice.send("Olá Bob, esta é uma mensagem secreta PGP!", receiver=bob)

    srv.route(msg_to_bob)
    srv.process()

    print("\n[TESTE 2] Enviando mensagem para canal 'devs'...")
    devs = srv.create_channel("devs")
    devs.join(alice)
    devs.join(bob)

    srv.route(charlie.send("Olá devs! Trabalho acadêmico em andamento.", channel="devs"))
    srv.process()

    print("\n[TESTE 3] Enviando aviso geral...")
    geral = srv.create_channel("geral")
    for u in [alice, bob, charlie]:
        geral.join(u)

    srv.route(alice.send("AVISO: Reunião de Sistemas Distribuídos às 14h", channel="geral"))
    srv.process()

    print(f"\n[SUCESSO] Fluxo PGP finalizado. Verifique os logs em: {log_path}")


if __name__ == "__main__":
    main()