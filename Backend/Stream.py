import datetime
import threading
import logging
import random
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# defining the api-endpoint
API_ENDPOINT = "http://0.0.0.0:5000/stream"
application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
class Stream():
    def __init__(self, userID):
        self.userID = userID
        self.animalID = self.get_animal_ID()
        self.latest_time = self.get_latest_Time()
        self.time = datetime.datetime.strptime(self.latest_time, '%Y-%m-%d')
        self.log = []

    def get_animal_ID(self):
        temp = db.engine.execute("select distinct animal_ID from records where userID=%s",
                                                self.userID).fetchall()
        animal_IDs = []
        for tuple in temp:
            animal_IDs.append(tuple[0])
        return animal_IDs

    def get_latest_Time(self):
        temp = db.engine.execute("select distinct time from records where userID=%s",
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
        time = self.get_new_Time()
        for animal_ID in self.animalID:
            record = {
                'userID': self.userID,
                'time': time,
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
        self.log.append(r.elapsed.total_seconds())
        # extracting response text
        # pastebin_url = r.text
        # print("The pastebin URL is:%s" % pastebin_url)

# clear up fake generate stream data
db.engine.execute("SET SQL_SAFE_UPDATES = 0")
db.engine.execute("Delete from records where group_ID = 999")
# get all userIDs
temp = db.engine.execute("select id from user").fetchall()
userIDs = []
for tuple in temp:
    userIDs.append(tuple[0])

def send_requests(userID, num_of_records = 15):
    test = Stream(userID)
    for i in range(num_of_records):
        test.send()
    print(test.log)
threads = []
for index, userID in enumerate(userIDs):
    logging.info("Main : create and start thread for userID %d at thread %d.", userID, index)
    t = threading.Thread(target=send_requests, args=(userID, 15))
    threads.append(t)
    t.start()

for index, thread in enumerate(threads):
    thread.join()
    logging.info("Main : End thread for thread %d.", index)
print("all threads fininshed")
