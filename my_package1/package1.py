from configs import config_logger

logger = config_logger.get_logger(__name__)


def process(msg):
    logger.info("Перед процессом")
    print(msg)
    logger.info("После процесса")
