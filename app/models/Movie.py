from app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(40))
    run_time = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    company = db.relationship("Company", backref="movies")

    def __init__(self, title, genre, run_time, company_id):
        self.title = title
        self.genre = genre
        self.run_time = run_time
        self.company_id = company_id
