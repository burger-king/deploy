REPO_DIR='{{ repos_dir }}'
ARCHIVE_DIR='{{ archives_dir }}'

SQLALCHEMY_DATABASE_URI = 'postgresql://{{ db_user }}:{{ db_pass }}@{{ db_host }}:{{ db_port }}/{{ db_name }}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '{{ salt }}' # note this _isn't_ the salt used for bcrypt as it generates its own
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_EMAIL_SENDER = '{{ mail_user }}'
SECURITY_URL_PREFIX = '/users'
SECURITY_REGISTER_URL = '/signup'
SECURITY_POST_LOGIN_VIEW = 'users.token'

MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_SERVER = '{{ mail_host }}'
MAIL_USERNAME = '{{ mail_user }}'
MAIL_PASSWORD = '{{ mail_pass }}'
MAIL_DEFAULT_SENDER = '{{ mail_user }}'
MAIL_DEBUG = False
