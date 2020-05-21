

import cv2
def main():
    j=0
    for i in dir(cv2):
        if i.startswith('COLOR_'):
            print(i)
            j+=1
    print(f'There are {j+1} color conversion flags in OpenCv')
if __name__=="__main__":
    main()
