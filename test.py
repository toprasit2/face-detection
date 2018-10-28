#import sys
import cv2

#img_name = sys.argv[1]
img_name = 'Drawing.png'
im = cv2.imread(img_name)
#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(im, 'OpenCV With Python', (80, 100), font, 1, (0, 0, 0), 2 , cv2.LINE_AA)
cv2.namedWindow('OriginalImage', cv2.WINDOW_NORMAL)
cv2.imshow('OriginalImage', im)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

