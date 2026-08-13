

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base



Base = declarative_base()
class Personal_details(Base):
    __tablename__ = 'details'
    id = Column('id', Integer, primary_key=True)
    first_name = Column("firstname", String)
    last_name = Column('lastname', String)
    email = Column('email', String)
    dob = Column('dob', String)
    age = Column('age', Integer)
    days = Column('days', String)
    months = Column('months', String)
    years = Column('years', String)
    marks = Column('marks', Integer)
    outof = Column('outof', Integer)
    percentage = Column('percentage', String)
    aadhar_no = Column('aadhar_no', String)

    def __init__(self, first_name, last_name, email, dob, age, days, months, years, marks, outof, percentage, aadhar_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
        self.age = age
        self.days = days
        self.months = months
        self.years = years
        self.marks = marks
        self.outof = outof
        self.percentage = percentage
        self.aadhar_no = aadhar_no
engine = create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_form_data(personal_details):


    # query = """CREATE TABLE IF NOT EXISTS form_data (
    # FIRST_NAME TEXT, LAST_NAME TEXT, EMAIL TEXT, DOB TEXT, DAYS TEXT, MONTHS TEXT, YEARS TEXT, MARKS TEXT, AADHAR NO TEXT)"""
    #
    # query = """INSERT INTO form_data values (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    session.add(personal_details)
    session.commit()

    detail = session.get(Personal_details,personal_details.email)
    print(personal_details.email)
    print("Details:",detail)
    return detail

def get_data():
    arr = []
    try:
        data = session.query(Personal_details).all()
        print(data, type(data))
        for detail in data:
            print(detail)
            arr.append(detail)
    except:
        return Exception("No Data")
    finally:
        session.close()
    print(arr)
    return arr

