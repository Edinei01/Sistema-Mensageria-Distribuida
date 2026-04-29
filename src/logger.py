import os
from datetime import datetime


class Logger:
    @staticmethod
    def log_event(op, prod, p_t, cons="---", c_t=None, info=""):
        now = datetime.now().strftime("%H:%M:%S")
        entry = (f"[{now}] {op:12} | PROD: {prod:8} (T:{p_t}) | "
                 f"CONS: {cons:8} (T:{c_t if c_t else '---'}) | MSG: {info}")

        log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        log_path = os.path.join(log_dir, "log_conferencia.txt")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        print(entry)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry + "\n")