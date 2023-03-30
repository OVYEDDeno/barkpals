from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey

db = SQLAlchemy()
owner_dogs = db.Table('owner_dogs',
    db.Column('owner_id', db.Integer, db.ForeignKey('owner.id'), primary_key=True),
    db.Column('dog_id', db.Integer, db.ForeignKey('dogs.id'), primary_key=True)
)

dog_breed = db.Table('dog_breed',
    db.Column('dog_id', db.Integer, db.ForeignKey('dogs.id'), primary_key=True),
    db.Column('breed_id', db.Integer, db.ForeignKey('breeds.id'), primary_key=True)
)
owner_dogs_playdates = db.Table('owner_dogs_playdates',
    db.Column('owner_id', db.Integer, db.ForeignKey('owner.id'), unique=True, primary_key=True),
    db.Column('dogs_id', db.Integer, db.ForeignKey('dogs.id'), unique=True, primary_key=True),
    db.Column('playdates_id', db.Integer, db.ForeignKey('playdates.id'), unique=True, primary_key=True)
)

class Owner(db.Model):
    __tablename__='owner'
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(200), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    zipcode = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # dogs = db.relationship('Dogs', secondary=owner_dogs, lazy='subquery')


    def __repr__(self):
        return f'<Owner {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "img_url": self.img_url,
            "name": self.name,
            "zipcode": self.zipcode,
            "email": self.email,
            # "dogs":list(map(lambda x: x.serialize(), self.dogs))

            # do not serialize the password, its a security breach
        }
class Dogs(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(200), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    breed = db.relationship('Breeds', secondary=dog_breed, lazy='subquery')
    chip_number = db.Column(db.Integer, unique=True, nullable=False)
    weight= db.Column(db.Float(precision=2), unique=False, nullable=False)
    neutered_or_spayed= db.Column(db.Boolean(), unique=False, nullable=False)
    owner_id = db.Column(db.Integer, ForeignKey('owner.id'), nullable=False)
    owner = db.relationship('Owner', foreign_keys=[owner_id], backref=db.backref('dogs', lazy=True))

    def __repr__(self):
        return f'<Dog {self.chip_number}>'

    def serialize(self):
        return {
            "id": self.id,
            "img_url": self.img_url,
            "name": self.name,
            "breed":list(map(lambda x: x.name, self.breed)),
            "chip_number": self.chip_number,
            "weight": self.weight,
            "neutered_or_spayed": self.neutered_or_spayed,
        }
class Breeds(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    temperament = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return f'<Breed {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "temperament": self.temperament,
            

        }

class Playdates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.relationship('Message', backref='playdate', lazy=True)
    dog1_id = db.relationship('Dogs', secondary=owner_dogs_playdates, lazy='subquery')
    dog2_id = db.relationship('Dogs', secondary=owner_dogs_playdates, lazy='subquery')
    # dog2_id = db.Column(db.Integer, ForeignKey('dogs.id'), nullable=False)
    # owner = db.relationship('Dogs', foreign_keys=[owner1_id], backref=db.backref('Owner', lazy=True))

    owner1_id = db.relationship('Owner', secondary=owner_dogs_playdates, lazy='subquery')
    # owner1_id = db.Column(db.Integer, ForeignKey('owner.id'), nullable=False)
    # owner = db.relationship('Owner', foreign_keys=[owner1_id], backref=db.backref('dogs', lazy=True))
    owner2_id = db.relationship('Owner', secondary=owner_dogs_playdates, lazy='subquery')
    # owner2_id = db.Column(db.Integer, ForeignKey('owner.id'), nullable=False)
    # owner = db.relationship('Owner', foreign_keys=[owner2_id], backref=db.backref('dogs', lazy=True))

    def __repr__(self):
        return f'<Playdates {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "dog1_id": Dogs.query.get(self.dog1_id).serialize(),
            "dog2_id": Dogs.query.get(self.dog2_id).serialize(),
            "owner1_id": Owner.query.get(self.owner1_id).serialize(),
            "owner2_id": Owner.query.get(self.owner2_id).serialize(),
            "messages": [message.serialize() for message in self.messages],
        }



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(120), unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)

    sender_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    playdate_id = db.Column(db.Integer, db.ForeignKey('playdates.id'), nullable=False)
    
    def __repr__(self):
        return f'<Message {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp,
            "sender": Owner.query.get(self.sender_id).serialize(),
        }