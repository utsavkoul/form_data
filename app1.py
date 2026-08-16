# This is a sample Python script.
from datetime import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request, redirect, url_for
from datetime import *; from dateutil.relativedelta import *
import calendar
# from database_mysql import Personal_details, add_form_data, get_data
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
import re

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__, template_folder='templates')

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:root@localhost:{3306}/database"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'my-secret-key'
    db = SQLAlchemy(app)
    login_manager = LoginManager(app)
    login_manager.login_view = "login"




    class Personal_details(db.Model):
        __tablename__ = 'details'
        id = db.Column(db.Integer, primary_key=True)
        first_name =db.Column(db.String(100))
        last_name = db.Column(db.String(100))
        email = db.Column(db.String(100))
        dob = db.Column(db.String(10))
        age = db.Column(db.Integer)
        days = db.Column(db.Integer)
        months = db.Column(db.Integer)
        years = db.Column(db.Integer)
        marks = db.Column(db.Integer)
        outof = db.Column(db.Integer)
        percentage = db.Column(db.String(10))
        aadhar_no = db.Column(db.String(100))
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

        def __init__(self, first_name, last_name, email, dob, age, days, months, years, marks, outof, percentage, aadhar_no, current_user_id):
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
            self.user_id = current_user_id

    class User(UserMixin,db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100))
        email = db.Column(db.String(100))
        password_hash = db.Column(db.String(100))
        def set_password(self, password):
            self.password_hash = generate_password_hash(password)
        def check_password(self, password):
            return check_password_hash(self.password_hash, password)
    with app.app_context():
        db.create_all()


    def get_data(user_id):
         return db.session.query(Personal_details).where(Personal_details.user_id==user_id)
    def add_form_data(personal_details):
        db.session.add(personal_details)
        db.session.commit()
    @app.route('/', methods=['GET'])
    def index():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        errors = []
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # Add remember me checkbox
            # Redirect to the specified page
            if username == '' or password == '':
                errors.append("Enter Username and Password")
            if not errors:
                user = User.query.filter_by(username=username).first()
                if user and user.check_password(password):
                    login_user(user)
                    return redirect(url_for('dashboard'))
                else:
                    return "Username and Password is incorrect"
        return render_template("login.html", errors=errors)
    #   check if username and password in database
    #   login() - redirect to dashboard
    #   Incorrect password
    #   error message

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        errors=[]
        if request.method == "POST":
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            confirm = request.form['confirm_password']
            print("Register Details",username, email, password, confirm )
            if not 3 <= len(username) <= 80:
                errors.append("Username must be at least 3 characters long")
            if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
                errors.append('Enter valid email address')
            if len(password) <6 :
                errors.append("Password must be at least 6 characters long")
            if password != confirm:
                errors.append("Passwords does not match")
            # If user already exist
            if not errors:
                try:
                    user = User(username=username, email=email)
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('index'))
                except IntegrityError:
                    db.session.rollback()
                    errors.append("Username already exist")
        return render_template("register.html", errors=errors)



    @app.route('/logout', methods=['GET'])
    def logout():
        logout_user()
        return redirect(url_for('index'))


    @app.route('/dashboard', methods=['GET', 'POST'])
    @login_required
    def dashboard():
        if request.method == 'GET':
            pass
            data = get_data(current_user.id)
            # return render_template('dashboard.html', data=data, detail_msg='Details', first_name='', last_name='',email='', dob='', days='', months='', years='', percentage='', aadhar_no='')data = get_data()
            return render_template('dashboard.html', all_data=data, detail_msg='Details', current_user=current_user.username, first_name='', last_name='',email='', dob='', days='', months='', years='', percentage='', aadhar_no='')
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            dob = str(request.form['dob'])
            marks = request.form['marks']
            outof = request.form['outof']
            aadhar_no = request.form['aadhar_no']

            dob_year = datetime.strptime(dob, "%Y-%m-%d")
            present = datetime.now()
            percentage = (float(marks) / float(outof)) * 100
            if dob_year <= datetime.now():
            # days = present.day - dob_year.day
            # months = present.month - dob_year.month
            # years = present.year - dob_year.year
                total_time = relativedelta(present, dob_year)
                print(total_time)
                age = total_time.years
                personal_details = Personal_details(first_name, last_name, email, dob, age, total_time.days,
                                                    total_time.months, total_time.years, marks, outof, percentage, aadhar_no, current_user.id)

                add_form_data(personal_details)
            else:
                raise Exception("Date selected is greater than current date")

            print(first_name, last_name, email, dob, total_time, total_time.days, total_time.months, total_time.years, marks, outof, percentage, aadhar_no)


            all_data = get_data(current_user.id)
            return render_template('dashboard.html', current_user=current_user.username, detail_msg='Details', all_data=all_data, first_name=first_name, last_name=last_name,email=email, dob=dob, age=age, days=total_time.days, months=total_time.months, years=total_time.years, percentage=percentage, aadhar_no=aadhar_no)


    @app.route('/form', methods=['POST'])
    def form():
        data = 'get_data()'
        return render_template('dashboard.html', data=data, detail_msg='Details', first_name='', last_name='', email='', dob='',
                               days='', months='', years='', percentage='', aadhar_no='')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    app.run(debug=True)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
