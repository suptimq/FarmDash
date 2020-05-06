from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    
    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=False)
    username = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128), index=True, unique=False)
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Data %r>' % self.username

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time = db.Column(db.String(128), index=True, unique=False)
    animal_ID = db.Column(db.String(128), index=True, unique=False)
    group_ID = db.Column(db.String(128), index=True, unique=False)
    status = db.Column(db.String(128), index=True, unique=False)
    milk_yield = db.Column(db.Integer, index=True, unique=False)
    avg_fat = db.Column(db.Float, index=True, unique=False)
    avg_Protein = db.Column(db.Float, index=True, unique=False)

    def __init__(self, item, userID):
        self.userID = userID
        self.time = item["time"]
        self.animal_ID = item["animal_ID"]

    def __repr__(self):
        return '<Data %r>' % self.id