# 📊 Trabalho 4 - Testes de Desempenho com Link Extractor

## 👥 Autores

- Igor Gomes Ximenes - 2217665
- Gabriel Abreu Cunha de Alencar - 2315097  
- Kalil Smith Pinto Palheta - 2223857

---

## 📌 1. Descrição do Trabalho

Este trabalho tem como objetivo avaliar o desempenho da aplicação **Link Extractor**, baseada em arquitetura de microsserviços.

A aplicação é composta por:

- Front-end (PHP)
- Serviço de extração de links (Python e Ruby)
- Serviço de cache (Redis)

A funcionalidade principal consiste em receber uma URL e retornar todos os links contidos na página.

---

## ⚙️ 2. Ferramenta de Teste de Carga

Foi utilizada a ferramenta **Locust**, que permite simular múltiplos usuários simultâneos por meio de scripts em Python.

### 🔹 Características do Locust

- Baseado em Python  
- Simulação de usuários concorrentes  
- Definição de comportamento via código  
- Coleta de métricas como:
  - Tempo de resposta (médio, mediana, percentis)
  - Requisições por segundo (RPS)
  - Taxa de falhas  

---

### 🧠 Script do usuário virtual (Locustfile)

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
```

---

## 🧪 3. Cenários de Teste

### 🔹 Variáveis analisadas

- Linguagem:
  - Python
  - Ruby  

- Cache:
  - Com Redis  
  - Sem Redis  

- Carga:
  - 10 usuários  
  - 100 usuários  
  - 1000 usuários  

---

### 📊 Cenários executados

| Linguagem | Cache | Usuários |
|----------|------|--------|
| Python | Com | 10 |
| Python | Sem | 10 |
| Python | Com | 100 |
| Python | Sem | 100 |
| Python | Com | 1000 |
| Python | Sem | 1000 |
| Ruby | Com | 10 |
| Ruby | Sem | 10 |
| Ruby | Com | 100 |
| Ruby | Sem | 100 |
| Ruby | Com | 1000 |
| Ruby | Sem | 1000 |

---

## 📈 4. Execução dos Testes

Os testes foram executados com o Locust, utilizando:

- múltiplos usuários simultâneos  
- taxa de criação controlada  
- execução contínua  
- coleta automática de métricas  

Os resultados foram exportados em arquivos CSV e analisados com Python (pandas + matplotlib).

---

## 📊 5. Resultados e Gráficos

### 🔹 Tempo Médio de Resposta

![Tempo Médio](graficos/tempo_medio.png)

---

### 🔹 Mediana do Tempo de Resposta

![Mediana](graficos/mediana.png)

---

### 🔹 Requisições por Segundo (RPS)

![RPS](graficos/rps.png)

---

### 🔹 Número de Falhas

![Falhas](graficos/falhas.png)

---

### 🔹 Comparação Python (Cache vs Sem Cache)

![Python](graficos/python_comparacao.png)

---

### 🔹 Comparação Ruby (Cache vs Sem Cache)

![Ruby](graficos/ruby_comparacao.png)

---

## 🧠 6. Análise dos Resultados

### 🔹 Tempo de resposta

- De 10 para 100 usuários → redução da latência  
- De 100 para 1000 usuários → aumento significativo  

#### 📌 Interpretação

- Baixa carga → subutilização do sistema  
- Carga média → melhor aproveitamento de recursos  
- Alta carga → saturação e aumento de latência  

---

### 🔹 Escalabilidade (RPS)

- Crescimento significativo até 100 usuários  
- Crescimento reduzido até 1000 usuários  

#### 📌 Interpretação

O sistema apresenta boa escalabilidade inicial, mas possui limite de capacidade.

---

### 🔹 Falhas

- 0 falhas em 10 e 100 usuários  
- Falhas surgem em 1000 usuários  

#### 📌 Interpretação

O sistema mantém estabilidade até carga moderada, mas degrada sob alta concorrência.

---

### 🔹 Cache (Redis)

- Diferença mínima entre com e sem cache  

#### 📌 Explicação

O uso de URLs diferentes impede o reaproveitamento do cache, reduzindo seu impacto.

---

### 🔹 Python vs Ruby

- Diferença de desempenho pequena  
- Python apresentou menos falhas em alta carga  

#### 📌 Interpretação

A linguagem não foi o principal fator de desempenho.

---

## ⚠️ 7. Limitações do Experimento

- Cache pouco efetivo devido a URLs distintas  
- Influência da latência de rede externa  
- Ausência de cenário de cache aquecido  

---

## 🏁 8. Conclusão

- O sistema apresenta boa escalabilidade inicial  
- Há degradação sob alta carga  
- O cache não impactou significativamente neste cenário  
- A linguagem teve influência limitada  

### 🎯 Conclusão Final

> O principal fator de impacto no desempenho foi a quantidade de usuários simultâneos.

---

## 🚀 9. Como Executar

```bash
docker-compose up -d
locust -f locustfile.py
```

Acessar:

```
http://localhost:8089
```

---

## 🧰 10. Tecnologias Utilizadas

- Docker / Docker Compose  
- Locust  
- Python (pandas, matplotlib)  
- Redis  
- Ruby / Python APIs  

---

## ✅ Resultado

Este trabalho permitiu analisar:

- comportamento sob carga  
- escalabilidade  
- impacto de cache  
- comparação entre linguagens  
