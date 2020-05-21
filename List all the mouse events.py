import cv2

def main():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    for j in events:
        print(j)

if __name__ == "__main__":
    main()
