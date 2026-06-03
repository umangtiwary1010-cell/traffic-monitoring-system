import cv2 as cv
from ultralytics import YOLO
import time 

model =YOLO("yolov8n.pt")

cap = cv.VideoCapture("videos/mp_.mp4")

fps =int(cap.get(cv.CAP_PROP_FPS))
print(fps)
out = cv.VideoWriter(
    "traffic_output.mp4",
    cv.VideoWriter_fourcc(*'mp4v'),
    fps,
    (640, 480)
)

speed = {}
line_y = 300
speed_calculated =set()
count=0
count_line_1=150
overspeeding=set()
count_line_2=260
cx,cy =0,0
prev_x,prev_y = 0,0
counted_id =set() 
curr_time={}
prev_time={}
previous_y = {}
car_count=0
bike_count =0 
speed_limit=50

while True:
    ret, frame = cap.read()
    if not ret:
     break


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
         counted_id.add(track_id)
         if class_name == "car":
          car_count+=1
         if class_name == "motorcycle":
          bike_count +=1
         print("counted")

     if previous_cy <=count_line_1 and cy>=count_line_1:
       prev_time[track_id] =time.time()
     if previous_cy <=count_line_2 and cy>=count_line_2:
       curr_time[track_id]=time.time()

     previous_y[track_id]=cy
     
     if track_id not in speed_calculated:
      if track_id in curr_time and track_id in prev_time:
       delta_t = curr_time[track_id]-prev_time[track_id]
       if delta_t>0:   
        speed[track_id] = int((11/delta_t)*3.6)
        speed_calculated.add(track_id)
        
     if track_id in speed:
      cv.putText(frame,f"{speed[track_id]} km/h",(cx,cy-10),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
     
      if speed[track_id]>50:
       cv.putText(frame,"overspeeding",(cx,cy),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255),thickness=1)
       overspeeding.add(track_id)
     
    cv.putText(frame,f"count = {count} ",(20,40),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,255),thickness=2)

    out.write(frame)
    cv.imshow("frame",frame)
    if cv.waitKey(1)==27:
       break

avg = round(sum(speed.values())/len(speed),2) if speed else 0
max_speed = max(speed.values()) if speed else 0


stats = f''' Traffic Analytics Report

Number of car crossed = {car_count}
Number of bike crossed = {bike_count}
average speed of vehicles  = {avg}
Number of vehicles overspeeding = {len(overspeeding)}
Maximum speed attained  = {max_speed}
'''
with open("stats.txt","w") as f:
      f.write(stats)

cap.release()
out.release()
cv.destroyAllWindows()
 
     
