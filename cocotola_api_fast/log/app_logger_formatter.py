import json
import logging


def get_app_log(record):
    json_obj = {
        'name': record.name,
        'level': record.levelname,
        'type': 'app',
        'timestamp': record.asctime,
        # 'filename': record.filename,
        'pathname': record.pathname,
        'line': record.lineno,
        'threadId': record.thread,
        'message': record.message,
        'stack': record.stack_info
    }

    return json_obj


class CustomFormatter(logging.Formatter):

    def format(self, record):
        logging.Formatter.format(self, record)
        return json.dumps(get_app_log(record))


# LOGGER = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'default': {
#             '()': 'cocotola_api_fast.log.app_logger_formatter.CustomFormatter',
#             'fmt': '%(asctime)s',
#         }
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'INFO',
#             'formatter': 'default',
#             'stream': 'ext://sys.stdout'
#         },
#     },
#     'loggers': {
#         'sqlalchemy.engine': {
#             'level': 'WARNING',
#             'handlers': [
#               'console',
#             ],
#             'propagate':False,
#           },
#     },
#     # 'root': {
#     #     'level': 'DEBUG',
#     #     'handlers': [
#     #       'console',
#     #     ]
#     #   },
# }
