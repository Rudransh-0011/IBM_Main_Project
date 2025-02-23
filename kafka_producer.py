# kafka_producer.py

from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_to_kafka(topic, data):
    producer.send(topic, data)
    producer.flush()

# Example usage
if __name__ == "__main__":
    send_to_kafka('social_media', {'text': 'This product is amazing!', 'platform': 'Twitter'})