import logging

from app.kafka.init_kafka import init_kafka

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    init_kafka()

def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
