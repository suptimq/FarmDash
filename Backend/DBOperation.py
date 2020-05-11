from application import db
from application.models import Data, Records, User
import pandas as pd
import copy

from pdb import set_trace

# For outside querying items in the database


class DBOperation():
    def __init__(self):
        self.records = []
        # self.fat, self.protein = self.calc_Monthly()

    def query_Monthly(self):
        return self.fat, self.protein

    def calc_All(self):
        records = Records.query.all()
        return records

    def get_CowIDs(self, userID):
        # Return all the cow ID for the current user
        temp = db.engine.execute("select distinct animal_ID from records where userID=%s",
                                 userID).fetchall()
        animal_IDs = []
        for tuple in temp:
            animal_IDs.append(tuple[0])
        return animal_IDs

    def calc_Monthly(self, userID, animal_ID):
        print("Aggregating fat and protein data")
        fat = {}
        protein = copy.deepcopy(fat)
        milkyield = copy.deepcopy(fat)

        # Store the appearing years
        year = set()

        if animal_ID == "all":
            records = Records.query.filter_by(userID=userID).all()
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
                # Remove leading zeros
                ymd = [y.lstrip("0") for y in ymd]
                AVGFat = sum(AVGFatRecords[time]) / len(AVGFatRecords[time]) if (
                    len(AVGFatRecords[time]) > 0) else sum(AVGFatRecords[time])
                AVGProtein = sum(AVGProteinRecords[time]) / len(AVGProteinRecords[time]) if (
                    len(AVGProteinRecords[time]) > 0) else sum(AVGProteinRecords[time])
                AVGYield = sum(AVGYieldRecords[time]) / len(AVGYieldRecords[time]) if (
                    len(AVGYieldRecords[time]) > 0) else sum(AVGYieldRecords[time])
                if ymd[0] not in fat:
                    fat[ymd[0]] = {}
                    protein[ymd[0]] = {}
                    milkyield[ymd[0]] = {}
                    # Add the year
                    year.add(ymd[0])
                    for i in range(1, 13):
                        fat[ymd[0]][str(i)] = []
                        protein[ymd[0]][str(i)] = []
                        milkyield[ymd[0]][str(i)] = []

                fat[ymd[0]][ymd[1]].append(AVGFat)
                protein[ymd[0]][ymd[1]].append(AVGProtein)
                milkyield[ymd[0]][ymd[1]].append(AVGYield)

        else:
            records = Records.query.filter_by(
                userID=userID, animal_ID=animal_ID).all()

            if len(records) != 0:
                for i in range(len(records)):
                    record = records[i]
                    ymd = record.time.split("-")

                    # Remove leading zeros
                    ymd = [y.lstrip("0") for y in ymd]
                    # first aggregate to one date "2018-3-1" then decomposite by month and date
                    if ymd[0] not in fat:
                        fat[ymd[0]] = {}
                        protein[ymd[0]] = {}
                        milkyield[ymd[0]] = {}
                        # Add the year
                        year.add(ymd[0])
                        for i in range(1, 13):
                            fat[ymd[0]][str(i)] = []
                            protein[ymd[0]][str(i)] = []
                            milkyield[ymd[0]][str(i)] = []

                    fat[ymd[0]][ymd[1]].append(record.avg_fat)
                    protein[ymd[0]][ymd[1]].append(record.avg_Protein)
                    milkyield[ymd[0]][ymd[1]].append(record.milk_yield)
        return fat, protein, milkyield, list(year)

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
                time = str(time.year) + "-" + str(time.day) + \
                    "-" + str(time.month)

            animal_ID = int(file["Animal_ID"][i])
            group_ID = int(file["Group_ID"][i])
            status = file["AnimalStatus"][i]
            milk_yield = int(file["Yield(gr)"][i])
            # deal with nan values
            if(milk_yield != milk_yield):
                milk_yield = 0
            avg_fat = float(file["Avg_Fat(%)"][i])
            avg_protein = float(file["Avg_Protein(%)"][i])
            item = Records(userID, time, animal_ID, group_ID,
                           status, milk_yield, avg_fat, avg_protein)
            try:
                db.session.add(item)
                db.session.commit()
                # print(item)
            except Exception as e:
                db.session.rollback()
                print("Rolledback:", e)

            db.session.close()

    def stream(self, jsonArray):
        records = []
        for json in jsonArray:
            userID = int(json["userID"])
            time = json["time"]
            animal_ID = int(json["animal_ID"])
            group_ID = int(json["group_ID"])
            status = json["status"]
            milk_yield = int(json["milk_yield"])
            avg_fat = float(json["avg_fat"])
            avg_protein = float(json["avg_protein"])
            item = Records(userID, time, animal_ID, group_ID,
                           status, milk_yield, avg_fat, avg_protein)
            records.append(item)
        try:
            db.session.bulk_save_objects(records)
            db.session.commit()
            # print(item)
        except Exception as e:
            db.session.rollback()
            print("Rolledback:", e)

        db.session.close()

    def delete_DBs(self, userIDs):
        # Delete all records containing the specified userID
        # Return the number of deleted items
        total_del = 0
        for userID in userIDs:
            total_del += Records.query.filter_by(userID=userID).delete()

        print('Successfully delete {} records'.format(total_del))

        db.session.commit()
        return total_del


if __name__ == "__main__":

    myOperation = DBOperation()

    # userIDs = []
    # for u in User.query.all():
    #     if u.id != 1:
    #         userIDs.append(u.id)
    # print(userIDs)
    # myOperation.delete_DBs(userIDs)

    # myOperation.get_CowIDs(1)
    # myOperation.create_Records()
    # fat, protein = myOperation.calc_Monthly(animal_ID = 2714)
    # print(fat)
    # print(protein)
