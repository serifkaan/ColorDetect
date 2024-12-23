import cv2
from streamer import get_image
from image_process import ImageProcessor
from config import loadConfig
from logger import setup_logger

# loggeri baslatıyoruz
logger = setup_logger()

def main():
    # config.toml dosyasindaki degerler config degiskenine yukleniyor
    config = loadConfig("/home/kaan/PycharmProjects/ColorDetect/config/config.toml")

    #goruntu streamer.py dosyasindaki get_image fonksiyonu ile image degiskenine yukleniyor
    image = get_image()


    # goruntu alinamazsa log dosyasina error levelinde log olarak kaydet
    if image is None:
        logger.error("Image not found!")
        return


    # ImageProcessor sınıfına config degiskenini parametre olarak verdik
    processor = ImageProcessor(config,logger)



    # processor ile process_image fonksiyonuna erisip bu fonkisyonun dondurdugu degerleri yeni degiskenlere atadık
    blue_output, green_output, red_output, yellow_output = processor.process_image(image)

    # sonuc olarak da 3 ayrı pencere seklinde renklerin tespit edildigi pikselleri cıktı olarak alıyoruz
    cv2.imshow("Original",image)
    cv2.imshow("Blue", blue_output)
    cv2.imshow("Green", green_output)
    cv2.imshow("Red", red_output)
    cv2.imshow("Yellow",yellow_output)



    # burada program herhangi bir tusa basılmasını bekliyor basınca programdan cikiyor

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# eger app.py dogrudan calıstırılırsa main() fonksiyonu calısır eger baska bir dosyadan import edilirse calısmaz
if __name__ == "__main__":
    main()
