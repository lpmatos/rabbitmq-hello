# -*- coding: utf-8 -*-

import pika
from typing import NoReturn

# ==============================================================================
# GLOBAL
# ==============================================================================

host, user, password, queue = "rabbitmq", "user", "aa1cf3497ecefc5293de!AA", "hello"

credentials = pika.PlainCredentials(user, password)
params = pika.ConnectionParameters(credentials=credentials, host=host)
connection = pika.BlockingConnection(params)

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def callback(ch, method, properties, body) -> NoReturn:
  print(f"[x] Received {body}.")

def run() -> NoReturn:
  channel = connection.channel()
  channel.queue_declare(queue=queue)
  channel.basic_consume(queue=queue,
    on_message_callback=callback,
    auto_ack=True)
  print("[*] Waiting for messages. To exit press CTRL + C.")
  channel.start_consuming()

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
  run()
