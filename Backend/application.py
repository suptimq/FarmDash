'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''
from flask import Flask, render_template, request, jsonify
from application import db, application
from application.models import Data, User
from DBOperation import DBOperation
from flask_cors import CORS
# Elastic Beanstalk initalization
# application = Flask(__name__)
application.debug = True
# change this to your own value
# application.secret_key = 'cC1YCIWOj9GgWspgNEo2'
# enable CORS
CORS(application, resources={r'/*': {'origins': '*'}})
myOperation = DBOperation()
@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        notes = "dead note"
        data_entered = Data(notes=notes)
        try:
            db.session.add(data_entered)
            db.session.commit()
        except:
            db.session.rollback()
        db.session.close()
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
        except:
            db.session.rollback()
            print("rolled back")
        db.session.close()
        return render_template('thanks.html', notes="add user successful")

    return render_template('base.html')


@application.route('/cow', methods=['GET'])
def get_data():
    # Bar chart data
    #   Dictionary: key-month, value-records within that month
    # print('Request cow id: {}'.format(cowID))
    print(request)
    cowID = request.args.get('ID')
    print(cowID)
    fat, protein, milkyield = myOperation.calc_Monthly(cowID)
    response = {
        'status': 'sucess',
        'fat_chart_data': fat,
        'protein_chart_data': protein,
        'milkyield_chart_data': milkyield
    }
    return jsonify(response)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
