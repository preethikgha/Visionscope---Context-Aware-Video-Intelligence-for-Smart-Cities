#  VisionScope — Context-Aware Video Intelligence for Smart Cities

> Transforming passive CCTV infrastructure into an intelligent, real-time decision support platform for urban environments.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat-square&logo=opencv)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=flat-square&logo=streamlit)

---

##  Overview

Modern smart cities deploy extensive CCTV infrastructure, but most systems remain passive — limited to recording or basic motion detection. **VisionScope** addresses this gap by introducing **context-aware intelligence**, enabling automated interpretation of traffic and crowd dynamics in real time.

The system goes beyond detection to provide **actionable insights**, assisting urban authorities in real-time decision-making across traffic management, crowd control, and event monitoring.

---

##  Core Capabilities

| Feature | Description |
|---|---|
| - Real-time Object Detection | YOLOv8-powered detection with bounding boxes and confidence scores |
| - Vehicle & Pedestrian Counting | Frame-level count aggregation for traffic and crowd analysis |
| - Traffic Density Classification | Low / Medium / High based on rule-based thresholds |
| - Crowd Density Classification | Sparse / Moderate / Dense with contextual interpretation |
| - Context-Aware Reasoning | Integrates time of day, location type, and day-of-week |
| - Advisory Generation | Automated, scenario-specific recommendations for authorities |
| - Analytics Logging | Persistent CSV-based storage for trend analysis |
| - Interactive Dashboard | Streamlit-based real-time visualization |

---

##  System Architecture
```
Video Input
    ↓
Frame Extraction         [OpenCV]
    ↓
Object Detection         [YOLOv8]
    ↓
Object Counting          [Bounding Box Aggregation]
    ↓
Density Classification   [Rule-Based Thresholds]
    ↓
Context Integration      [Time · Location · Day Type]
    ↓
Decision Engine          [Advisory Generation]
    ↓
Analytics Storage        [CSV Logging]
    ↓
Dashboard Visualization  [Streamlit]
```

---

##  Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| Computer Vision | OpenCV |
| Deep Learning | YOLOv8 (Ultralytics) |
| Data Handling | Pandas |
| Dashboard | Streamlit |
| Storage | CSV |

---

##  Algorithms & Concepts

### 1. Object Detection — YOLOv8

- Single-stage detector optimized for real-time inference
- Outputs bounding boxes, class labels, and confidence scores per frame
- Pretrained on dataset; detects 80+ object classes including `car`, `truck`, `bus`, `person`, `motorcycle`

### 2. Density Classification

**Traffic Density (Vehicles):**
```
< 10  vehicles  →  Low
10–25 vehicles  →  Medium
> 25  vehicles  →  High
```

**Crowd Density (Persons):**
```
< 15  persons  →  Sparse
15–40 persons  →  Moderate
> 40  persons  →  Dense
```

### 3. Context-Aware Reasoning

Context variables injected at inference time:
- **Time of day** — Morning / Afternoon / Evening / Night
- **Day type** — Weekday / Weekend / Holiday
- **Location type** — Intersection / Highway / Commercial Zone / Event Venue

Scenario examples:
```
High Traffic + Peak Hour          →  Congestion Alert
Dense Crowd + Night + Commercial  →  Crowd Safety Advisory
Medium Traffic + Weekend          →  Routine Monitoring
Sparse + Off-Peak                 →  Normal — No Action Required
```




---

##  Getting Started
```bash
# Clone the repo
git clone https://github.com/your-username/VisionScope.git
cd VisionScope

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run python detection/object_detector.py
```




---

##  Future Enhancements

- [ ] Multi-camera feed support
- [ ] Incident detection (accidents, abandoned objects)
- [ ] License plate recognition
- [ ] Alert push notifications (SMS / Email)
- [ ] Edge deployment (Jetson Nano / Raspberry Pi)
- [ ] Fine-tuned model on Indian urban datasets

---




##  Author


**Preethikgha**  
