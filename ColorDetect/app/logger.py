from loguru import logger

# loggeri yapılandirdiyoruz
def setup_logger():
    #logger.add fonksiyonu ile app.log dosyasinda loglar tutulacak
    logger.remove()
    logger.add("/home/kaan/PycharmProjects/ColorDetect/logs/app.log", rotation="500 MB",mode="w")
    return logger
