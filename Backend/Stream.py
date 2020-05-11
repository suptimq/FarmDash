import datetime
import string
import random
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# defining the api-endpoint
API_ENDPOINT = "http://0.0.0.0:5000/stream"

class Stream():
    def __init__(self, userID):
        self.userID = userID
        application = Flask(__name__)
        application.config.from_object('config')
        self.db = SQLAlchemy(application)
        self.animalID = self.get_animal_ID()
        self.latest_time = self.get_latest_Time()
        self.time = datetime.datetime.strptime(self.latest_time, '%Y-%m-%d')

    def get_animal_ID(self):
        temp = self.db.engine.execute("select distinct animal_ID from records where userID=%s",
                                                self.userID).fetchall()
        animal_IDs = []
        for tuple in temp:
            animal_IDs.append(tuple[0])
        return animal_IDs

    def get_latest_Time(self):
        temp = self.db.engine.execute("select distinct time from records where userID=%s",
                                      self.userID).fetchall()
        time = []
        for tuple in temp:
            time.append(tuple[0])
        time.sort()
        if len(time) == 0:
            time.append('2018-01-01')
        return time[-1]

    def get_new_Time(self):
        self.time += datetime.timedelta(days=1)
        return str(self.time.date())


    def send(self):
        # data to be sent to api
        data = []
        for animal_ID in self.animalID:
            record = {
                'userID': self.userID,
                'time': self.get_new_Time(),
                'animal_ID': animal_ID,
                'group_ID': 999,
                'status':'milk',
                'milk_yield': random.randint(40000, 60000),
                'avg_fat': random.uniform(2, 4),
                'avg_protein': random.uniform(2, 4)
            }
            data.append(record)

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, json=data)

        # extracting response text
        pastebin_url = r.text
        print("The pastebin URL is:%s" % pastebin_url)

test = Stream(1)
for i in range(10):
    test.send()
