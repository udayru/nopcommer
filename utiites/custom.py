import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./logs/automaticlogs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m %d %Y %I %M %S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

