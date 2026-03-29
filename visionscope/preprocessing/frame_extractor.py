import cv2

video_path = "data/traffic_video/sample.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

frame_id = 0
skip_frames = 5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_id += 1

    if frame_id % skip_frames != 0:
        continue

    resized_frame = cv2.resize(frame, (640, 360))

    cv2.imshow("VisionScope - Processed Frame", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
