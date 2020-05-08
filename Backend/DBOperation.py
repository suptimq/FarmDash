from application import db
from application.models import Data, Records
import pandas as pd
import copy

class DBOperation():
    def __init__(self):
        self.records = []
        # self.fat, self.protein = self.calc_Monthly()

    def query_Monthly(self):
        return self.fat, self.protein

    def calc_All(self):
        records = Records.query.all()
        return records

    def calc_Monthly(self, animal_ID):
        print("Aggregating fat and protein data")
        fat = {}
        fat["2018"] = {}
        fat["2019"] = {}
        for i in range(1,13):
            fat["2018"][str(i)] = []
            fat["2019"][str(i)] = []
        protein = copy.deepcopy(fat)
        milkyield = copy.deepcopy(fat)

        if animal_ID == "all":
            records = Records.query.all()
            AVGFatRecords = {}
            AVGProteinRecords = {}
            AVGYieldRecords = {}
            for i in range(len(records)):
                record = records[i]
                if record.time not in AVGFatRecords:
                    AVGFatRecords[record.time] = [record.avg_fat]
                    AVGProteinRecords[record.time] = [record.avg_Protein]
                    AVGYieldRecords[record.time] = [record.milk_yield]
                else:
                    AVGFatRecords[record.time].append(record.avg_fat)
                    AVGProteinRecords[record.time].append(record.avg_Protein)
                    AVGYieldRecords[record.time].append(record.milk_yield)
            for time in AVGFatRecords:
                ymd = time.split("-")
                AVGFat = sum(AVGFatRecords[time]) / len(AVGFatRecords[time]) if (len(AVGFatRecords[time]) > 0) else sum(AVGFatRecords[time])
                AVGProtein = sum(AVGProteinRecords[time]) / len(AVGProteinRecords[time]) if (len(AVGProteinRecords[time]) > 0) else sum(AVGProteinRecords[time])
                AVGYield = sum(AVGYieldRecords[time]) / len(AVGYieldRecords[time]) if (len(AVGYieldRecords[time]) > 0) else sum(AVGYieldRecords[time])
                fat[ymd[0]][ymd[1]].append(AVGFat)
                protein[ymd[0]][ymd[1]].append(AVGProtein)
                milkyield[ymd[0]][ymd[1]].append(AVGYield)

        else:
            records = Records.query.filter_by(animal_ID = animal_ID).all()
            if len(records) != 0:
                for i in range(len(records)):
                    record = records[i]
                    ymd = record.time.split("-")
                    # first aggregate to one date "2018-3-1" then decomposite by month and date

                    fat[ymd[0]][ymd[1]].append(record.avg_fat)
                    protein[ymd[0]][ymd[1]].append(record.avg_Protein)
                    milkyield[ymd[0]][ymd[1]].append(record.milk_yield)
        return fat, protein, milkyield

    def create_DBs(self):
        db.create_all()
        print("DB created.")

    def create_Records(self):
        file = pd.read_excel("./data/13_DA Project_1.xlsx")
        userID = 1
        print("creating records")
        for i in range(len(file)):
            time = file["datesql"][i]
            if(isinstance(time, str)):
                dmy = time.split("/")
                time = dmy[2] + "-" + str(int(dmy[1])) + "-" + str(int(dmy[0]))
            else:
                time = str(time.year) + "-" + str(time.day) + "-" + str(time.month)

            animal_ID = int(file["Animal_ID"][i])
            group_ID = int(file["Group_ID"][i])
            status = file["AnimalStatus"][i]
            milk_yield = float(file["Yield(gr)"][i])
            # deal with nan values
            if(milk_yield != milk_yield):
                milk_yield = 0
            avg_fat = float(file["Avg_Fat(%)"][i])
            avg_protein = float(file["Avg_Protein(%)"][i])
            item = Records(userID, time, animal_ID, group_ID, status, milk_yield, avg_fat, avg_protein)
            try:
                db.session.add(item)
                db.session.commit()
                db.session.close()
                # print(item)
            except Exception as e:
                db.session.rollback()
                print("Rolledback:", e)

# myOperation = DBOperation()
# myOperation.create_Records()
# fat, protein = myOperation.calc_Monthly(animal_ID = "all")
# print(fat)
# print(protein)