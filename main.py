import dht
import machine
import time
import urequests as requests

tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor 
# tempSensor = dht.DHT22(machine.Pin(27))   # DHT22 Constructor
adc = machine.ADC(4)

TOKEN = "BBUS-VG7bGtevEv2uCzkKbuKazSRLPGhcEC" #Put here your TOKEN
DEVICE_LABEL = "picowboard" # Assign the device label desire to be send
HUMIDITY_LABEL = "humidity"   # Assign the variable label desire to be send
TEMPERATURE_LABEL = "temperature"  # Assign the variable label desire to be send
DELAY = 60  # Delay in seconds

# Builds the json to send the request
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None

# Sending data to Ubidots Restful Webserice
def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

while True:
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature: {} - Humidity: {}%".format(temperature, humidity))
        returnValue = sendData(DEVICE_LABEL, TEMPERATURE_LABEL, temperature)
        returnValue2 = sendData(DEVICE_LABEL, HUMIDITY_LABEL, humidity)
    except Exception as error:
        print("Exception occurred", error)
    time.sleep(DELAY)