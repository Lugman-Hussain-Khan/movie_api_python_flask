from app import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    country = db.Column(db.String(20))

    def __init__(self, name, country):
        self.name = name
        self.country = country
