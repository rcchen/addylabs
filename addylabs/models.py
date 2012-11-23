
# Attributes are characteristics of a Person that are specific
# to a particular Category

class Attribute(db.Model):

    __tablename__ = 'attributes'
    id = db.Column('attributeId', db.Integer, primary_key = True)
    person = db.Column(db.Integer)
    category = db.Column(db.Integer)
    text = db.Column(db.String(1000))
    date = db.Column(db.DateTime)

    def __init__(self, person, category, text):
        self.person = person
        self.category = category
        self.text = text
        self.date = datetime.utcnow()

# Categories are defined by a User for Attributes. For example
# the attribute "Sushi from Kaenyama" would go under the category
# of "Food"

class Category(db.Model):

    __tablename__ = 'categories'
    id = db.Column('categoryId', db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    userid = db.Column(db.Integer)

    def __init__(self, name, userid):
        self.name = name
        self.userid = userid

# A Person is defined by a User and can have Attributes

class Person(db.Model):

    __tablename__ = 'persons'
    id = db.Column('personId', db.Integer, primary_key = True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    userid = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, firstname, lastname, userid):
        self.firstname = firstname
        self.lastname = lastname
        self.userid = userid
        self.date = datetime.utcnow()

# The User is the person who uses the application. The User
# creates Persons, Categories, and assigns Attributes to Persons
# that fall under certain Categories

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column('userId', db.Integer, primary_key = True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = hashlib.sha224(password)
