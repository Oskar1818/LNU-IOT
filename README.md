## Temperature and humidity measurements using Ubidots
Oskar Sturebrand (os222ut)
With the help of a DHT11,  Raspberry pico WH and the platform Ubidots, I was able to measure and visualize my indoor temperature and humidity in a very easy way.
Time to recreate: approximately 4-6 hours

### Objective
I chose this project to be able to measure the temperature and humidity of my indoor environment in an easy and hands off manner. This project will help me determine and visualize what effect strategies have on cooling my indoor temperature. It also allows me to track humidity which also has a big impact on perceived temperature. 


### Material
Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.

- [x] List of material
- [ ] What the different things (sensors, wires, controllers) do - short specifications
- [x] Where you bought them and how much they cost

I bought all the components off the website https://www.electrokit.com

| Quantity | Component            | Price   |
| -------- | -------------------- | ------- |
| 1        | Raspberry Pi Pico WH | 109 SEK |
| 1        | DHT11                | 49 SEK  |
| 3        | Jumper Wires         | 49 SEK  |
| 1        | Breadboard 840       | 69 SEK  |
| 1        | Micro USB cable      | 39 SEK  |

#### Raspberry Pi Pico WH
The Pico is a low-cost microcontroller board. It's where the script is executed from and is the the brain of this project. It queries the DHT11 sensor for the temperature and humidity readings and sends it to Ubidots.

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/a082c1a5-4ba8-4520-9c54-98e0de3c1d6f" alt="pico" width="600"/>

#### DHT11
This is the sensor that I used to measure the temperature and humidity. Bellow are some technicall details of its capabilities:

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/e4d59bc7-71b4-45ee-8d27-a403c9bb9920" alt="sensor" width="600"/>

| Item  | Measurement Range | Humidity Accuracy | Temperature Accuracy | Resolution |
| ----- | ----------------- | ----------------- | -------------------- | ---------- |
| DHT11 | 20-90%RH , 0-50 ℃ | ±5％RH             | ±2℃                  | 1          |

#### Jumper wires
The jumper wires are metal wires used to connect components electrically. They are often used in combination with a breadboard for easy setup.

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/66ec99f2-a465-455e-9842-f69b6cfba4fe" alt="wires" width="600"/>


#### Breadboard
The breadboard is used in combination with jumper wires to connect the different components together without having to solder. The breadboard has small holes which hold the wires in place and electrically connect them inside the board.  

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/8f0753d2-d404-472d-8da4-193f6335470f" alt="bread" width="600"/>


### Computer setup
I went the recommended path on the road map and used visual studio code as my IDE, the benefit being that i can use the Pymakr plugin to upload (flash) the code to the pico. The steps i took to setup the development enviroment followed the provided guide from the road map. But the general steps were: 
1. download and install node.js
2. download and install vs code
3. install the pymakr plugin from the vs code store

the complete steps can be fond here: https://hackmd.io/@lnu-iot/rkiTJj8O9

### Putting everything together
In the images bellow you can see exactly how everything is connected. I created a circuit diagram in Wokwi, unfortunatly it only had the DHT22 sensor, so i had to use it instead in the diagram. If we ignore the It's right most pin, the connection is identical to the DHT11. 

Looking at the pin schematic of the Pico, we can see that the **red** jumper wire is connected to ground on the picos 38:th pin, which is then connected to the DHT11's right most pin.

The **oragne** wire is connected to pin 36, which is the 3v pin. That is then connected to the middle pin of the sensor.

Lastly, the **yellow** wire is connected to the 32:nd pin on the pico, which is GP27 where the data is read. 

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/39cec65e-60f5-40db-9d0d-e278a689c2c9" alt="bread" width="600"/>

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/0285446b-20b6-4189-b72b-8ea22c29a27b" alt="bread" width="600"/>

<img src="https://github.com/Oskar1818/LNU-IOT/assets/70581204/02625f6e-5cb0-4cf0-a9f6-dda93275a0bf" alt="bread" width="600"/>

### Platform
I used Ubidots because it was easiest to setup without having to self host anything. Its very convinient to have everything in the cloud, and Ubidots STEM plan is very generous. It allows you to upload around 4000 data points per 24h which is more than 2 a minute which was more than enough for my application. The only downside is that they only allow you to retain your data for 1 month, so that's something that would need to be improved to scale the project to a more permenant solution. A way to solve that could be to self host a database. 

### The code

Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.

I used the code from the road map on connecting to Ubidots using HTTP requests on REST API to setup the wifi and http requests https://hackmd.io/@lnu-iot/r1k63jjwo. 

The intresting parts of the code are essentially only configuring some constants:
```py
# Configuration Constants
TOKEN = "*****"
DEVICE_LABEL = "picowboard"
HUMIDITY_LABEL = "humidity"
TEMPERATURE_LABEL = "temperature"
DELAY = 2  # Delay in seconds
TIME_TRIGGER = 10 * 60  # 10 minutes in seconds
```

Initializing the temperature and humidity sensor to the correct pin:
```py
# Sensor Initialization
tempSensor = dht.DHT11(machine.Pin(27))  # DHT11 Constructor
```

This is the main loop. In the first couple of lines, Im just Initializing a t1 and h1 variable, which will hold the first of two temperature and humidity readings. This value will be used later by comparing it to a second value, t2 and h2 to see if it has changed. We also store the current time in last_sent_time, this will be used later to keep track of when data was last sent.
```py
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
```

Here we are taking another time stamp, and getting the sensor readings from the tempSensor.
```py
current_time = time.time()
tempSensor.measure()
t2, h2 = tempSensor.temperature(), tempSensor.humidity()
print(f"Temperature: {t2} - Humidity: {h2}%")
```

We basically send data based on two diffrent conditons; 1. If 10min has elapsed since the last data point was sent. or 2. if the sensor reading changes by 1 degree for the temperature and 2% for humidity (thats why we use abs(h2 - h1)) to prevent oscillations. 
```py
# Determine if data should be sent
time_triggered = current_time - last_sent_time >= TIME_TRIGGER
temp_changed = t1 is None or t2 != t1
humidity_changed = h1 is None or abs(h2 - h1) > 2
```

So basically, if it has been more than 10 min, or if temperature changed, or if humidity changed we enter the if statement. We then diffirentiate between temp_changed and humidity_changed to determine what data to send. Otherwise we just print "Temperature and Humidity unchanged." and move on. 
```py
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
```

which is just to sleep for 2 seconds, before we do the same comparison again.
```py
time.sleep(DELAY)
```

### Transmitting the data / connectivity

How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

- [ ] How often is the data sent? 
- [ ] Which wireless protocols did you use (WiFi, LoRa, etc ...)?
- [ ] Which transport protocols were used (MQTT, webhook, etc ...)
- [ ] *Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.

### Presenting the data

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [ ] Provide visual examples on how the dashboard looks. Pictures needed.
- [ ] How often is data saved in the database.
- [ ] *Explain your choice of database.
- [ ] *Automation/triggers of the data.

### Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation

---
