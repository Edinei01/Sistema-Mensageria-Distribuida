import time
import hmac
import hashlib


class TGS:

    def __init__(self, master_key: str):
        self.master_key = master_key.encode()

    def create_ticket(self, client_name: str, service_name: str, duration: int = 3600):
        expiration = time.time() + duration
        payload = f"{client_name}:{service_name}:{expiration}"

        signature = hmac.new(self.master_key, payload.encode(), hashlib.sha256).hexdigest()

        return f"{payload}|{signature}"

    def validate_ticket(self, ticket: str):
        try:
            payload, signature = ticket.split("|")
            expected_sig = hmac.new(self.master_key, payload.encode(), hashlib.sha256).hexdigest()
            if signature != expected_sig:
                return False, "Assinatura inválida"

            _, _, expiration = payload.split(":")
            if time.time() > float(expiration):
                return False, "Ticket expirado"

            return True, payload
        except Exception:
            return False, "Erro no formato do ticket"