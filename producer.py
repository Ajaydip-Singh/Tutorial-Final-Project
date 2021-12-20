from json import dumps
from kafka import KafkaProducer

# Convert data to json and encode to UTF-8
producer = KafkaProducer(
    bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"], 
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

for i in range(1000):
    message = {"number": i}
    producer.send("ordinary-topic", value=message).get(timeout=60)
