from kafka import KafkaConsumer
import pymongo
import json

# Kafka consumer configuration
consumer = KafkaConsumer(
    'iot_data',  # Topic name
    bootstrap_servers=['localhost:9092'],  # Kafka broker
    auto_offset_reset='earliest',  # Read messages from the beginning
    enable_auto_commit=True,  # Commit messages after reading
    group_id='iot-consumer-group',  # Consumer group
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize the data
)

# MongoDB connection (Optional: Comment this out for now if MongoDB is not up)
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['iot_database']  # Database name
    collection = db['iot_data']  # Collection name
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    collection = None

# Process messages
for message in consumer:
    iot_data = message.value
    print(f"Received message: {iot_data}")
    
    if collection:
        collection.insert_one(iot_data)  # Insert the message into MongoDB
        print(f"Inserted into MongoDB: {iot_data}")
    else:
        print("MongoDB is not available, skipping database insertion.")
