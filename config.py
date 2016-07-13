DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = "secret"

SECRET_KEY = u'$2b$12$/8ROyAhlsFqvldbGk3aLs.'



MAP_API_KEY = 'r9SdjiTsZJAGRBtmwkT5LBk9jp_XV_'
MAP_MODE = 'develop'