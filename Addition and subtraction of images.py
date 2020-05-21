import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "E:\\Sources\\Programming\\Python\\CV2 image processing\\Database image\\misc\\"
    
    imgpath1 =  path + "4.2.01.tiff"
    imgpath2 =  path + "4.2.03.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    add = img1 + 50
    
    sub1 = img1 - 50
    sub2 = 50 - img1
    
    titles = ['Liquid Drop', 'Lena', 'Addition', 'img1 - img2', 'img2 - img1']
    images = [img1, img2, add, sub1, sub2]
    
    
    
    for i in range(5):
        plt.subplot(1, 5, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()
