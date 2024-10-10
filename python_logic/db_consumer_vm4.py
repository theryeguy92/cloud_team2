from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Change 'localhost' to your MongoDB server if needed
db = client.iot_database
collection = db.iot_collection

# Configure Kafka Consumer
consumer = KafkaConsumer(
    'iot_topic',
    bootstrap_servers=['localhost:9092'],  # Change 'localhost' if using a remote server
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='iot-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume messages from Kafka and insert into MongoDB
for message in consumer:
    data = message.value
    print(f"Consumed message: {data}")
    collection.insert_one(data)  # Insert the data into MongoDB