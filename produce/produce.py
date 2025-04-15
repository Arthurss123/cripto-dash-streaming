from confluent_kafka import Producer
import random
import json
from faker import Faker
import time

fake = Faker()

moedas_fakes = ['BitCoin', 'Etherium', 'LiteCoin', 'Ripple', 'Solana']

def gerar_transacao():
    moeda = random.choice(moedas_fakes)
    valor_compra = round(random.uniform(1000, 50000), 2)  #Aqui geramos um preço de compra que esta limitado entre 1000 e 50000
    valor_venda = round(valor_compra * random.uniform(0.98, 1.05), 2)  # Aqui geramos um preço de venda pode ser mais alto ou mais baixo
    volume_transacao = random.randint(1, 50)  # Volume de moedas transacionadas
    data_transacao = fake.date_this_year()  # Aqui geramos uma data de transação aleatoria dentro desse ano
    
    return {
        'moeda': moeda,
        'valor_compra': valor_compra,
        'valor_venda': valor_venda,
        'volume_transacao': volume_transacao,
        'data_transacao': str(data_transacao)
    }

def delivery_report(err, msg):
    if err is not None:
        print('Falha ao enviar: {}'.format(err))
    else:
        print('Mensagem enviada para {} [{}]'.format(msg.topic(), msg.partition()))

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(conf)

topic = 'transacoes_moedas'

while True:
    transacao = gerar_transacao()

    producer.produce(topic, json.dumps(transacao), callback=delivery_report)
    producer.flush()

    time.sleep(random.uniform(0.5, 2))
