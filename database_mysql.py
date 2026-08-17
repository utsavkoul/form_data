# from calendar import Month
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:root@localhost:{3306}/details"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class Personal_details(db.Model):
#     __tablename__ = 'details'
#     id = db.Column(db.Integer, primary_key=True)
#     first_name =db.Column(db.String(100))
#     last_name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     dob = db.Column(db.String(10))
#     age = db.Column(db.Integer)
#     days = db.Column(db.Integer)
#     months = db.Column(db.Integer)
#     years = db.Column(db.Integer)
#     marks = db.Column(db.Integer)
#     outof = db.Column(db.Integer)
#     percentage = db.Column(db.String(10))
#     aadhar_no = db.Column(db.String(100))
#
#     def __init__(self, first_name, last_name, email, dob, age, days, months, years, marks, outof, percentage, aadhar_no):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.dob = dob
#         self.age = age
#         self.days = days
#         self.months = months
#         self.years = years
#         self.marks = marks
#         self.outof = outof
#         self.percentage = percentage
#         self.aadhar_no = aadhar_no
#
# def add_form_data(personal_details):
#     db.session.add(personal_details)
#     db.session.commit()
# def get_data():
#     arr=[]
#     all_data = db.session.query(Personal_details).all()
#     for data in all_data:
#         arr.append(data)
#
#     return arr
#
#
#
# personal_details = Personal_details(first_name="Utsav",last_name='Koul', email='koulutsav123@gmail.com', dob='11-01-2002', age=24, days=1, months=1, years=24, marks=90, outof=100, percentage=90, aadhar_no=1142345424)
#
#
#
#
#
# with app.app_context():
#     db.create_all()
#
#     add_data(personal_details)