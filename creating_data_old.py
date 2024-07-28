import requests
import random
import time

# URLs
url_call_elevator = 'http://localhost:8000/call_elevator'
url_update_status = 'http://localhost:8000/update_status'

# Function to call the elevator
def call_elevator(floor):
    response = requests.post(url_call_elevator, json={'floor_called': floor})
    print(f"Called elevator to floor {floor}: {response.json()}")

# Function to update the elevator status
def update_status(current_floor, is_vacant):
    response = requests.post(url_update_status, json={'current_floor': current_floor, 'is_vacant': is_vacant})
    print(f"Updated status to floor {current_floor}, vacant: {is_vacant}: {response.json()}")

# Create floors to test. I choose for 30.
floors = [item for item in range(0, 31)]
print(floors)

while True: # Keep creating until satisfied. I could have used a foor loop with a max interations, but i choose for this to stop when i wanted.
    # Call the elevator
    floor_called = random.choice(floors)
    call_elevator(random.choice(floors))
    time.sleep(random.uniform(0.5, 2.0))
    
    # Update the elevator status
    current_floor = random.choice(floors)
    is_vacant = random.choice([True, False])
    update_status(current_floor, is_vacant)
    time.sleep(random.uniform(0.5, 2.0))