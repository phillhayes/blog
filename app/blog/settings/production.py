from blog.settings.base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': database_url.config(
        default=config('postgres://klbmmkfsjdvcvu:bfa886f7ed4282f5ba334759bb83ba483c85fc7b62f51b7e1b29af2b690b0919@ec2-23-23-186-157.compute-1.amazonaws.com:5432/d413hlnpbnaa80')
    )
    
}
