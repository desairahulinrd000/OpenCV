import matplotlib.pyplot as plt
import cv2
def main():
    imgpath="E:\\Sources\\Programming\\Python\\CV2 image processing\\Database image\\misc\\4.2.03.tiff"
    img=cv2.imread(imgpath,1)
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.title("Color image BGR")
    plt.yticks([])
    plt.xticks([])
    plt.imshow(img)
    plt.show()
    plt.title("Color image RGB")
    plt.yticks([])
    plt.xticks([])
    plt.imshow(img1)
    plt.show()
if __name__=='__main__':
    main()
