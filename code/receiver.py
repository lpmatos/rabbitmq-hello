# -*- coding: utf-8 -*-

import time
import pika
from typing import NoReturn

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

from settings.log import Log
from settings.config import Config

# ==============================================================================
# GLOBAL
# ==============================================================================

config = Config()

rabbit_host = config.get_env("RABBITMQ_HOST")
rabbit_user = config.get_env("RABBITMQ_DEFAULT_USER")
rabbit_password = config.get_env("RABBITMQ_DEFAULT_PASS")

log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else "/var/log/code"
log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else "file.log"
log_level = config.get_env("LOG_LEVEL") if config.get_env("LOG_LEVEL") else "DEBUG"
logger_name = config.get_env("LOGGER_NAME") if config.get_env("LOGGER_NAME") else "Code"

logger = Log(log_path, log_file, log_level, logger_name).logger

queue = "hello"

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def callback(ch, method, properties, body) -> NoReturn:
  print(f"[x] Received {body}.")

def run() -> NoReturn:
  logger.info(f"Connecting to {rabbit_host}:{5672}")

  credentials = pika.PlainCredentials(rabbit_user, rabbit_password)
  params = pika.ConnectionParameters(
    host=rabbit_host,
    credentials=credentials
  )

  start_time = time.time()

  while True:
    try:
      connection = pika.BlockingConnection(params)
      break
    except pika.exceptions.AMQPConnectionError:
      logger.warn("Cannot connect yet, sleeping 5 seconds.")
      time.sleep(5)
    if time.time() - start_time > 60:
      logger.error("Could not connect after 30 seconds.")
      exit(1)

  channel = connection.channel()
  channel.queue_declare(queue=queue)

  logger.info("Waiting for jobs.")

  channel.basic_consume(queue=queue,
    on_message_callback=callback,
    auto_ack=True)
  print("[*] Waiting for messages. To exit press CTRL + C.")
  channel.start_consuming()

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
  cprint(figlet_format("RabbitMQ", font="starwars"), "white", attrs=["dark"])
  run()
