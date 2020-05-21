import cv2
import matplotlib.pyplot as plt

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

 
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    

    cap.release()
    return img1
if __name__ == "__main__":
    a=main()
    b=cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow("Camera Image",b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
