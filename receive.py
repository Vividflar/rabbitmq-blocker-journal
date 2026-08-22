import pika

connection = pika.BlockingConnection(pika.URLParameters('amqps://tviucipo:RGXbxLb3Hg2quA9IOBe_TOSbPP3xd51A@gerbil.rmq.cloudamqp.com/tviucipo'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Receive{body}")
    
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()