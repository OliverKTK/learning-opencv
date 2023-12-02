import cv2
import sys

s= 0
if len(sys.argv) > 1:
    s = sys.argv[1]
cap = cv2.VideoCapture(s)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out_mp4 = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*"XVID"), 17, (frame_width, frame_height))

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: #Escape
    has_frame, frame = cap.read()
    if not has_frame:
        break

    else:
        out_mp4.write(frame)
    cv2.imshow(win_name, frame)

cap.release()
cv2.destroyWindow(win_name)
out_mp4.release()