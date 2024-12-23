import cv2

def get_image():
    # yol olarak verilen jpg dosyasını image adli  degiskene atar ve image degiskenini dondurur
    image_path = "/home/kaan/Downloads/test8.jpg"
    image = cv2.imread(image_path)

    if image is None:
        print(f"Resim {image_path} could not read!")
        return None

    return image


