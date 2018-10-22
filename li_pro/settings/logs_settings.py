# coding=utf-8

import logging
import os

LOG_DIR = '/data/log/yanzhe/app/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d  %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'raw': {
            'format': '%(message)s'
        }
    },

    'handlers': {
        # 'null': {
        #     'level': 'DEBUG',
        #     'class': 'django.utils.log.NullHandler',
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler'
        # },

        # 默认的服务器Log(保存到log/filelog.log中, 通过linux的logrotate来处理日志的分割
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'filelog.log'),
            'formatter': 'verbose',
        },

        # 默认的服务器ERROR log
        'default_err': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error_logger.log'),
            'formatter': 'verbose',
        },
        'exception_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'exception_logger.log'),
            'formatter': 'raw',
        },
        'ticker_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'ticker_logger.log'),
            'formatter': 'verbose',
        },
        'push_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'push_logger.log'),
            'formatter': 'verbose',
        },
        'elapsed_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'elapsed_logger.log'),
            'formatter': 'verbose',
        },
        'info_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info_logger.log'),
            'formatter': 'verbose',
        },
        'auth_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'auth_logger.log'),
            'formatter': 'verbose',
        },
        'webproblem_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'webproblem_logger.log'),
            'formatter': 'verbose',
        },
        'sql_logger': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'sql.log'),
            'formatter': 'verbose',
        },
        'pay_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'pay.log'),
            'formatter': 'verbose',
        },
        'search_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'search.log'),
            'formatter': 'verbose',
        },
        'ip_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'ip.log'),
            'formatter': 'verbose',
        },
        'profile_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'profiler.log'),
            'formatter': 'raw',
        },
        'refund_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'refund_logger.log'),
            'formatter': 'verbose',
        },
        'dr_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'dr_logger.log'),
            'formatter': 'verbose',
        },
        'apple_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'apple_logger.log'),
            'formatter': 'verbose',
        },
        'antispam_handler': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'antispam_logger.log'),
            'formatter': 'verbose',
        },
        'channel_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'channel_logger.log'),
            'formatter': 'verbose',
        },
        'cpc_click_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'cpc_click_logger.log'),
            'formatter': 'verbose',
        },
        'tracer_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'tracer.log'),
            'formatter': 'raw'
        },
        'momo_stat_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'momo_stat.log'),
            'formatter': 'verbose',
        }
    },

    'loggers': {
        # 默认都交给django了
        'django': {
            'handlers': ['default'],
            'propagate': True,
            'level': 'INFO',
        },
        'gm_tracer.subscribe': {
            'handlers': ['tracer_handler'],
            'propagate': False,
            'level': 'INFO'
        },
        'django.request': {
            'handlers': ['default_err'],
            'level': 'ERROR',
            'propagate': False,
        },
        'exception_logger': {
            'handlers': ['exception_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'ticker_logger': {
            'handlers': ['ticker_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'push_logger': {
            'handlers': ['push_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'elapsed_logger': {
            'handlers': ['elapsed_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'info_logger': {
            'handlers': ['info_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'auth_logger': {
            'handlers': ['auth_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'err_logger': {
            "handlers": ['default_err'],
            'level': "ERROR",
            "propagate": False,
        },
        'pay': {
            'handlers': ['pay_logger'],
            'propagate': True,
            'level': 'INFO',
        },
        'search': {
            'handlers': ['search_logger'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['sql_logger'],
        },
        'ip_logger': {
            'handlers': ['ip_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'profile_logger': {
            'handlers': ['profile_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'refund_logger': {
            'handlers': ['refund_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'dr_logger': {
            'handlers': ['dr_handler'],
            'propagate': True,
            'level': 'INFO',
        },
        'apple_logger': {
            'handlers': ['apple_handler'],
            'propagate': True,
            'level': 'INFO',
        },
        'antispam_logger': {
            'handlers': ['antispam_handler'],
            'propagate': False,
            'level': 'WARNING',
        },
        'channel_logger': {
            'handlers': ['channel_handler'],
            'propagate': False,
            'level': 'INFO',
        },
        'cpc_click_logger': {
            'handlers': ['cpc_click_handler'],
            'propagate': False,
            'level': 'INFO',
        },
        'momo_stat_logger': {
            'handlers': ['momo_stat_handler'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d  %(message)s',
    filename=os.path.join(LOG_DIR, 'filelog.log'),
)


# def GM_LOGGING():
#     try:
#         from .settings_local import DEBUG
#     except ImportError:
#         DEBUG = False
#     return {
#         'request_info_extractor_class': 'libs.logging.RequestInfoExtractor',
#         'log': {
#             'basedir': LOG_DIR,
#             'prefix': 'backend',
#             'buffered': not DEBUG,
#         }
#     }
