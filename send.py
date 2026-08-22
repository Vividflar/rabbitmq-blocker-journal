import pika

connection = pika.BlockingConnection(pika.URLParameters('amqps://tviucipo:RGXbxLb3Hg2quA9IOBe_TOSbPP3xd51A@gerbil.rmq.cloudamqp.com/tviucipo'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
