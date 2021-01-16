import requests
import logging
import time

from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

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
            "key.converter": "io.confluent.connect.json.JsonSchemaConverter",
            "key.converter.schema.registry.url": "http://schemaregistry:8081",
            "value.converter": "io.confluent.connect.json.JsonSchemaConverter",
            "value.converter.schema.registry.url": "http://schemaregistry:8081",
            "connection.uri": "mongodb://mongo:changethis@mongodb:27017"
          }}
        }}""".format(topic_name=topic_name)

    r = requests.post(url, headers=headers, data=data)
    print(r)
    print(r.text)

def init_kafka():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    retry_count = 0
    while True:
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

    # mongo sinks
    create_kafka_job("blocks")
    create_kafka_job("logs")
    create_kafka_job("transactions")
