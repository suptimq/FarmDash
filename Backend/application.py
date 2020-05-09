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


@application.route('/login', methods=['POST'])
def login():
    # Three cases when dealing with user authentication
    # code-200: succes, code-100: password unmatched, code-300: user not fount
    if request.method == 'POST':
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            print('here')
            if user.password == password:
                user_obj = {'username': user.username, 'email': user.email}
                resp = {'user': user_obj, 'msg': 'success', 'code': 200}
                return jsonify(resp)
            else:
                resp = {'msg': 'failure', 'code': 100}
                return jsonify(resp)
        else:
            resp = {'msg': 'failure', 'code': 300}
            return jsonify(resp)


@application.route('/register', methods=['GET', 'POST'])
def register():
    # Three cases when dealing with user registration
    # code-200: succes, code-100: user exists, code-300: database error
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        email = post_data.get('email')
        username = post_data.get('username')
        password = post_data.get('password')

        userExist = User.query.filter_by(email=email).all()
        if userExist:
            resp = {'msg': 'failure', 'code': 100}
            return jsonify(resp)

        userDB = User(email, username, password)
        try:
            db.session.add(userDB)
            db.session.commit()
            resp = {'msg': 'success', 'code': 200}
        except:
            db.session.rollback()
            print("rolled back")
            resp = {'msg': 'failure', 'code': 300}
        db.session.close()
        return jsonify(resp)


@application.route('/cow', methods=['GET'])
def get_data():
    # Bar chart data
    #   Dictionary: key-month, value-records within that month
    # print('Request cow id: {}'.format(cowID))
    # print(request)
    cowID = request.args.get('ID')
    userEmail = request.args.get('email')
    # print(cowID)
    # print(userEmail)
    user = User.query.filter_by(email=userEmail).first()
    userID = user.id
    # print(userID)
    fat, protein, milkyield = myOperation.calc_Monthly(userID, cowID)
    cows = myOperation.get_CowIDs(userID)
    response = {
        'status': 'sucess',
        'fat_chart_data': fat,
        'protein_chart_data': protein,
        'milkyield_chart_data': milkyield,
        'cows': cows
    }
    return jsonify(response)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
