import picamera
import time

path = '/home/pi/src3/06_multimedia'

camera = picamera.PiCamera()

now_str = time.strftime("%Y%m%d_%H%M%S")
while True:
    a = int(input(" photo: 1, video: 2, exit: 9 >>"))
    if a == 9: break
    elif a == 1:
        try:
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3)
            camera.capture('%s/photo_%s.jpg' % (path,now_str))
            camera.rotation = 180
            

        finally:
            camera.stop_preview()

    elif a == 2:
        try:
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3)
            camera.start_recording('%s/video_%s.h264' % (path,now_str))
            input("recording..")
            input("press enter to finish")
            camera.stop_recording()

        finally:
            camera.stop_preview()
