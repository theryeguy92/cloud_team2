import pymongo
import matplotlib.pyplot as plt
import numpy as np

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['iot_db']
collection = db['iot_data']

# Clear the collection before adding new data
collection.delete_many({})

# Insert new data for 2 producers
collection.insert_many([
    {'value': 10}, {'value': 20}, {'value': 30}, {'value': 40}, {'value': 50},
    {'value': 60}, {'value': 70}, {'value': 80}, {'value': 90}, {'value': 100}
])

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
plt.title('CDF of IoT Data - 2 Producers')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
