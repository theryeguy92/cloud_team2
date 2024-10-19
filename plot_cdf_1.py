import pymongo
import matplotlib.pyplot as plt
import numpy as np
import random

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['iot_db']
collection = db['iot_data']

# Number of producers to simulate
num_producers = 1  # Change this to 2, 3, or 4 for each run

# Clear existing data
collection.delete_many({})

# Simulate data insertion based on the number of producers
new_data = [random.randint(1, 100) for _ in range(100 * num_producers)]
collection.insert_many([{"value": value} for value in new_data])

# Fetch data from MongoDB
data = [doc['value'] for doc in collection.find()]

# Check if data is empty
if not data:
    print("No data found in the 'iot_data' collection.")
    exit()

# Print a sample of the fetched data
print(f"Sample data: {data[:5]}")

# Generate CDF
sorted_data = np.sort(data)
y_vals = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# Plot CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, y_vals, marker='.', linestyle='none', markersize=5)
plt.xlabel('Value')
plt.ylabel('CDF')
plt.title(f'CDF of IoT Data for {num_producers} Producers')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
