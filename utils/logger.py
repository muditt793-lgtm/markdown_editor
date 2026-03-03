import logging
import sys
from pathlib import Path
from config.settings import LOG_LEVEL, LOG_FORMAT, LOG_FILE, LOGS_DIR

class LoggerConfig:
    _logger = None
    
    @staticmethod
    def get_logger(name=None):
        if LoggerConfig._logger is None:
            LoggerConfig._logger = LoggerConfig._setup_logger(name or "MarkdownEditor")
        return LoggerConfig._logger
    
    @staticmethod
    def _setup_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, LOG_LEVEL))
        
        LOGS_DIR.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(getattr(logging, LOG_LEVEL))
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, LOG_LEVEL))
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger

logger = LoggerConfig.get_logger()
