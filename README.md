# AI Traffic Vehicle Counter using YOLOv8

A real-time computer vision project that detects, tracks, and counts vehicles crossing a virtual line using YOLOv8 and OpenCV.

---

## Features

* Real-time vehicle detection
* Vehicle tracking using unique IDs
* Line crossing vehicle counting
* Supports:

  * Car
  * Bus
  * Truck
  * Motorcycles
* Live counter display

---

## Technologies Used

* Python
* OpenCV
* YOLOv8
* Ultralytics
* NumPy

---

## How It Works

The system processes a traffic video feed using YOLOv8 object detection.

Each detected vehicle gets a unique tracking ID.
When the vehicle crosses the virtual counting line, the counter increases only once for that vehicle.

---

## Installation

```bash id="zkhgb0"
pip install -r requirements.txt
```

---

## Run the Project

```bash id="v60wuh"
python main.py
```

---

## Future Improvements

* Speed estimation
* Helmet detection
* Number plate recognition
* Traffic density analysis
* Multi-lane support
* Traffic signal automation

---

## Project Demo




https://github.com/user-attachments/assets/5f757258-e883-44b4-8a81-026fde068196





---

## Author

Ashutosh Kumar



