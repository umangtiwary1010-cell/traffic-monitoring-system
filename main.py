import cv2 as cv
from ultralytics import YOLO

model =YOLO("yolov8n.pt")

cap = cv.VideoCapture("videos/mp_.mp4")
line_y = 300
count=0
cx,cy =0,0
counted_id =set()
previous_y = {}
while True:
    ret, frame = cap.read()

    frame=cv.resize(frame,(640,480))
    result =model.track(frame,persist=True)
    cv.line(frame,(0,300),(640,300),(0,255,0),thickness=1)
    for box in result[0].boxes:
     class_id = int(box.cls[0])

     if box.id is None:
      continue
     track_id = int(box.id[0])
     
     class_name = model.names[class_id]
     if class_name not in ["car","motorcycle","truck"]:
       continue
     x1,y1,x2,y2 = box.xyxy[0]
     x1,y1,x2,y2 = map(int,[x1,y1,x2,y2])
     cx=(x1+x2)//2
     cy=(y1+y2)//2

     cv.circle(frame,(cx,cy),5,(255,255,0),thickness=-1)
    
    
     if track_id in previous_y:
       previous_cy=previous_y[track_id]
     else :
       previous_cy = cy -1
     if track_id not in counted_id:
        if previous_cy <=line_y and cy>=line_y:
         count +=1
         print("counted")
         counted_id.add(track_id)

     previous_y[track_id]=cy
 
     
    cv.putText(frame,f"count = {count}",(20,40),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,255),thickness=2)
    cv.imshow("frame",frame)
    if cv.waitKey(1)==27:
       break
     
cap.release()
cv.destroyAllWindows()
 
     
