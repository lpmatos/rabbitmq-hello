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

def run() -> NoReturn:
  channel = connection.channel()
  channel.queue_declare(queue=queue)
  channel.basic_publish(exchange="", routing_key=queue, body="Hello World!")
  print("[x] Sent 'Hello World!'")
  connection.close()

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
  run()
