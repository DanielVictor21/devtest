from fastapi import FastAPI
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
load_dotenv()
username = os.getenv('USER')
password = os.getenv('PASSWORD')

app = FastAPI()

DATABASE_URL = f"postgresql://{username}:{password}@localhost:5432/elevator"

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS elevator_calls (
            id SERIAL PRIMARY KEY,
            floor_called INTEGER,
            timestamp TIMESTAMPTZ
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS elevator_status (
            id SERIAL PRIMARY KEY,
            current_floor INTEGER,
            is_vacant BOOLEAN,
            timestamp TIMESTAMPTZ
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()

class CallElevatorRequest(BaseModel):
    floor_called: int
    timestamp: str  

class UpdateStatusRequest(BaseModel):
    current_floor: int
    is_vacant: bool
    timestamp: str  

@app.post("/call_elevator")
def call_elevator(request: CallElevatorRequest):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO elevator_calls (floor_called, timestamp) VALUES (%s, %s)', 
        (request.floor_called, request.timestamp)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "success", "floor_called": request.floor_called, "timestamp": request.timestamp}

@app.post("/update_status")
def update_status(request: UpdateStatusRequest):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO elevator_status (current_floor, is_vacant, timestamp) VALUES (%s, %s, %s)', 
        (request.current_floor, request.is_vacant, request.timestamp)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "success", "current_floor": request.current_floor, "is_vacant": request.is_vacant, "timestamp": request.timestamp}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
