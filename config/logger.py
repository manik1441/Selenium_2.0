import logging
import logging.config
import config
def setup_logging():
    debug = config.DEBUG_LOG if hasattr(config, 'DEBUG_LOG') and config.DEBUG_LOG else False
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG' if debug else 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'file': {
                'level': 'DEBUG' if debug else 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': '../../reports/app.log',
            },
        },
        'loggers': {
            '': {
                'handlers': ['file'],
                'level': 'DEBUG' if debug else 'INFO',
                'propagate': True,
            },
        }
    }

    logging.config.dictConfig(logging_config)

