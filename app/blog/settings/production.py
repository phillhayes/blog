from blog.settings.base import *
import dj_database_url
import psycopg2

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='ppostgres://zhvovrzcptdyap:0e8da72557f45175af9b17bd114224afcaa38e3abf67c48b92c857ecdb8edf33@ec2-23-21-76-49.compute-1.amazonaws.com:5432/d3mgec0s1hv3s2')
    
}
