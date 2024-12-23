import cv2
import numpy as np
from logger import setup_logger


class ImageProcessor:
    def __init__(self, config,logger):
        self.config = config
        self.logger = setup_logger()

    def process_image(self, image):

        # goruntuyu hsv formatına cevirir
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # girilen renkteki degerler 1(beyaz) digerleri ise 0(siyah) seklinde maskelenecek
        # mavi renk tespiti
        blue_lower = np.array(self.config['colors']['blue_lower'])
        blue_upper = np.array(self.config['colors']['blue_upper'])
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)# hsv formatinda ust ve alt degerleri verilmis bir maske olusturur.ust ve alt degerler yukarıdaki iki satırda config.tomlden alınıyor
        blue_output = cv2.bitwise_and(image, image, mask=blue_mask) # goruntu ile maskenin ayni konumdaki pikselleri karsilastirilir ikisi de 1 ise sonuc 1 biri 0 ise 0 (logic and islemi)
        blue_pixels = np.count_nonzero(blue_mask)# maskedeki toplam beyaz sayisini sayiyoruz ve color_pixels adli degiskene atiyoruz

        # yeşil renk tespiti
        green_lower = np.array(self.config['colors']['green_lower'])
        green_upper = np.array(self.config['colors']['green_upper'])
        green_mask = cv2.inRange(hsv, green_lower, green_upper) # hsv formatinda ust ve alt degerleri verilmis bir maske olusturur.ust ve alt degerler yukarıdaki iki satırda config.tomlden alınıyor
        green_output = cv2.bitwise_and(image, image, mask=green_mask)# goruntu ile maskenin ayni konumdaki pikselleri karsilastirilir ikisi de 1 ise sonuc 1 biri 0 ise 0 (logic and islemi)
        green_pixels = np.count_nonzero(green_mask)# maskedeki toplam beyaz sayisini sayiyoruz ve color_pixels adli degiskene atiyoruz


        # kırmızı renk tespiti.iki ayri aralikta kontrol edilir cunku hsv spektrumunda iki ayri ucta yer alır
        red_lower1 = np.array(self.config['colors']['red_lower1'])
        red_upper1 = np.array(self.config['colors']['red_upper1'])
        red_lower2 = np.array(self.config['colors']['red_lower2'])
        red_upper2 = np.array(self.config['colors']['red_upper2'])
        red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
        red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
        red_mask = cv2.bitwise_or(red_mask1, red_mask2)# hsv formatinda ust ve alt degerleri verilmis bir maske olusturur.ust ve alt degerler yukarıdaki iki satırda config.tomlden alınıyor
        red_output = cv2.bitwise_and(image, image, mask=red_mask) # goruntu ile maskenin ayni konumdaki pikselleri karsilastirilir ikisi de 1 ise sonuc 1 biri 0 ise 0 (logic and islemi)
        red_pixels = np.count_nonzero(red_mask) # maskedeki toplam beyaz sayisini sayiyoruz ve color_pixels adli degiskene atiyoruz

        yellow_lower = np.array(self.config['colors']['yellow_lower'])
        yellow_upper = np.array(self.config['colors']['yellow_upper'])
        yellow_mask = cv2.inRange(hsv,yellow_lower,yellow_upper)
        yellow_output = cv2.bitwise_and(image,image,mask=yellow_mask)
        yellow_pixels = np.count_nonzero(yellow_mask)

        # Maskelerin boş olup olmadığını kontrol etmek icin color_detected adlı bir dizi olusturuldu
        color_detected = {}

        # Girilen renkteki degerli piksel maskede en az bir tane bile varsa true yoksa false.ve bu bool deger color_detected[color] anahtarına atanır
        color_detected['blue'] = np.any(blue_mask)
        color_detected['green'] = np.any(green_mask)
        color_detected['red'] = np.any(red_mask)
        color_detected['yellow'] = np.any(yellow_mask)

        # color_detected dizisinin elemanlarıyla tek tek renklerin tespit edilip edilmedigini tespit edip log olarak kaydediyoruz.

        if color_detected['blue']:
            self.logger.success(f"Blue color has been detected. Blue pixels:{blue_pixels}")

        else:
            self.logger.info("Blue color could not detected.")

        if color_detected['green']:
            self.logger.success(f"Green color has been detected. Green pixels:{green_pixels}")

        else:
            self.logger.info("Green color could not detected.")

        if color_detected['red']:
            self.logger.success(f"Red color has been detected. Red pixels:{red_pixels}")

        else:
            self.logger.info("Red color could not detected.")

        if color_detected['yellow']:
            self.logger.success(f"Yellow color has been detected. Yellow pixels:{yellow_pixels}")

        else:
            self.logger.info("Yellow color could not detected")


        return blue_output, green_output, red_output,yellow_output

        # sonuc olarak fonksiyon renkleri ayri ayri iceren degerleri (color_output) , color_detected dizisini ve toplam beyazlari dondurecek


