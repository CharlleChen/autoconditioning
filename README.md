# AutoConditioning (Automatic Air Conditioner)
This project proposes to automatically adjust temparature based on the number of people in the room. It utilized Computer Visions, embedded systems and web development to deploy the project. This is a project for [Uncommon Hacks 2021](https://uncommon-hacks-2021.devpost.com). Checkout the devpost blog [here](https://devpost.com/software/autoconditioning). It has been awareded with "Best Hardware Award" sponsored by Dgi-Key and "Most Impactful Award".

# Achieved functions
- Detect the number of people in the room and display the number on a website
- Mannually adjust the temparature of the AC via the Internet when the intelligent tempareture policy doesn't work well

# Technical specifications
- Utilized AI-powered Camera Module [VisionSeed](https://visionseed.youtu.qq.com/) and its Python SDK
- Deployed Objected-Detection algorithm on the module
- Used Raspberry Pi for edge deployment
- Constructed the cloud side with Flask framework
- Utilized web socket to communicate between edge-end and cloud-end

# File structure
## cloud-end codes
- flash_server

## raspberrypi codes
- gateway_raspberrypi.py
