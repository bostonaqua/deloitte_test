db_name = 'deloitte'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'localhost'


class Config(object):
    SECRET_KEY = "its_my_secret"
    SQLALCHEMY_DATABASE_URI = "postgresql://" + db_user + ":" + db_pass + "@"+ db_host + "/" + db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
