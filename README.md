# 🚦 Intelligent Traffic Monitoring System

A Computer Vision project built using **YOLOv8** and **OpenCV** for real-time traffic analysis.

The system detects and tracks vehicles, counts them using virtual line crossing, estimates their speed, identifies overspeeding vehicles, and generates traffic statistics.

---

## Features

* Vehicle Detection using YOLOv8
* Multi-Object Tracking with unique IDs
* Vehicle Counting using virtual line crossing
* Speed Estimation based on known road distance
* Overspeed Detection
* Traffic Analytics Report Generation

---

## Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy

---

## How It Works

### Vehicle Detection

YOLOv8 is used to detect vehicles such as:

* Cars
* Motorcycles
* Trucks

### Vehicle Tracking

Each detected vehicle is assigned a unique tracking ID, allowing the system to follow the same vehicle across multiple frames.

### Vehicle Counting

A virtual counting line is placed on the road. When a vehicle crosses this line, it is counted only once.

### Speed Estimation

Two virtual reference lines are placed at a known real-world distance apart.

When a vehicle crosses:\
1. Reference Line 1 → Start Time Recorded
2. Reference Line 2 → End Time Recorded

Speed is calculated using:

Speed = Distance / Time

and converted into km/h.

### Overspeed Detection

Vehicles exceeding the predefined speed limit are flagged as overspeeding.

### Traffic Analytics

The system generates a report containing:

* Total vehicles counted
* Number of cars
* Number of motorcycles
* Average vehicle speed
* Maximum speed observed
* Number of overspeeding vehicles

---

## Project Output

### Real-Time Output

* Vehicle Detection
* Vehicle Tracking
* Vehicle Counting
* Speed Display
* Overspeed Alerts

### Generated Statistics Report

Example:

```text
Number of car crossed = 15
Number of bike crossed = 8
Average speed of vehicles = 42.7 km/h
Number of vehicles overspeeding = 3
Maximum speed attained = 71 km/h
```

---

## Future Improvements

* Frame-based speed estimation for improved accuracy
* Number Plate Recognition (ANPR)
* Traffic Density Analysis
* Smart Traffic Signal Optimization
* Lane-wise Vehicle Statistics

---

## Learning Outcomes

This project helped me understand:

* Object Detection
* Multi-Object Tracking
* Real-Time Video Processing
* Traffic Analytics
* Computer Vision System Design

## Project Demo



https://github.com/user-attachments/assets/3feddb74-9348-45ff-83ba-f87db27c56ce
  
<img width="646" height="364" alt="Screenshot 2026-05-29 161758" src="https://github.com/user-attachments/assets/41d177b0-d281-4519-ab7f-f959474ae7a2" />


---

## Author

Ashutosh Kumar
