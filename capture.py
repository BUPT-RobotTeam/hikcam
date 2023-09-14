#!/usr/bin/env python
print('loading libraries...')
import cv2
import numpy as np
import sys
sys.path.append('./build')
# for msbuild
sys.path.append('./build/Release')
sys.path.append('./build/Debug')
import hikcam

print('initializing camera...')
capture = hikcam.hikcam()

if not capture.enumerate():
    print("no device found")
    exit(1)

capture.open(0)
capture.start()
imgSize = (1280, 1024)

while True:
    frame = capture.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 理论上这个色彩空间转换是不需要的，C++库已经转成RGB了
    # 但不知道为什么要转一下才正常
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    # 把 1280x1024 转成 640x512
    cv2.imshow("video", frame)
    print(f"fps={capture.fps()}")
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
capture.stop()
