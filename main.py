# Imports
import dht
import machine
import time
import urequests as requests

# Configuration Constants
TOKEN = "BBUS-VG7bGtevEv2uCzkKbuKazSRLPGhcEC"
DEVICE_LABEL = "picowboard"
HUMIDITY_LABEL = "humidity"
TEMPERATURE_LABEL = "temperature"
DELAY = 2  # Delay in seconds
TIME_TRIGGER = 10 * 60  # 10 minutes in seconds

# Sensor Initialization
tempSensor = dht.DHT11(machine.Pin(27))  # DHT11 Constructor

# Function Definitions
def build_json(variable, value):
    """Builds the JSON payload to send the request."""
    try:
        return {variable: {"value": value}}
    except Exception as e:
        print(f"Error building JSON: {e}")
        return None

def sendData(device, variable, value):
    """Sends data to Ubidots Restful Webservice."""
    try:
        url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{device}"
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)
        if data:
            print(data)
            response = requests.post(url=url, headers=headers, json=data)
            return response.json()
    except Exception as e:
        print(f"Error sending data: {e}")

# Main Loop
t1, h1 = None, None  # Initialize previous temperature and humidity
last_sent_time = time.time()

while True:
    try:
        current_time = time.time()
        tempSensor.measure()
        t2, h2 = tempSensor.temperature(), tempSensor.humidity()
        print(f"Temperature: {t2} - Humidity: {h2}%")

        # Determine if data should be sent
        time_triggered = current_time - last_sent_time >= TIME_TRIGGER
        temp_changed = t1 is None or t2 != t1
        humidity_changed = h1 is None or abs(h2 - h1) > 2
        if time_triggered or temp_changed or humidity_changed:
            if temp_changed or time_triggered:
                sendData(DEVICE_LABEL, TEMPERATURE_LABEL, t2)
                t1 = t2
            if humidity_changed or time_triggered:
                sendData(DEVICE_LABEL, HUMIDITY_LABEL, h2)
                h1 = h2
            last_sent_time = current_time
        else:
            print("Temperature and Humidity unchanged.")
    except Exception as error:
        print(f"Exception occurred: {error}")
    time.sleep(DELAY)