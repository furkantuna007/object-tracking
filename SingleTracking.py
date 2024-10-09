import cv2
import sys
from random import randint

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
tracker_type = tracker_types[2]

if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
elif tracker_types == 'MIL':
    tracker = cv2.legacy.TrackerMIL_create()
elif tracker_types == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
elif tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracker_type == 'GOTURN':
    tracker = cv2.legacy.TrackerGOTURN_create()

video = cv2.VideoCapture('videos/race.mp4')
if not video.isOpened():
    print('Could not open video file')
    sys.exit()

ok, frame = video.read()
if not ok:
    print('Could not read video file')
    sys.exit()

bbox = cv2.selectROI(frame) #box region
print(bbox)

ok = tracker.init(frame, bbox)
print(ok)

colors = (randint(0, 255), randint(0, 255), randint(0, 255)) #RGB

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = tracker.update(frame)
    print(ok, bbox)
    if ok == True:
        (x,y,w,h) = [int (x) for x in bbox]
        print(x,y,w,h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), colors, 2, 1)
    else:
        cv2.putText(frame, 'Unable to track the object.', (100,80), cv2.FONT_HERSHEY_SIMPLEX, 1, colors, 2 )

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break









