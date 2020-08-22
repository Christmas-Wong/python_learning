import myLogger
import logging.config
from loguru import logger

def log_by_config():
    print("*"*10+"logging config"+"*"*10)
    logging.config.fileConfig('./log/logging.config')

    # create logger
    logger = logging.getLogger('simpleExample')

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

def my_logger():
    print("*"*10+"my logger"+"*"*10)
    logger = myLogger.get_logger()
    logger.info("my_logger")

def loguru_logger():
    print("*" * 10 + "my logger" + "*" * 10)
    logger.add('loguru.log')
    logger.info("loguru")

if __name__ == "__main__":
    my_logger()
    log_by_config()
    loguru_logger()

