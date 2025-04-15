# Cripto Dash Streaming

Um sistema de ingestão, processamento e visualização de dados em tempo real para transações de criptomoedas, utilizando Kafka, PostgreSQL, Streamlit e outras tecnologias modernas de dados.

---

## 🚀 Visão Geral

Este projeto simula um pipeline completo de engenharia de dados em tempo real, coletando transações fictícias de criptomoedas, processando-as com Apache Kafka, armazenando-as em um banco de dados PostgreSQL e exibindo-as em um dashboard interativo com **Streamlit**.

---

## 🧱 Tecnologias Utilizadas

| Camada | Tecnologias |
|--------|-------------|
| **Coleta/Streaming** | `Python`, `Kafka`, `confluent_kafka` |
| **Processamento** | `Kafka Consumer`, `Python` |
| **Armazenamento** | `PostgreSQL`, `psycopg2` |
| **Visualização** | `Streamlit`, `Plotly`, `Pandas` |

---

## 📊 Funcionalidades do Dashboard

- Filtro por **moeda**
- Filtro por período: `Últimas 24h`, `7 dias`, `30 dias` ou `Tudo`
- Visualização de:
  - Preço médio
  - Valor máximo e mínimo
  - Variação percentual
- Gráfico interativo com Plotly
- Exportação dos dados para CSV
- Visualização da tabela com dados brutos
---

## 🔧 Como Rodar o Projeto

### 1. Clone o repositório
```terminal
git clone https://github.com/Arthurss123/cripto-dash-streaming.git
cd cripto-dash-streaming
```

### 2. Instale as dependências
```terminal
pip install -r requirements.txt
```

### 3. Suba o servidor Kafka e PostgreSQL
Você pode usar Docker ou subir localmente. Exemplo com Docker
```terminal
docker-compose up -d
```

### 4. Rode o producer e o consumer
```terminal
python data_producer/producer.py
python data_consumer/consumer.py
```

### Contribuição
Caso deseje contribuir com o projeto e meu aprendizado, seria de grande ajuda!

###👨‍💻 Autor
Arthur Moura
Estudante de Engenharia de Dados |
🔗 [LinkedIn](https://www.linkedin.com/in/arthurmoura233/)

