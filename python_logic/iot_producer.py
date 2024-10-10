from kafka import KafkaProducer
import json
import random
from time import sleep

# Configure Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Change 'localhost' if using a remote server
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Mock data for image simulation
image_data = [
    {'ID': 1, 'GroundTruth': 'cat', 'Data': 'Image data for cat'},
    {'ID': 2, 'GroundTruth': 'dog', 'Data': 'Image data for dog'},
    {'ID': 3, 'GroundTruth': 'car', 'Data': 'Image data for car'}
]

# Function to produce messages to Kafka
def produce_message():
    message = random.choice(image_data)
    print(f"Producing message: {message}")
    producer.send('iot_topic', message)
    producer.flush()  # Ensure all messages are sent

# Produce messages indefinitely
while True:
    produce_message()
    sleep(5)  # Wait for 5 seconds before sending the next message