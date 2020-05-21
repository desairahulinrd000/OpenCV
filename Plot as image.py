import matplotlib.pyplot as plt
import cv2
def main():
    imgpath="E:\\Sources\\Programming\\Python\\CV2 image processing\\Database image\\misc\\4.2.03.tiff"
    img=cv2.imread(imgpath,0)
    plt.imshow(img)
    plt.show()
    plt.yticks([])
    plt.xticks([])
    plt.imshow(img,cmap='Blues')
    plt.show()
    plt.imshow(img,cmap='Reds')
    plt.show()
    plt.imshow(img,cmap='Accent')
    plt.show()
    plt.imshow(img,cmap='seismic')
    plt.show()
    plt.imshow(img,cmap='Spectral')
    plt.show()
if __name__=='__main__':
    main()
