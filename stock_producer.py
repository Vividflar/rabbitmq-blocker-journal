import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='stock_updates')

update = {"product_id": "SKU-1001", "new_quantity": 42}

channel.basic_publish(
    exchange='',
    routing_='stock_updates',
    body=json.dumps(update)
)
print(f" [x] Sent stock updates: {update}")

connection.close()