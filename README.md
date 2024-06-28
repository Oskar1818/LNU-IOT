# Template

**Please keep the total length of the tutorial below 25k characters.** You can include code that is linked to a repository. Keep the code snippets in the tutorial short.

## Temperature and humidity measurements using Ubidots

Give a short and brief overview of what your project is about.
What needs to be included:

- [x] Title
- [x] Your name and student credentials (xx666x)
- [x] Short project overview
- [x] How much time it might take to do (approximation)

Oskar Sturebrand (os222ut)

With the help of a DHT11,  Raspberry pico WH and the platform Ubidots, I was able to measure and visualize my indoor temperature and humidity in a very easy way.

Time to recreate: approximately 4-6 hours

### Objective

Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?

- [x] Why you chose the project
- [x] What purpose does it serve
- [x] What insights you think it will give

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
The pi is where the script is executed from and is the the brain of this project. It queries the DHT11 sensor for the temperature and humidity readings and sends it to Ubidots. 

#### DHT11
This is the sensor that I used to measure the temperature and humidity.

| Item  | Measurement Range | Humidity Accuracy | Temperature Accuracy | Resolution |
| ----- | ----------------- | ----------------- | -------------------- | ---------- |
| DHT11 | 20-90%RH , 0-50 ℃ | ±5％RH             | ±2℃                  | 1          |
|       |                   |                   |                      |            |

#### Jumper wires
The jumper wires are used to connect the pico and the other components electrically. In this project we use them to connect the DHT11 to the pico.


#### Breadboard
The breadboard is used to connect the different together without having to solder. 

### Computer setup

How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a beginner should be able to understand.

- [ ] Chosen IDE
- [ ] How the code is uploaded
- [ ] Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.

### Putting everything together

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

![image](https://github.com/Oskar1818/LNU-IOT/assets/70581204/97baacad-f85e-4162-827f-c3fef9088672)


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
