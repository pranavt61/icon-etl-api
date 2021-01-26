from confluent_kafka import Consumer

class BufferReader:
    def __init__(self):
        self.buffer_queue = []

    def read_buffer_queue(self):
        if len(self.buffer_queue) == 0:
            return None
        return self.buffer_queue.pop(0)

    def write_buffer_queue(self, msg):
        self.buffer_queue.append(msg)

def read_consumer():
    c = Consumer({
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'latest',
    })

    c.subscribe(['blocks'])

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            continue
        blocks_buffer = msg.value().decode('utf-8')
    c.close()

