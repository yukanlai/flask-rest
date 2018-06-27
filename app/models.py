from app import db

class Animal(db.Model):
    """
    Create a Animal table
    """

    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.String(60), unique=True)
    sex = db.Column(db.String(60))
    age = db.Column(db.String(60))

    def __repr__(self):
        return '<Animal: {}>'.format(self.animal_id)
