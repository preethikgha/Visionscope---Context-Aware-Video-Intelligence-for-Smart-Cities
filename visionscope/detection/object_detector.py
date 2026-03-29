import cv2
import csv
from datetime import datetime
from ultralytics import YOLO

# -------------------------------
# LOAD YOLO MODEL
# -------------------------------
model = YOLO("yolov8n.pt")

# -------------------------------
# VIDEO SOURCE
# -------------------------------
video_path = "data/traffic_video/sample.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

# -------------------------------
# CREATE CSV FILE
# -------------------------------
csv_file = open("analytics_log.csv", mode="w", newline="")
csv_writer = csv.writer(csv_file)

csv_writer.writerow([
    "timestamp",
    "vehicle_count",
    "people_count",
    "traffic_status",
    "crowd_status",
    "location_type",
    "time_of_day",
    "day_type",
    "advisory"
])

# -------------------------------
# MAIN LOOP
# -------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()

    # ---- Automatic Context ----
    location_type = "road"

    if 6 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 17:
        time_of_day = "afternoon"
    elif 17 <= hour < 22:
        time_of_day = "evening"
    else:
        time_of_day = "night"

    day_type = "weekday" if weekday < 5 else "weekend"

    results = model(frame)

    vehicle_count = 0
    people_count = 0

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            if class_name in ["car", "bus", "truck", "motorbike"]:
                vehicle_count += 1

            if class_name == "person":
                people_count += 1

    # ---- Density Classification ----
    if vehicle_count < 10:
        traffic_status = "Low Traffic"
    elif vehicle_count < 25:
        traffic_status = "Medium Traffic"
    else:
        traffic_status = "High Traffic"

    if people_count < 15:
        crowd_status = "Sparse Crowd"
    elif people_count < 40:
        crowd_status = "Moderate Crowd"
    else:
        crowd_status = "Dense Crowd"

    # ---- Advisory Logic ----
    advisory = "Normal monitoring."

    if traffic_status == "High Traffic" and time_of_day in ["morning", "evening"]:
        advisory = "Heavy congestion detected. Suggest traffic rerouting."

    elif traffic_status == "Medium Traffic" and location_type == "road":
        advisory = "Moderate traffic flow. Monitor signal timing."

    elif crowd_status == "Dense Crowd" and location_type == "market":
        advisory = "High crowd density. Deploy crowd control personnel."

    elif crowd_status == "Sparse Crowd":
        advisory = "Low public activity. No action required."

    # ---- Write to CSV ----
    csv_writer.writerow([
        now.strftime("%Y-%m-%d %H:%M:%S"),
        vehicle_count,
        people_count,
        traffic_status,
        crowd_status,
        location_type,
        time_of_day,
        day_type,
        advisory
    ])

    # ---- Visualization ----
    annotated_frame = results[0].plot()

    cv2.putText(annotated_frame, f"Vehicles: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(annotated_frame, f"People: {people_count}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(annotated_frame, traffic_status, (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.putText(annotated_frame, crowd_status, (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.putText(annotated_frame, advisory, (20, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("VisionScope - Smart Analysis", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
csv_file.close()
cv2.destroyAllWindows()