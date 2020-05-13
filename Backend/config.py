# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
import random
USER = 'admin'
PASSWORD = 'mypassword'
URI = ['@mysql-dashboard.cj7rotsa2rnv.us-east-2.rds.amazonaws.com:3306/flaskdemo',
       '@mysql-dashboard-replica.cj7rotsa2rnv.us-east-2.rds.amazonaws.com:3306/flaskdemo']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USER + ':' + PASSWORD + URI[random.randint(0,1)]
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
