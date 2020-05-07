from application import db
from application.models import Data, Records
import pandas as pd

# db.create_all()
# print("DB created.")
file = pd.read_excel("./data/13_DA Project_1.xlsx")
userID = 1
for i in range(len(file)):
    time = file["datesql"][i]
    if(isinstance(time, str)):
        dmy = time.split("/")
        time = dmy[2] + "-" + dmy[1] + "-" + dmy[0]
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