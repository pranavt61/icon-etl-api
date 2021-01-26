import requests
import logging
import time

from app.core.config import settings

def create_kafka_job(topic_name):
    url = "http://" + settings.KAFKA_CONNECT_URL + "/connectors"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = """{{
          "name": "{topic_name}-mongo-sink",
          "config": {{
            "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
            "topics": "{topic_name}",
            "tasks.max": "1",
            "database": "icon",
            "collection": "{topic_name}",
            "key.converter": "org.apache.kafka.connect.storage.StringConverter",
            "key.converter.schema.registry.url": "http://schemaregistry:8081",
            "value.converter": "io.confluent.connect.json.JsonSchemaConverter",
            "value.converter.schema.registry.url": "http://schemaregistry:8081",
            "connection.uri": "mongodb://mongo:changethis@mongodb:27017"
          }}
        }}""".format(topic_name=topic_name)

    r = requests.post(url, headers=headers, data=data)

def init_kafka():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    retry_count = 0
    while True:
        if retry_count >= 120:
            # if connect is still not up in 2 minutes, give up
            logger.error("Kafka connect unreachable, failed to create sinks")
            return
        try:
            r = requests.get("http://" + settings.KAFKA_CONNECT_URL)
            if r.status_code == 200:
                break
            else:
                retry_count += 1
                logger.info("Could not connect to kafka-connect, retrying in 1 sec: " + str(retry_count) + " retries")
                time.sleep(1)
        except:
            retry_count += 1
            logger.info("Could not connect to kafka-connect, retrying in 1 sec: " + str(retry_count) + " retries")
            time.sleep(1)

    # kafka connect is up
    # start setting up mongo sinks

    logger.info("Creating kakfa connects")

    # mongo sinks
    create_kafka_job("blocks")
    create_kafka_job("logs")
    create_kafka_job("transactions")
