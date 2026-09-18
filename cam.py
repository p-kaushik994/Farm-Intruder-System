from ultralytics import YOLO
import cv2
import winsound

model=YOLO("yolov8n.pt")

capture=cv2.VideoCapture(0)

target = ['person','dog','cow','cat','buffalo']
sound={"person":(1000,500),
       "dog":(700,300),
       "cow":(500,400),
       "cat":(800,200),
       "buffalo":(400,600)}

detected_count={}
thresold=5


while True:

    ret , frame = capture.read()

    if not ret:
        break

    result = model(frame,verbose=False)

    annotated_frame = result[0].plot()

    detected_frame = {}

    for r in result:
        for box in r.boxes:
            label=model.names[int(box.cls[0])]
            confidence = float(box.conf[0])

            if label in target and confidence >= 0.6:
                detected_frame[label]=confidence

    for label in detected_frame:
        detected_count[label]=detected_count.get(label,0)+1

    for label in list(detected_count.keys()):
        if label not in detected_frame:
            detected_count[label]=0

    for label,count in detected_count.items():

        if count==thresold:

            print(f"🚨 Stable detection : {label} (conf: {detected_frame.get(label,0):.2f})")

            detected_count[label]+=1000                 #alert section
            cv2.putText(annotated_frame,f"ALERT: {label.upper()}",(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),2)

        if label in sound:
            freq,dur = sound[label]
            winsound.Beep(freq,dur)

            
    cv2.imshow("Detected",annotated_frame)

    if cv2.waitKey(1) & 0xFF ==27:
        break

capture.release()
cv2.destroyAllWindows()

