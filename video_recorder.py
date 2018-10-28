import os
import cv2
FILE_OUTPUT = 'live.avi'
def video_recorder():
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)
    cap = cv2.VideoCapture(0)
    currentFrame = 0
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'X264')
    out = cv2.VideoWriter(FILE_OUTPUT, fourcc, 20.0, (int(width), int(height)))
    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('my webcam', frame)
        if cv2.waitKey(1) == 27:
            break
        currentFrame += 1
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_recorder()
