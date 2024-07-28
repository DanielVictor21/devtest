import requests
import random
import datetime

# URLs
url_call_elevator = 'http://localhost:8000/call_elevator'
url_update_status = 'http://localhost:8000/update_status'

# Function to call the elevator
def call_elevator(floor, timestamp):
    payload = {'floor_called': floor, 'timestamp': timestamp}
    print(f"Calling elevator with payload: {payload}")  # Debug print
    response = requests.post(url_call_elevator, json=payload)
    print(f"Called elevator to floor {floor}: {response.json()}")

# Function to update the elevator status
def update_status(current_floor, is_vacant, timestamp):
    payload = {'current_floor': current_floor, 'is_vacant': is_vacant, 'timestamp': timestamp}
    print(f"Updating status with payload: {payload}")  # Debug print
    response = requests.post(url_update_status, json=payload)
    print(f"Updated status to floor {current_floor}, vacant: {is_vacant}: {response.json()}")

# Function to generate datetimes in one day
def get_random_date():
    start_date = datetime.datetime.now() - datetime.timedelta(days=1)  # 1 day before
    end_date = datetime.datetime.now()  # today
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.isoformat()  # ISO 8601 format

# Create floors to test. I choose for 30.
floors = [item for item in range(0, 31)]
print(floors)

for i in range(0, 1001): # Create 1000 rows, i think is a good number for a test.
    # Generate a random timestamp
    timestamp = get_random_date()
    
    # Call the elevator
    floor_called = random.choice(floors)
    call_elevator(floor_called, timestamp)
    
    # Update the elevator status
    current_floor = random.choice(floors)
    is_vacant = random.choice([True, False])
    update_status(current_floor, is_vacant, timestamp)
