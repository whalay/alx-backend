#!/usr/bin/env python3
""" basic babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config(object):
    """ config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """ get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """ index.html """
    return render_template('3-index.html',
                           title=gettext('home_title'),
                           body=gettext('home_header'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
