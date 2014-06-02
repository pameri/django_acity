# Django settings for osac project.
import os
#import djcelery
#djcelery.setup_loader()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#BROKER_URL = 'django://'
#BROKER_URL = 'amqp://guest:guest@localhost:5672/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },    
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
#HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'
#CELERY_HAYSTACK_DEFAULT_TASK = 'celery_haystack.tasks.CeleryHaystackSignalHandler'

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'sqlserver_ado', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'C:\\Aptana\\recetario\\recetario.db',                      # Or path to database file if using sqlite3.
        #'NAME': 'PORTAL',                      # Or path to database file if using sqlite3.
        'NAME': 'BM2012',
        'USER': 'sa',                      # Not used with sqlite3.
        'PASSWORD': 'sistemas',                  # Not used with sqlite3.
        'HOST': '172.16.3.19\BM2008',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
                    #'provider': 'SQLOLEDB',
                    'provider': 'SQLNCLI10',                    
                    #'use_mars' : True,
                    'extra_params': 'DataTypeCompatibility=80;MARS Connection=True;',                    
                    }
    },
    'osac': {
        'ENGINE': 'sqlserver_ado',
        'NAME': 'BDAPPV1',
        'USER': 'sa',
        'PASSWORD': 'sistemas',
        'HOST': 'marte\bmmanager',
        'PORT': '',
        'OPTIONS': {
                    #'provider': 'SQLOLEDB',
                    'provider': 'SQLNCLI10',                    
                    #'use_mars' : True,
                    'extra_params': 'DataTypeCompatibility=80;MARS Connection=True;',                    
                    }
        
    }
}
TASTYPIE_DEFAULT_FORMATS = ['json','xml']
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Lima'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-pe'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '' #os.path.normpath(os.path.join(os.path.dirname(__file__),'static/'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
# Additional locations of static files
STATICFILES_DIRS = (
                    
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=pqb(@23eocjqf+apmeh2j25t)ed#1ddv@19g6dh(d1rtotj+-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  #'zinnia.context_processors.version',
  ) # Optional

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'portal.urls'

#Identificar o definir el perfil de los usuarios
AUTH_PROFILE_MODULE = 'home.userProfile'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'portal.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


#LOGIN_URL =  '/login/'
#LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType #,ActiveDirectoryGroupType

#DEBUG_TOOLBAR_PATCH_SETTINGS = False


    
    
# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://172.16.3.20"

AUTH_LDAP_BIND_DN = "administrator@atlanticcity.local"
#AUTH_LDAP_BIND_DN = 'cn=administrator,cn=Users,dc=atlanticcity,dc=local'
AUTH_LDAP_BIND_PASSWORD = "ren@ultf1"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=atlantic_city,dc=atlanticcity,dc=local", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
#AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=atlantic_city,dc=atlanticcity,dc=local", ldap.SCOPE_SUBTREE, "(userPrincipalName=%(user)s)")
#AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=atlantic_city,dc=atlanticcity,dc=local", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
#AUTH_LDAP_GROUP_SEARCH = LDAPSearch('ou=atlantic_city,dc=atlanticcity,dc=local', ldap.SCOPE_SUBTREE, '(objectClass=group)')
#AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# Only users in this group can log in.
#AUTH_LDAP_REQUIRE_GROUP = 'cn=enabled,ou=atlantic_city,dc=atlanticcity,dc=local'


# Set up the basic group parameters.
#AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=atlantic_city,ou=groups,dc=atlanticcity,dc=local",ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"



# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}


#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    'is_active': 'cn=active,ou=atlantic_city,dc=atlanticcity,dc=local',
#    'is_staff': 'cn=staff,ou=atlantic_city,dc=atlanticcity,dc=local',
#    'is_superuser': 'cn=superuser,ou=atlantic_city,dc=atlanticcity,dc=local'
#}

# This is the default, but I like to be explicit.
#AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
#AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for 5 minutes to reduce LDAP traffic
#AUTH_LDAP_CACHE_GROUPS = True
#AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300
#AUTH_LDAP_GLOBAL_OPTIONS = {
#    ldap.OPT_X_TLS_REQUIRE_CERT: False,
#    ldap.OPT_REFERRALS: False,
#}


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',    
    'portal.apps.home', 
    #'portal.apps.osac',
    #'portal.apps.blog',
    'portal.apps.bmpedido',
    #'portal.apps.webServices.wsProductos',
    #'haystack',
    #'south',
    #'tastypie'
    #'debug_toolbar',
    #'sqlserver_ado.sql_app',
    #'tagging',
    #'mptt',
    #'zinnia',    
    #'django-tastypie'
    #'djcelery',
    #'celerytest',
    #'kombu.transport.django',
    # 'celery_haystack',
    #'queued_search',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


