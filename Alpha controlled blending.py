
import cv2

def emptyFunction(pos):
    
    pass

def main():
    
    path = "E:\\Sources\\Programming\\Python\\CV2 image processing\\Database image\\misc\\"
    
    imgpath1 =  path + "4.2.05.tiff"
    imgpath2 =  path + "4.2.01.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    
    
    windowName = "Transition Demo"
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('Alpha', windowName, 0, 1000, emptyFunction)
    
    while(True):
        
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
        
        alpha = cv2.getTrackbarPos('Alpha', windowName) / 1000
        beta = 1 - alpha
        
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        
        
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
