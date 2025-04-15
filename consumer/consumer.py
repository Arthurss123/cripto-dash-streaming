from confluent_kafka import Consumer
import json
import psycopg2

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'crypto_debug_grafico',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(['transacoes_moedas'])

def salvar_em_banco(data):
    try:
        conn = psycopg2.connect(
            dbname="kafka_streaming",
            user="postgres",
            password="19081969",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transacoes_moedas (moeda, valor_compra, valor_venda, volume_transacao, data_transacao)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['moeda'], data['valor_compra'], data['valor_venda'], data['volume_transacao'], data['data_transacao']))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Erro ao salvar dados no banco:", e)

print("Recebendo dados")
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Erro: {}".format(msg.error()))
            continue

        data = json.loads(msg.value().decode('utf-8'))
        print(f"Dados recebidos, use ctrl + c para finalizar: {data}")

        salvar_em_banco(data)
        
except KeyboardInterrupt:
    print("Encerrando consumer...")
finally:
    consumer.close()
