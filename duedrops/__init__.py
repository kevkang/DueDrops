import os
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('duedrops.default_settings')
app.config.from_envvar('DUEDROPS_SETTINGS')
mail = Mail(app)

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'duedrops.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)

import duedrops.views
