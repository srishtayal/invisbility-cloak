import cv2
import numpy as np
import time

# Check OpenCV version
print(cv2.__version__)
print(np.__version__)

capture_video = cv2.VideoCapture(0)  

time.sleep(1)

count = 0
background = None

for i in range(60):
    return_val, background = capture_video.read()
    if not return_val:
        print("Failed to capture frame, skipping...")
        continue

    if background is None:
        print("Error: Background frame is None!")
        break

if background is not None:
    background = np.flip(background, axis=1)  
else:
    print("Error: Background is None!")
    exit()

while capture_video.isOpened():
    return_val, img = capture_video.read()
    if not return_val:
        break
    count += 1
    img = np.flip(img, axis=1)  


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    lower_red1 = np.array([0, 120, 70])   
    upper_red1 = np.array([10, 255, 255])  

    lower_red2 = np.array([170, 120, 70])  
    upper_red2 = np.array([180, 255, 255])  


    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 + mask2

    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    red_mask = cv2.dilate(red_mask, np.ones((3, 3), np.uint8), iterations=1)

    non_red_mask = cv2.bitwise_not(red_mask)

    res1 = cv2.bitwise_and(background, background, mask=red_mask)  
    res2 = cv2.bitwise_and(img, img, mask=non_red_mask) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 

    cv2.imshow("INVISIBLE MAN", final_output)

    k = cv2.waitKey(10)
    if k == 27: 
        break

capture_video.release()
cv2.destroyAllWindows()