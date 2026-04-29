# 📡 Sistema de Mensageria Distribuída

## 📘 Disciplina
Computação Paralela e Distribuída

## 👨‍🎓 Aluno
Edinei

## 📅 Data
27 de abril de 2026

---

# 🧠 Visão Geral

Este projeto implementa um **sistema de mensageria distribuída simulado em Python**, permitindo comunicação entre clientes com suporte a:

- 📩 Unicast (um para um)
- 📢 Multicast (um para grupo)
- 📡 Broadcast (um para todos)

O sistema utiliza o **Relógio Lógico de Lamport** para garantir ordenação causal das mensagens e inclui mecanismos de **criptografia** baseados em classes desenvolvidas na disciplina de Segurança de Sistemas de Informação.

---

# ⚙️ Funcionalidades

✔ Registro de clientes com identificação única  
✔ Criação e participação em canais  
✔ Envio de mensagens com timestamp lógico (Lamport)  
✔ Message Buffer para armazenamento e organização de mensagens  
✔ Suporte a unicast, multicast e broadcast  
✔ Log de eventos em arquivo `.txt`  
✔ Integração com criptografia simétrica e assimétrica  

---

# 🧩 Arquitetura do Sistema

```
src/
 ├── client.py
 ├── server.py
 ├── message.py
 ├── message_buffer.py
 ├── logical_clock.py
 ├── logger.py
 ├── channel.py
 └── crypto/
      ├── symmetric.py
      ├── asymmetric.py
      └── tgs.py
```

---

# 🕰️ Relógio Lógico (Lamport)

O sistema utiliza o algoritmo de Lamport para manter a ordem causal dos eventos.

Regras:

- Evento local: `time = time + 1`
- Envio de mensagem: incrementa o tempo e envia timestamp
- Recebimento: `time = max(time_local, time_recebido) + 1`

---

# 📦 Message Buffer

Responsável por:

- Armazenar mensagens
- Identificar produtor e consumidor
- Organizar entrega por tipo de comunicação:
  - Unicast
  - Multicast
  - Broadcast

---

# 🔐 Criptografia

O sistema integra módulos de criptografia para:

- Criptografia simétrica
- Criptografia assimétrica

As mensagens são protegidas no envio e descriptografadas no recebimento.

---

# 📝 Logs

Todas as operações são registradas em arquivo:

```
logs/sistema_log.txt
```

Incluindo:

- Produtor
- Consumidor
- Timestamp lógico de envio
- Timestamp lógico de recebimento
- Conteúdo da mensagem

---

# 🧪 Testes

O sistema foi testado manualmente com os seguintes cenários:

- ✔ Registro de cliente e envio unicast
- ✔ Multicast em canais
- ✔ Broadcast para todos os clientes
- ✔ Ordenação correta via relógio lógico
- ✔ Criptografia funcionando corretamente
- ✔ Registro completo em log

---

# 🚀 Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos
- Algoritmo de Lamport
- Estruturas de Mensageria Distribuída
- Criptografia (simétrica e assimétrica)

---

# 📂 Repositório

GitHub: https://github.com/Edinei01/Sistema-Mensageria-Distribuida

---

# 📌 Observações

Este projeto foi desenvolvido com foco acadêmico, simulando um ambiente distribuído lógico, sem uso de comunicação real via rede (sockets físicos), priorizando a modelagem conceitual do sistema.

