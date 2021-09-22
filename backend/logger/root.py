from loguru import logger


logger.add(
    'backend/logs/logging.log',
    format='{time:YYYY-MM-DD, HH:mm:ss} | {message}',
    rotation='10 MB',
    compression='zip',
)
