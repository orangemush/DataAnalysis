import pymysql

pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_audi_prediction',
        'USER': 'root',
        'HOST': 'localhost',
        "PASSWORD": "12345678",
        'PORT': '3306',
    }
}
SECRET_KEY = 'django-insecure-&ns2fc#)7@^pcih8&av1gx--r9(x-g159hxd4kf++c4&h%aluk'