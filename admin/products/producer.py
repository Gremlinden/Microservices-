import pika, json

params = pika.URLParameters('amqps://jjijrwxg:jkkL5kS-7-OKsLkJNJ4jC5mvZtnfBTAy@stingray.rmq.cloudamqp.com/jjijrwxg')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
