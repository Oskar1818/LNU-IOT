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

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

![image](https://github.com/Oskar1818/LNU-IOT/assets/70581204/0285446b-20b6-4189-b72b-8ea22c29a27b)



- [ ] Circuit diagram (can be hand drawn)
- [ ] *Electrical calculations

### Platform

Describe your choice of platform. If you have tried different platforms it can be good to provide a comparison.

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [ ] Describe platform in terms of functionality
- [ ] *Explain and elaborate what made you choose this platform 

### The code

Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.

```python=
import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!
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
