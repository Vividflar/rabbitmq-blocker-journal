import pika
import json

connection = pika.BlockingConnection(pika.URLParameters('amqps://tviucipo:RGXbxLb3Hg2quA9IOBe_TOSbPP3xd51A@gerbil.rmq.cloudamqp.com/tviucipo'))
channel = connection.channel()

channel.queue_declare(queue='stock_updates')

def callback(ch, method, properties, body):
    update = json.loads(body)
    print(f" [x] Stock updated -> Product {update['product_id']} is now at {'new_quantity'} units")
    
channel.basic_consume(queue='stock_updates', on_message_callback=callback, auto_ack=True)

print(' [*] Listening for the stock updates. To exit press CTRL+C')
channel.start_consuming()