# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
USER = 'admin'
PASSWORD = 'mypassword'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USER + ':' + PASSWORD + \
    '@mysql-dashboard.cj7rotsa2rnv.us-east-2.rds.amazonaws.com:3306/flaskdemo'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 3600


SQLALCHEMY_BINDS = {
    'master': SQLALCHEMY_DATABASE_URI,
    'slave': 'mysql+pymysql://' + USER + ':' + PASSWORD + '@mysql-dashboard-replica.cj7rotsa2rnv.us-east-2.rds.amazonaws.com:3306/flaskdemo'
}


WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
