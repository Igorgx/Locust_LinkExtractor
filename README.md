# 📊 Trabalho 4 - Testes de Desempenho com Link Extractor

## 👥 Autores

- Igor Gomes Ximenes  
- Gabriel Abreu Cunha de Alencar  
- Kalil Smith Pinto Palheta  

---

# 📌 1. Descrição do Trabalho

Este trabalho tem como objetivo avaliar o desempenho da aplicação **Link Extractor**, baseada em arquitetura de microsserviços.

A aplicação é composta por:

- Front-end (PHP)
- Serviço de extração de links (Python e Ruby)
- Serviço de cache (Redis)

A funcionalidade principal consiste em receber uma URL e retornar todos os links contidos na página.

---

# ⚙️ 2. Ferramenta de Teste de Carga

Foi utilizada a ferramenta **Locust**, que permite simular múltiplos usuários simultâneos por meio de scripts em Python.

## 🔹 Características do Locust

- Baseado em Python  
- Simulação de usuários concorrentes  
- Definição de comportamento via código  
- Coleta de métricas como:
  - Tempo de resposta (médio, mediana, percentis)
  - Requisições por segundo (RPS)
  - Taxa de falhas  

---

## 🧠 Script do usuário virtual (Locustfile)

Cada usuário realiza 10 requisições consecutivas com URLs diferentes:

```python
from locust import HttpUser, task, between

class LinkExtractorUser(HttpUser):
    wait_time = between(1, 2)

    urls = [
        "https://example.com",
        "https://httpbin.org",
        "https://example.org",
        "https://iana.org",
        "https://github.com",
        "https://stackoverflow.com",
        "https://wikipedia.org",
        "https://python.org",
        "https://openai.com",
        "https://google.com"
    ]

    @task
    def extract_links(self):
        for url in self.urls:
            self.client.get(f"/api/extract?url={url}")
