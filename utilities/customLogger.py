import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_file = os.path.abspath(os.curdir) + "\\logs\\automation.log"

        logger = logging.getLogger("SaucedemoLogger")
        logger.setLevel(logging.DEBUG)

        # Avoid adding duplicate handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode='a')
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            selenium_logger = logging.getLogger('selenium')
            selenium_logger.setLevel(logging.DEBUG)
            selenium_logger.addHandler(file_handler)
            


        return logger
