import logging

class Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('{asctime} - {levelname} - {message}', style='{')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    @classmethod
    def info(cls, message):
        cls.logger.info(message)
    
    @classmethod
    def warning(cls, message):
        cls.logger.warning(message)

    @classmethod
    def debug(cls, message):
        cls.logger.debug(message)

    @classmethod
    def exception(cls, message):
        cls.logger.exception(message)


