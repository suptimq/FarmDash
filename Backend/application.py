'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request
from application import db, application
from application.models import Data, User

# Elastic Beanstalk initalization
# application = Flask(__name__)
application.debug = True
# change this to your own value
# application.secret_key = 'cC1YCIWOj9GgWspgNEo2'


@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        notes = "dead note"
        data_entered = Data(notes=notes)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=notes)

    return render_template('base.html')

@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        data_entered = User(email, username, password)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
            print("rolled back")
        return render_template('thanks.html', notes="add user successful")

    return render_template('base.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0')
