import cv2 as cv

# img = cv.imread("heart-beat.png")
# cv.imshow('heart',img)
# video

cpt = cv.VideoCapture("https://i.vimeocdn.com/video/1006505996-c5eb0efe2a621196ea11e2b75f516ec2bdf1393036e242042d5776e61f10b6d5-d_640x360.jpg")
cpt.read()
cv.waitKey(0)