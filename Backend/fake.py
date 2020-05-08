import datetime
import string
import random
from application import db
from application.models import Records, User


# Assuming users are already stored in DB
class FakeHerdGenerator():
    def __init__(self, write=False, num_data=100, num_group=5, start='2018-03-01', end='2019-01-28'):
        self.num_data = num_data
        self.num_group = num_group
        self.start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end, "%Y-%m-%d")

        self.status = "Milk"

        # Write into DB or not
        self.write = write

        self.date_array = self.daterange(self.start_date, self.end_date)
        self.users = User.query.all()
        self.animals = self.random_animalID()
        self.groups = self.random_groudID()

        self.saved_records = []

    def generate_Records(self):
        # For each user, go through each date
        # For each date, go through each animal
        # The total number of records: num_user * num_date * num_animal
        for user in self.users:
            userID = user.id
            if userID == 1:
                print('SKIP USERID == 1')
                continue
            for date in self.date_array:
                for animal in self.animals:
                    groupID = random.sample(self.groups, 1)[0]
                    status = self.status
                    milk_yield = self.random_milkYield()
                    avg_fat = self.random_avgFat()
                    avg_protein = self.random_avgProtein()
                    record = Records(userID, date, animal,
                                     groupID, status, milk_yield, avg_fat, avg_protein)
                    self.saved_records.append(record)

        # Insert all data at one time
        if self.write:
            try:
                db.session.add_all(self.saved_records)
                db.session.commit()
                print('Successfully => {}'.format(self.saved_records))
                print('Total insert {} records'.format(len(self.saved_records)))
            except Exception as e:
                db.session.rollback()
                print("Rolledback:", e)
        else:
            print('Please enable write mode!')

        db.session.close()

    def daterange(self, start, end):
        date_array = [
            start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        date_array_format = [d.strftime("%Y-%m-%d") for d in date_array]

        return date_array_format

    def random_animalID(self):
        # list might not be exactly 100
        return list(set(random.randint(0, 1000) for _ in range(self.num_data)))

    def random_groudID(self):
        return list(set(random.randint(0, 1000) for _ in range(self.num_group)))

    def random_milkYield(self):
        return 0 if random.random() < 0.2 else random.randint(20000, 60000)

    def random_avgFat(self):
        return 0 if random.random() < 0.5 else random.uniform(0, 4)

    def random_avgProtein(self):
        return 0 if random.random() < 0.5 else random.uniform(0, 4)


class FakeUserGenerator():
    def __init__(self, write=False, num_user=100, email_len=7, user_len=3, ps_len=7):
        self.num_user = num_user
        self.email_len = email_len
        self.user_len = user_len
        self.ps_len = ps_len

        # Write into DB or not
        self.write = write

        self.email_set = set()
        self.username_set = set()
        self.saved_user = []

    def generate_Users(self):
        counter = 0
        while counter < self.num_user:
            email = self.random_Email(self.email_len)
            username = self.random_Username(self.user_len)
            password = self.random_Password(self.ps_len)

            # Dupliacte checking
            email_duplicate = email in self.email_set
            username_duplicate = username in self.username_set

            if not email_duplicate and not username_duplicate:
                counter += 1
                userDB = User(email, username, password)
                self.saved_user.append(userDB)
                self.email_set.add(email)
                self.username_set.add(username)

        # Insert all data at one time
        if self.write:
            try:
                db.session.add_all(self.saved_user)
                db.session.commit()
                print('Successfully => {}'.format(self.saved_user))
                print('Total insert {} records'.format(len(self.saved_user)))
            except Exception as e:
                db.session.rollback()
                print("Rolledback:", e)
        else:
            print('Please enable write mode!')

        db.session.close()

    def random_Email(self, length):
        nums = ''.join([str(i) for i in range(0, 10)])
        letters = string.ascii_letters
        candidates = nums + letters
        suffix = '@gmail.com'

        return ''.join(random.choice(candidates) for _ in range(length)) + suffix

    def random_Username(self, length):
        prefix = 'user_'
        nums = ''.join([str(i) for i in range(0, 10)])

        return prefix + ''.join(random.choice(nums) for _ in range(length))

    def random_Password(self, length):
        prefix = 'password_'
        nums = ''.join([str(i) for i in range(0, 10)])

        return prefix + ''.join(random.choice(nums) for _ in range(length))


if __name__ == "__main__":

    user_generator = FakeUserGenerator(write=True, num_user=3)
    herd_generator = FakeHerdGenerator(
        write=True, num_data=1, num_group=1, start='2018-03-01', end='2018-03-02')

    # These two functions should not be ran at the same time since unfixed database session problem
    # user_generator.generate_Users()
    herd_generator.generate_Records()

    # for u in User.query.all():
    #     print(u.id)
    #     print(u.email)

    # for r in Records.query.all():
    #     print(r)
