log_level_for_log_files = 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s (%(name)s) %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_main': {
            'level': log_level_for_log_files,
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': './logs/euiv_management.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file_main', ],
            'level': 'INFO',
        },
        'EUIVSaveGame': {
            'handlers': ['console', 'file_main', ],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'file_main', ],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console', 'file_main', ],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file_main', ],
            'level': 'INFO',
        },
    }
}
