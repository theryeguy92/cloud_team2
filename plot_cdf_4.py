import pymongo
import matplotlib.pyplot as plt
import numpy as np

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['iot_db']
collection = db['iot_data']

# Clear existing data in the collection
collection.delete_many({})

# Insert data for the fourth producer
collection.insert_many([
    {'value': 20}, {'value': 40}, {'value': 60}, {'value': 80}, {'value': 100},
    {'value': 120}, {'value': 140}, {'value': 160}, {'value': 180}, {'value': 200}
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
plt.title('CDF of IoT Data - 4 Producers')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
