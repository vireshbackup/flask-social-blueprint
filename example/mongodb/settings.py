# coding=utf-8
# Created 2014 by Janusz Skonieczny 

# coding=utf-8
#
# Copyright 2010 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.

import logging
import os

SRC_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# ============================================================================
#  a flask settings
#  http://flask.pocoo.org/docs/config/#configuring-from-files
# ============================================================================

SECRET_KEY = os.environ.get('SECRET_KEY', '47e585de7f22984d5ee291c2f31412384bfc32d0')
FLASH_MESSAGES = True

MONGODB_SETTINGS = dict(
    db=os.environ.get('MONGODB_DATABASE', 'flask_social_blueprint'),
    host=os.environ.get('MONGODB_PORT_27017_TCP_ADDR', '127.0.0.1'),
    port=int(os.environ.get('MONGODB_PORT_27017_TCP_PORT', 27017)),
    username=os.environ.get('MONGODB_USERNAME', None),
    password=os.environ.get('MONGODB_PASSWORD', None),
    tz_aware=False if 'MONGODB_NO_TZ_AWARE' in os.environ else True,
)

# Flask-Login
# https://flask-login.readthedocs.org/en/latest/#protecting-views

LOGIN_DISABLED = False

# Flask-Security
# http://pythonhosted.org/Flask-Security/configuration.html

#SECURITY_URL_PREFIX = '/_social'

SECURITY_PASSWORD_SALT = "abc"
# SECURITY_PASSWORD_HASH = "bcrypt"  # requires py-bcrypt
# SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_HASH = "plaintext"
SECURITY_EMAIL_SENDER = "support@example.com"

SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True

SECURITY_CONFIRM_SALT = "570be5f24e690ce5af208244f3e539a93b6e4f05"
SECURITY_REMEMBER_SALT = "de154140385c591ea771dcb3b33f374383e6ea47"
SECURITY_DEFAULT_REMEMBER_ME = True

# Set secret keys for CSRF protection
CSRF_SESSION_KEY = '8a7474974efcf76896aa84eea9cbe016bbc08828'
CSRF_ENABLED = True

# Flask-Babel
# http://pythonhosted.org/Flask-Babel/
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = "UTC"

# Flask-Mail
# http://pythonhosted.org/Flask-Mail/
SERVER_EMAIL = 'Flask-SocialBlueprint <support@example.com>'

# Flask-SocialBlueprint
# https://github.com/wooyek/flask-social-blueprint
SOCIAL_BLUEPRINT = {
    # https://developers.facebook.com/apps/
    "flask_social_blueprint.providers.Facebook": {
        # App ID
        'consumer_key': '197…',
        # App Secret
        'consumer_secret': 'c956c1…'
    },
    # https://apps.twitter.com/app/new
    "flask_social_blueprint.providers.Twitter": {
        # Your access token from API Keys tab
        'consumer_key': 'bkp…',
        # access token secret
        'consumer_secret': 'pHUx…'
    },
    # https://console.developers.google.com/project
    "flask_social_blueprint.providers.Google": {
        # Client ID
        'consumer_key': '797….apps.googleusercontent.com',
        # Client secret
        'consumer_secret': 'bDG…'
    },
    # https://github.com/settings/applications/new
    "flask_social_blueprint.providers.Github": {
        # Client ID
        'consumer_key': '6f6…',
        # Client Secret
        'consumer_secret': '1a9…'
    },
}

# Settings with secrets
try: 
    from settings_local import *
except ImportError:
    pass    