import logging
from base64 import b64decode


logging.basicConfig(level=logging.WARNING)


def notifica_pubsub(event, context):
    logging.info(f"Evento: {event}")
    logging.warn(f"Contexto: {context}")
    logging.warn(f"Data: {b64decode(event['data']).decode('utf-8')}")

    return "OK"