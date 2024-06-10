#!/usr/bin/env python3
from flask_babel import Babel
'''creating a flask app'''


class Config:
    '''configure the app'''
    def __init__(self, app) -> None:
        self.LANGUAGES = ["en", "fr"]
        app.config['BABEL_DEFAULT_LOCALE'] = 'en'
        app.config['BABEL_SUPPORTED_LOCALES'] = self.LANGUAGES
        app.config['DEFAULT_TIMEZONE'] = 'UTC'

app = __import__('0-app').app
app = Config(app)
babel = Babel(app)