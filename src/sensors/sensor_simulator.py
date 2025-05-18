import random
import json
from datetime import datetime

def generate_fill_level_event(sensor_id):
    event = {
        "sensor_id": sensor_id,
        "timestamp": datetime.utcnow().isoformat(),
        "fill_level": round(random.uniform(0, 100), 2)
    }
    return event

if __name__ == "__main__":
    print(json.dumps(generate_fill_level_event("sensor_1"), indent=2))