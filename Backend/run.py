from flask import Flask, jsonify, request
from flask_cors import CORS
import random

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/cow', methods=['GET'])
def get_data():
    # Bar chart data
    #   Dictionary: key-month, value-records within that month
    # print('Request cow id: {}'.format(cowID))
    print(request)
    cowID = request.args.get('ID')
    year = request.args.get("Year")
    print(cowID)

    fat_chart_data = {'Jan': [random.randint(0, 100) for _ in range(31)], 'Feb': [
        random.randint(0, 100) for _ in range(28)]}

    protein_chart_data = {'Jan': [random.randint(0, 100) for _ in range(31)], 'Feb': [
        random.randint(0, 100) for _ in range(28)]}

    response = {
        'status': 'sucess',
        'fat_chart_data': fat_chart_data,
        'protein_chart_data': protein_chart_data,
    }
    return jsonify(response)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    # print(from_internet())
    # import sys
    # sys.exit()
    app.run()
