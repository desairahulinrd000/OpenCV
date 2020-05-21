import cv2

def main():
    
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(0)
    
    filename="D:\\New folder\\Documents\\My programms\\Python\\CV2\\demo video.avi"
    codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
    framerate = 30
    resolution = (640, 480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    
    VideoFileOutput.release()
    cap.release()

if __name__ == "__main__":
    main()
