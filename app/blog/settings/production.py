from blog.settings.base import *
import dj_database_url
import psycopg2

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://iyryaqdtrktgwu:b877a6a3371d472f0f0681eb6abd9072dfce4dfc135497c9f785bcef0e5e812f@ec2-54-243-185-132.compute-1.amazonaws.com:5432/dbehmul6ht3sfn')
    
}
